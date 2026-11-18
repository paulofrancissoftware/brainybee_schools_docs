# Brainy Bee Schools Documentation

Public legal, privacy, and school-procurement documentation for Brainy Bee Schools.

The Privacy Policy, COPPA Direct Notice, Data Retention and Deletion Policy, Security Overview, Subprocessor List, and Data Request Procedure are published operational documents effective August 15, 2026. The School Services Agreement, Data Privacy Addendum, and Parent/Guardian Notice remain review templates and are not ready for signature or distribution until the applicable legal and school review is complete.

## November 17 proposed update

This working tree contains **proposed revisions, not a newly adopted or published policy**. The changed Privacy Policy, COPPA Direct Notice, Retention Policy and Security Overview are proposed Version 1.1 drafts. The agreement, DPA and parent-notice templates are Draft 0.2. The current-product risk reassessment remains a draft; its August 2 historical risk scores and acceptance are not a fresh approval of the current release. Previously adopted Version 1.0 policies remain effective until a revision is approved and published with any required notice.

The revisions clarify authorized initial and recurring Clever roster processing, including records synchronized before first login or while apps are closed; saved partial Tests; educational practice plans, goals, progress and reward evidence; and device information. They do not authorize new data uses, change the retention schedule, replace district approval or establish FERPA/COPPA compliance. Clever certification is separate from school authorization and privacy review.

## Recommended publishing model

- Keep this repository public so schools and families can review the same current documents.
- Publish the `docs/` directory with GitHub Pages.
- Keep signed agreements, order forms, student data exports, support records, deletion evidence, completed incident records, and confidential evidence supporting security or provider reviews in private storage outside this repository.
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
| COPPA Direct Notice | Published Version 1.0; proposed revision is a draft | Record school receipt; binding educational-use authorization belongs in the agreement/DPA |
| School Services Agreement | Draft review template | Provider and authorized school/district representative sign only after review and completion of the Order Form |
| Data Privacy Addendum | Draft review template | Both parties sign or incorporate a district-approved equivalent into the agreement |
| Parent/Guardian Notice Template | Draft review template | School customizes and distributes it; not a universal parental-consent form |
| Data Retention and Deletion Policy | Yes | No |
| Security Overview | Yes | No |
| Subprocessor List | Yes | No |
| Data Request Procedure | Yes | No |
| Secure Export Delivery Procedure | Yes | No; operational approval required |
| Written Information Security Program | Yes | No; operational policy |
| Privacy and Security Risk Assessment | Yes | No; review at least annually |
| Incident Response Plan | Yes | No; operational plan |
| Subprocessor Assurance Register | Yes | No; preserve accepted terms privately |
| Quebec Cross-Border Privacy Impact Assessment | Yes | No; Quebec counsel review required |

The proposed local revisions identified above are not approved for publication merely because their earlier versions appear in the public-document list.

## School signature packet

1. Ask the district for its required vendor approval process, DPA or state addendum, and authorized contracting signatory. A teacher or technical contact may sign only with the institution's delegated authority.
2. Complete and review the **Services Agreement and its Order Form**: district legal identity, covered schools/classes, dates, licenses/seats, price including a zero-cost pilot if applicable, currency/payment terms, educational purpose, contacts and addenda. Do not assume that the draft's CAD default, Quebec/Longueuil venue, liability or indemnity terms are accepted by a US public district.
3. Attach the **DPA or district-approved equivalent** and preserve the exact policy and subprocessor versions with the privately signed packet. The existing templates have signature blocks; the final incorporation/signature method is for the district and counsel to approve.
4. Provide the **COPPA Direct Notice before relying on school authorization**, including authorization for initial roster processing before a student first signs in. Record informed school authorization and notice receipt; a Clever connection or certification alone is not the contract or authorization record.
5. Supply the privacy, retention, security, subprocessor and data-request documents. Customize the parent notice with the school and determine any additional parental notice/consent requirements with the district and counsel. The operator retains its own COPPA obligations.

FERPA does not universally require a separately signed DPA under the school-official exception, but state, district and procurement requirements may require written terms. This packet is a proposed contracting approach, not a representation that district or legal approval has occurred. Keep signed files and identifiable school information out of this public repository.

## Word documents

Run on macOS:

```bash
./scripts/build-docx.sh
```

Run on Windows with Python 3 installed, from this repository:

```powershell
& .\scripts\build-docx.ps1
```

The Windows exporter creates standard editable DOCX files locally without opening Word or requiring additional Python packages. Open the generated packet in Word or Pages to inspect its final layout before sending it.

Editable Word files are written to `exports/docx/`, including an assembled legal packet and an assembled operational-governance packet. The blank incident-register CSV remains in `templates/`; completed registers must be stored privately.

Generated files retain the source documents' draft notices and blanks. Generation does not make a packet ready for signature. Inspect the final Word layout and resolve the legal and school review checklist before sending a signature copy.

## GitHub Pages setup

The included Actions workflow deploys `docs/` to GitHub Pages.

1. Use the existing public `paulofrancissoftware/brainybee_schools_docs` repository.
2. Commit and push public policies only after confirming that they match current product and operational practices and approving the applicable effective date and notice process. A push to `main` runs the Pages deployment workflow; do not publish proposed revisions as adopted policies. Keep agreement and school-notice templates marked as drafts until their legal review is complete.
3. In GitHub, open **Settings > Pages** and choose **GitHub Actions** as the source.
4. Verify every page, then update the Schools app and store listings to the dedicated policy URL.

Do not put Firebase keys, Clever secrets, student data, signed agreements, completed incident registers, exports, privacy request evidence, or confidential security details in this repository.
