# Brainy Bee Schools Documentation

Public legal, privacy, and school-procurement documentation for Brainy Bee Schools.

The Privacy Policy, COPPA Direct Notice, Data Retention and Deletion Policy, Security Overview, Subprocessor List, and Data Request Procedure are published operational documents effective August 15, 2026. The School Services Agreement, Data Privacy Addendum, and Parent/Guardian Notice remain review templates and are not ready for signature or distribution until the applicable legal and school review is complete.

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
| COPPA Direct Notice | Yes | School acknowledgement recommended |
| School Services Agreement | Public template | Yes |
| Data Privacy Addendum | Public template | Yes |
| Parent/Guardian Notice Template | Yes | No; school distributes it |
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

## Word documents

Run on macOS:

```bash
./scripts/build-docx.sh
```

Editable Word files are written to `exports/docx/`, including an assembled legal packet and an assembled operational-governance packet. The blank incident-register CSV remains in `templates/`; completed registers must be stored privately.

## GitHub Pages setup

The included Actions workflow deploys `docs/` to GitHub Pages.

1. Use the existing public `paulofrancissoftware/brainybee_schools_docs` repository.
2. Commit and push public policies only after confirming that they match current product and operational practices. Keep agreement and school-notice templates marked as drafts until their legal review is complete.
3. In GitHub, open **Settings > Pages** and choose **GitHub Actions** as the source.
4. Verify every page, then update the Schools app and store listings to the dedicated policy URL.

Do not put Firebase keys, Clever secrets, student data, signed agreements, completed incident registers, exports, privacy request evidence, or confidential security details in this repository.
