# Publication Readiness Checklist

All items below must be resolved before removing the draft banners or publishing these documents as final.

## Business identity

- [x] Identify Chi Cheung Lau as the legal operator contracting with schools.
- [x] Add the monitored mailing address: 1940 Rue Cloutier, Brossard, Quebec J4Z 0S4, Canada.
- [x] Add the monitored privacy telephone number: +1 514-451-0030.
- [ ] Confirm `paulofrancis.software@gmail.com` is the public privacy email or replace it with a domain mailbox.
- [x] Identify Chi Cheung Lau, Owner and Privacy Officer, as the person responsible for privacy. No delegation is needed while the owner personally performs this role.
- [x] Use the laws of the Province of Quebec and applicable federal laws of Canada, with the Judicial District of Longueuil as the proposed venue, subject to School-specific requirements.

## Product and data handling

- [ ] Confirm production Schools builds expose only Clever SSO and do not expose Demo School or email/password test accounts.
- [ ] Confirm school administrators, not individual teachers, execute school authorization and contracting documents.
- [x] Implement and emulator-test manual organization, class, and student export/deletion procedures with dry-run inventory, guarded execution, verification, and deletion receipts.
- [x] Run a read-only production inventory for the pilot organization and reconcile the tool with the current Firebase schema.
- [x] Implement, document, and emulator-test correction and reversible stop-collection procedures; deploy the Firestore access gate and Clever hold check.
- [x] Document recipient verification, data minimization, approved-channel controls, confirmation, and temporary-copy removal for sensitive exports.
- [ ] Select the pilot School's authenticated transfer portal and complete a synthetic end-to-end delivery test, including access revocation and cleanup evidence.
- [ ] Approve the proposed 30-day export window, 60-day production deletion target, 90-day backup expiration target, and 12-month security-log limit.
- [ ] Configure or document Firebase retention and Cloud Logging settings to match the published schedule.
- [ ] Confirm Clever OAuth state records expire after five minutes and are deleted after redemption.
- [x] Test school offboarding on seeded Auth and Firestore emulator data and confirm the deletion receipt does not reproduce Student Data.
- [ ] Confirm Android and Apple backup behavior and decide whether school app data should be excluded from device cloud backups.

## Privacy and security blockers found in the current app

- [x] Rotate and revoke the Firebase Admin service-account key previously tracked in the Schools source repository.
- [x] Remove that key from the current Git history and add service-account key patterns to `.gitignore`.
- [x] Self-host the Inter and Roboto fonts in the iOS and Android apps.
- [x] Remove the assignment QR feature and its `api.qrserver.com` request from the Schools apps.
- [ ] Create the written information security program required by the amended COPPA Rule, designate its coordinator, and perform the initial risk assessment.
- [ ] Create a written incident-response plan and a privacy-incident register.
- [ ] Obtain and retain appropriate written privacy/security assurances from Firebase/Google, Clever, and any remaining subprocessor.
- [ ] Complete a Quebec privacy impact assessment before communicating personal information outside Quebec and retain the required written agreements where applicable.

## App and store alignment

- [ ] Add a clear and prominent Privacy link on the app Home/landing screen or obtain counsel's approval for the final placement. The FTC FAQ says a child-directed app's privacy link must be on its Home screen.
- [ ] Change both Schools app links from the consumer `brainybee_docs` URL to the dedicated Schools Privacy Policy URL.
- [ ] Review the in-app Terms. Remove language suggesting the school is responsible for the operator's COPPA compliance.
- [ ] Use separate iOS privacy manifests for Consumer and Schools, or remove Schools declarations that do not apply, including Purchase History if it is not collected.
- [ ] Re-audit final iOS and Android binaries for SDKs, network domains, permissions, and collected fields.
- [ ] Make App Store Connect and Google Play disclosures match the final Schools binary and these documents.

## Legal review and school procurement

- [ ] Have qualified US children's privacy and student privacy counsel review COPPA, FERPA, PPRA, and state student privacy terms.
- [ ] Have qualified Quebec/Canadian privacy counsel review Quebec Law 25, cross-border processing, and the contracting entity.
- [ ] Prepare French versions of the agreement and related documents before contracting with Quebec schools, and obtain advice about Quebec French-language requirements for contracts of adhesion.
- [ ] Prepare state-specific addenda when a school or district requires them.
- [ ] Confirm insurance coverage and have counsel approve the proposed general cap, enhanced privacy/security cap, indemnity, governing law, venue, and public-school procurement language.
- [ ] Decide how material policy changes will be communicated to schools and families.
- [ ] Record the final effective date, policy version, release tag, and Git commit in each signed school file.
- [ ] Remove every `DRAFT` banner, placeholder marker, and `noindex,nofollow` robots directive only after final approval.
- [ ] Regenerate all Word exports after the final web-document edits and inspect the final packet in Microsoft Word or Apple Pages.
