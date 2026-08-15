# Legal and Contract Readiness Checklist

The public operational policies were adopted as Version 1.0 on August 15, 2026 after the documented product and operational review. The remaining items must be resolved before treating the school agreement, DPA, parent notice, or jurisdiction-specific materials as final. Counsel may also recommend revisions to the published policies; material changes must receive a new effective date and school notice when required.

## Business identity

- [x] Identify Chi Cheung Lau as the legal operator contracting with schools.
- [x] Add the monitored mailing address: 1940 Rue Cloutier, Brossard, Quebec J4Z 0S4, Canada.
- [x] Add the monitored privacy telephone number: +1 514-451-0030.
- [x] Use `paulofrancis.software@gmail.com` as the monitored public privacy email for the pilot; reconsider a domain mailbox before broader launch.
- [x] Identify Chi Cheung Lau, Owner and Privacy Officer, as the person responsible for privacy. No delegation is needed while the owner personally performs this role.
- [x] Use the laws of the Province of Quebec and applicable federal laws of Canada, with the Judicial District of Longueuil as the proposed venue, subject to School-specific requirements.

## Product and data handling

- [x] Confirm production Schools builds expose only Clever SSO and do not expose email/password test accounts. The optional Demo School button starts Clever's demo-district sign-in and is controlled by the production `cleverDemoSignInEnabled` flag.
- [x] Require an authorized school or district representative, not an individual student, to execute school authorization and contracting documents. A teacher may sign only when the institution has granted that authority.
- [x] Implement and emulator-test manual organization, class, and student export/deletion procedures with dry-run inventory, guarded execution, verification, and deletion receipts.
- [x] Run a read-only production inventory for the pilot organization and reconcile the tool with the current Firebase schema.
- [x] Implement, document, and emulator-test correction and reversible stop-collection procedures; deploy the Firestore access gate and Clever hold check.
- [x] Document recipient verification, data minimization, approved-channel controls, confirmation, and temporary-copy removal for sensitive exports.
- [ ] Select the pilot School's authenticated transfer portal and complete a synthetic end-to-end delivery test, including access revocation and cleanup evidence.
- [x] Adopt the 30-day export window, 60-day production deletion target, seven-day Firestore recovery-version expiry, 30-day ordinary-log retention, and 400-day Google-required audit-log retention.
- [x] Configure and document Firestore point-in-time recovery, database deletion protection, and Cloud Logging retention to match the published schedule.
- [x] Complete a non-personal synthetic Firestore point-in-time recovery test and verify that the deleted current record remained absent.
- [x] Confirm Clever OAuth state expires after five minutes, is deleted after redemption, and is removed by an authenticated scheduled cleanup every 15 minutes.
- [x] Test school offboarding on seeded Auth and Firestore emulator data and confirm the deletion receipt does not reproduce Student Data.
- [x] Exclude Schools app-managed data from Android backup/device transfer and Apple cloud backup.

## Privacy and security blockers found in the current app

- [x] Rotate and revoke the Firebase Admin service-account key previously tracked in the Schools source repository.
- [x] Remove that key from the current Git history and add service-account key patterns to `.gitignore`.
- [x] Self-host the Inter and Roboto fonts in the iOS and Android apps.
- [x] Remove the assignment QR feature and its `api.qrserver.com` request from the Schools apps.
- [x] Create the written information security program, designate Chi Cheung Lau as coordinator, and complete the initial risk assessment.
- [x] Create a written incident-response plan and a blank privacy-incident register template; completed records remain private.
- [x] Record the Google and Clever written privacy/security terms and review materials in the Subprocessor Assurance Register; counsel must confirm their legal sufficiency.
- [x] Complete an initial Quebec cross-border privacy impact assessment; Quebec counsel must validate the conclusion and written-agreement requirements.

## App and store alignment

- [ ] Obtain counsel's approval for the final Privacy-link placement. The current student and teacher placement is Preferences, which remains available to students even when all optional preferences are disabled.
- [x] Change both Schools app links from the consumer `brainybee_docs` URL to the dedicated Schools Privacy Policy URL.
- [x] Route any in-app Terms action to the dedicated School Services Agreement and remove obsolete credential and one-sided COPPA-responsibility wording from the dormant fallback text.
- [x] Remove inapplicable Schools privacy-manifest declarations, including Photos/Videos and Purchase History.
- [x] Re-audit the version 2.49 iOS and Android binaries for SDKs, network domains, permissions, and collected fields. No advertising, analytics, tracking, Storage, camera, location, microphone, photo, or payment capability was found.
- [x] Prepare App Store Connect and Google Play disclosure answers that match the version 2.49 binaries and these documents in the app repository's `PRODUCTION-READINESS.md`.
- [ ] Enter and confirm those disclosures in App Store Connect and Google Play when uploading the final signed builds.

## Legal review and school procurement

- [ ] Have qualified US children's privacy and student privacy counsel review COPPA, FERPA, PPRA, and state student privacy terms.
- [ ] Have qualified Quebec/Canadian privacy counsel review Quebec Law 25, cross-border processing, and the contracting entity.
- [ ] Prepare French versions of the agreement and related documents before contracting with Quebec schools, and obtain advice about Quebec French-language requirements for contracts of adhesion.
- [ ] Prepare state-specific addenda when a school or district requires them.
- [ ] Confirm insurance coverage and have counsel approve the proposed general cap, enhanced privacy/security cap, indemnity, governing law, venue, and public-school procurement language.
- [x] Use direct email notice to each School contact plus a dated public policy update; obtain new authorization or consent before a change when law requires it.
- [ ] Record the final effective date, policy version, release tag, and Git commit in each signed school file.
- [x] Remove draft markers and `noindex,nofollow` from the six adopted public operational documents; preserve draft markers and placeholders on school and legal-review templates until final approval.
- [ ] Regenerate all Word exports after the final web-document edits and inspect the final packet in Microsoft Word or Apple Pages.
