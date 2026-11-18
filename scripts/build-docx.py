#!/usr/bin/env python3
"""Export legal HTML main content to editable DOCX with Python 3 only.

No Office automation, network access or third-party dependencies. Generate every
file in private staging before replacing exports. Source HTML is authoritative.
"""
import argparse
from dataclasses import dataclass, field
from datetime import datetime, timezone
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import tempfile
from urllib.parse import urljoin, urlparse
from xml.etree import ElementTree as E
from zipfile import ZipFile, ZIP_DEFLATED

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
R = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
REL = 'http://schemas.openxmlformats.org/package/2006/relationships'
CT = 'http://schemas.openxmlformats.org/package/2006/content-types'
E.register_namespace('w', W)
E.register_namespace('r', R)
BASE = 'https://paulofrancissoftware.github.io/brainybee_schools_docs/'
PAGES = [
 ('privacy-policy', 'Privacy-Policy'), ('coppa-direct-notice', 'COPPA-Direct-Notice'),
 ('school-services-agreement', 'Services-Agreement'), ('data-privacy-addendum', 'Data-Privacy-Addendum'),
 ('parent-guardian-notice', 'Parent-Guardian-Notice'), ('data-retention-deletion', 'Data-Retention-and-Deletion-Policy'),
 ('security-overview', 'Security-Overview'), ('subprocessors', 'Subprocessor-List'),
 ('data-requests', 'Data-Request-Procedure'), ('secure-export-delivery', 'Secure-Export-Delivery-Procedure'),
 ('information-security-program', 'Written-Information-Security-Program'),
 ('privacy-security-risk-assessment', 'Privacy-and-Security-Risk-Assessment'),
 ('incident-response-plan', 'Incident-Response-Plan'), ('subprocessor-assurance-register', 'Subprocessor-Assurance-Register'),
 ('quebec-privacy-impact-assessment', 'Quebec-Cross-Border-Privacy-Impact-Assessment')]
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}
BLOCK = {'p', 'div', 'section', 'article', 'h1', 'h2', 'h3', 'h4', 'ul', 'ol', 'table', 'pre', 'blockquote'}


@dataclass
class Node:
    tag: str
    attrs: dict = field(default_factory=dict)
    children: list = field(default_factory=list)


class Parser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node('root')
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        node = Node(tag, dict(attrs))
        self.stack[-1].children.append(node)
        if tag not in VOID:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                break

    def handle_data(self, data):
        self.stack[-1].children.append(data)


def descendants(node, tag):
    for child in node.children:
        if isinstance(child, Node):
            if child.tag == tag:
                yield child
            yield from descendants(child, tag)


def el(parent, tag, **attrs):
    return E.SubElement(parent, '{%s}%s' % (W, tag), {'{%s}%s' % (W, k): str(v) for k, v in attrs.items()})


def xml(root):
    return E.tostring(root, encoding='utf-8', xml_declaration=True)


class Document:
    def __init__(self):
        self.root = E.Element('{%s}document' % W)
        self.body = el(self.root, 'body')
        self.rels = E.Element('Relationships', xmlns=REL)
        for name in ('styles', 'numbering'):
            E.SubElement(self.rels, 'Relationship', Id=name, Type=R + '/' + name, Target=name + '.xml')
        self.numbering = E.Element('{%s}numbering' % W)
        for abstract, fmt in ((0, 'bullet'), (1, 'decimal')):
            a = el(self.numbering, 'abstractNum', abstractNumId=abstract)
            el(a, 'multiLevelType', val='multilevel')
            for level in range(9):
                lv = el(a, 'lvl', ilvl=level)
                el(lv, 'start', val=1)
                el(lv, 'numFmt', val=fmt)
                el(lv, 'lvlText', val='\u2022' if fmt == 'bullet' else '%%%s.' % (level + 1))
                pp = el(lv, 'pPr')
                el(pp, 'ind', left=360 * (level + 1), hanging=240)
        self.num_count = 0
        self.source = ''

    def paragraph(self, parent, style=None, numbering=None):
        p = el(parent, 'p')
        if style or numbering:
            pp = el(p, 'pPr')
            if style:
                el(pp, 'pStyle', val=style)
            if numbering:
                np = el(pp, 'numPr')
                el(np, 'ilvl', val=numbering[1])
                el(np, 'numId', val=numbering[0])
        return p

    def run(self, parent, text=None, bold=False, italic=False, link=False, br=False):
        run = el(parent, 'r')
        if bold or italic or link:
            rp = el(run, 'rPr')
            if link:
                el(rp, 'rStyle', val='Hyperlink')
            if bold:
                el(rp, 'b')
            if italic:
                el(rp, 'i')
        if br:
            el(run, 'br')
        if text:
            t = el(run, 't')
            t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
            t.text = re.sub(r'\s+', ' ', text)

    def inline(self, children, parent, bold=False, italic=False, link=False):
        for child in children:
            if isinstance(child, str):
                self.run(parent, child, bold, italic, link)
                continue
            if child.tag in {'script', 'style', 'header', 'footer', 'nav'}:
                continue
            if child.tag == 'br':
                self.run(parent, br=True)
            elif child.tag == 'span' and 'line' in child.attrs.get('class', '').split():
                self.run(parent, br=True)
                self.run(parent, '________________________________________')
                self.run(parent, br=True)
            elif child.tag == 'a' and child.attrs.get('href'):
                target = urljoin(BASE + self.source + '.html', child.attrs['href'])
                if urlparse(target).scheme not in {'https', 'http', 'mailto', 'tel'}:
                    raise ValueError('Unsupported hyperlink scheme: ' + target)
                rid = 'link' + str(len(self.rels))
                E.SubElement(self.rels, 'Relationship', Id=rid, Type=R + '/hyperlink', Target=target, TargetMode='External')
                hp = el(parent, 'hyperlink')
                hp.set('{%s}id' % R, rid)
                self.inline(child.children, hp, bold, italic, True)
            elif child.tag not in {'ul', 'ol'}:
                self.inline(child.children, parent, bold or child.tag in {'strong', 'b', 'th'}, italic or child.tag in {'em', 'i'}, link)

    def blocks(self, children, parent):
        pending = []
        def flush():
            if any(isinstance(x, Node) or x.strip() for x in pending):
                self.inline(pending, self.paragraph(parent))
            pending.clear()
        for node in children:
            if isinstance(node, str):
                pending.append(node)
                continue
            if node.tag in {'script', 'style', 'header', 'footer', 'nav'}:
                continue
            if node.tag not in BLOCK:
                pending.append(node)
                continue
            flush()
            if node.tag in {'h1', 'h2', 'h3', 'h4', 'p', 'pre', 'blockquote'}:
                style = {'h1': 'Title', 'h2': 'Heading1', 'h3': 'Heading2', 'h4': 'Heading3'}.get(node.tag)
                self.inline(node.children, self.paragraph(parent, style))
            elif node.tag in {'ul', 'ol'}:
                self.list(node, parent)
            elif node.tag == 'table':
                self.table(node, parent)
            elif 'draft-banner' in node.attrs.get('class', '').split():
                self.inline(node.children, self.paragraph(parent, 'DraftNotice'))
            else:
                self.blocks(node.children, parent)
        flush()

    def list(self, node, parent, depth=0):
        self.num_count += 1
        numid = self.num_count
        num = el(self.numbering, 'num', numId=numid)
        el(num, 'abstractNumId', val=1 if node.tag == 'ol' else 0)
        for item in node.children:
            if not isinstance(item, Node) or item.tag != 'li':
                continue
            self.inline(item.children, self.paragraph(parent, numbering=(numid, min(depth, 8))))
            for child in item.children:
                if isinstance(child, Node) and child.tag in {'ul', 'ol'}:
                    self.list(child, parent, depth + 1)

    def table(self, node, parent):
        table = el(parent, 'tbl')
        tp = el(table, 'tblPr')
        el(tp, 'tblW', w=10080, type='dxa')
        borders = el(tp, 'tblBorders')
        for edge in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
            el(borders, edge, val='single', sz=4, color='B5C4C0')
        rows = list(descendants(node, 'tr'))
        columns = max((sum(isinstance(c, Node) and c.tag in {'td', 'th'} for c in row.children) for row in rows), default=1)
        grid = el(table, 'tblGrid')
        for _ in range(columns):
            el(grid, 'gridCol', w=10080 // columns)
        for row in rows:
            tr = el(table, 'tr')
            for cell in row.children:
                if not isinstance(cell, Node) or cell.tag not in {'td', 'th'}:
                    continue
                tc = el(tr, 'tc')
                cp = el(tc, 'tcPr')
                el(cp, 'tcW', w=10080 // columns, type='dxa')
                if cell.tag == 'th':
                    el(cp, 'shd', fill='E5EFEB')
                if any(isinstance(c, Node) and c.tag in BLOCK for c in cell.children):
                    self.blocks(cell.children, tc)
                else:
                    self.inline(cell.children, self.paragraph(tc), bold=cell.tag == 'th')
                if tc[-1].tag != '{%s}p' % W:
                    self.paragraph(tc)

    def add(self, source, main, page_break=False):
        self.source = source
        if page_break:
            el(el(self.paragraph(self.body), 'r'), 'br', type='page')
        self.blocks(main.children, self.body)

    def save(self, path):
        sect = el(self.body, 'sectPr')
        el(sect, 'pgSz', w=12240, h=15840)
        el(sect, 'pgMar', top=1080, right=1080, bottom=1080, left=1080, header=360, footer=360, gutter=0)
        types = E.Element('Types', xmlns=CT)
        E.SubElement(types, 'Default', Extension='rels', ContentType='application/vnd.openxmlformats-package.relationships+xml')
        E.SubElement(types, 'Default', Extension='xml', ContentType='application/xml')
        for part, kind in [('document', 'document.main'), ('styles', 'styles'), ('numbering', 'numbering')]:
            E.SubElement(types, 'Override', PartName='/word/' + part + '.xml', ContentType='application/vnd.openxmlformats-officedocument.wordprocessingml.' + kind + '+xml')
        package = E.Element('Relationships', xmlns=REL)
        E.SubElement(package, 'Relationship', Id='document', Type=R + '/officeDocument', Target='word/document.xml')
        with ZipFile(path, 'w', ZIP_DEFLATED) as output:
            for name, root in [('[Content_Types].xml', types), ('_rels/.rels', package), ('word/document.xml', self.root), ('word/_rels/document.xml.rels', self.rels), ('word/styles.xml', styles()), ('word/numbering.xml', self.numbering)]:
                output.writestr(name, xml(root))


def styles():
    root = E.Element('{%s}styles' % W)
    defaults = el(root, 'docDefaults')
    rp = el(el(defaults, 'rPrDefault'), 'rPr')
    el(rp, 'rFonts', ascii='Arial', hAnsi='Arial', eastAsia='Arial', cs='Arial')
    el(rp, 'sz', val=21)
    pp = el(el(defaults, 'pPrDefault'), 'pPr')
    el(pp, 'spacing', after=120, line=276, lineRule='auto')
    for name, size in [('Normal', 21), ('Title', 40), ('Heading1', 28), ('Heading2', 23), ('Heading3', 22), ('DraftNotice', 21)]:
        st = el(root, 'style', type='paragraph', styleId=name)
        if name == 'Normal':
            st.set('{%s}default' % W, '1')
        el(st, 'name', val=name)
        if name != 'Normal':
            el(st, 'basedOn', val='Normal')
        p = el(st, 'pPr')
        if name.startswith('Heading') or name == 'Title':
            el(p, 'keepNext')
            el(p, 'spacing', before=240, after=120)
            if name.startswith('Heading'):
                el(p, 'outlineLvl', val=int(name[-1]) - 1)
        if name == 'DraftNotice':
            el(p, 'shd', fill='FFF2CC')
        r = el(st, 'rPr')
        if name != 'Normal':
            el(r, 'b')
        el(r, 'sz', val=size)
    st = el(root, 'style', type='character', styleId='Hyperlink')
    el(st, 'name', val='Hyperlink')
    r = el(st, 'rPr')
    el(r, 'color', val='0563C1')
    el(r, 'u', val='single')
    return root


def main():
    parser_args = argparse.ArgumentParser(description=__doc__)
    repo = Path(__file__).resolve().parents[1]
    parser_args.add_argument('--source-directory', type=Path, default=repo / 'docs')
    parser_args.add_argument('--output-directory', type=Path, default=repo / 'exports' / 'docx')
    parser_args.add_argument('--evidence', type=Path)
    options = parser_args.parse_args()
    sources, hashes = [], {}
    for page, title in PAGES:
        source = options.source_directory / (page + '.html')
        data = source.read_bytes()
        parser = Parser()
        parser.feed(data.decode('utf-8-sig'))
        mains = list(descendants(parser.root, 'main'))
        if len(mains) != 1:
            raise ValueError(str(source) + ': expected exactly one main element')
        sources.append((page, title, mains[0]))
        hashes[source.name] = hashlib.sha256(data).hexdigest()
    jobs = [(source[1], [source]) for source in sources]
    jobs.extend([('Legal-Documentation-Packet', sources[:9]), ('Operational-Governance-Packet', sources[9:])])
    results = []
    with tempfile.TemporaryDirectory(prefix='brainybee-docx-') as temporary:
        staging = Path(temporary)
        for title, contents in jobs:
            document = Document()
            for i, (page, _, main_node) in enumerate(contents):
                document.add(page, main_node, i > 0)
            name = 'Brainy-Bee-Schools-' + title + '.docx'
            document.save(staging / name)
            data = (staging / name).read_bytes()
            results.append({'file': name, 'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data), 'sources': [s[0] for s in contents], 'paragraphs': len(list(document.root.iter('{%s}p' % W))), 'tables': len(list(document.root.iter('{%s}tbl' % W)))})
        options.output_directory.mkdir(parents=True, exist_ok=True)
        for item in results:
            target = options.output_directory / item['file']
            pending = target.with_suffix('.docx.tmp')
            pending.write_bytes((staging / item['file']).read_bytes())
            pending.replace(target)
    if options.evidence:
        options.evidence.parent.mkdir(parents=True, exist_ok=True)
        options.evidence.write_text(json.dumps({'generator': 'Python standard-library OOXML', 'created_utc': datetime.now(timezone.utc).isoformat(), 'source_sha256': hashes, 'outputs': results}, indent=2) + '\n', encoding='utf-8')
    print('Generated 15 individual Word documents and two combined packets in ' + str(options.output_directory.resolve()))


if __name__ == '__main__':
    main()
