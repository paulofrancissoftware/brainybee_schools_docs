# Brainy Bee Schools Documentation

Public legal, privacy, and school-procurement documentation for Brainy Bee Schools.

> DRAFT: The documents are working drafts, not legal advice or a compliance certification. Do not publish or sign them until every item in `DRAFT-CHECKLIST.md` is complete and qualified privacy counsel has reviewed the final text.

## Recommended publishing model

- Keep this repository public so schools and families can review the same current documents.
- Publish the `docs/` directory with GitHub Pages.
- Keep signed agreements, order forms, student data exports, support records, and deletion evidence in private storage outside this repository.
- Tag each published legal release, for example `legal-v1.0.0`, so the exact terms accepted by a school can be reconstructed later.
- Preserve a private copy of each signed agreement together with the applicable release tag or commit hash.

Expected public URL after GitHub Pages is enabled:

`https://paulofrancissoftware.github.io/brainybee_schools_docs/`

Expected Privacy Policy URL for the iOS and Android apps:

`https://paulofrancissoftware.github.io/brainybee_schools_docs/privacy-policy.html`

## Documents

| Document | Public | Signature needed |
| --- | --- | --- |
| Privacy Policy | Yes | No |
| COPPA Direct Notice | Yes | School acknowledgement recommended |
| School Services Agreement | Public template | Yes |
| Data Privacy Addendum | Public template | Yes |
| Parent/Guardian Notice Template | Yes | No; school distributes it |
| Data Retention and Deletion Policy | Yes | No |
| Security Overview | Yes | No |
| Subprocessor List | Yes | No |
| Data Request Procedure | Yes | No |
| Secure Export Delivery Procedure | Yes | No; operational approval required |

## Word documents

Run on macOS:

```bash
./scripts/build-docx.sh
```

Editable Word files are written to `exports/docx/`, including an assembled documentation packet. The secure export procedure is generated as a separate operational document and is not appended to the contract/legal packet.

## GitHub Pages setup

The included Actions workflow deploys `docs/` to GitHub Pages.

1. Use the existing public `paulofrancissoftware/brainybee_schools_docs` repository.
2. Commit and push publication-ready documents only after the draft checklist and legal review are complete.
3. In GitHub, open **Settings > Pages** and choose **GitHub Actions** as the source.
4. Verify every page, then update the Schools app and store listings to the dedicated policy URL.

Do not put Firebase keys, Clever secrets, student data, signed agreements, or privacy request evidence in this repository.
