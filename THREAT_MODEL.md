# Threat Model

## Assets
- Dataset Integrity (CSV/JSON files)
- Provenance Metadata
- CI/CD Secrets (GitHub Tokens)

## Threats
1. **Data Tampering:** Unauthorized modification of survey results.
2. **Metadata Corruption:** Loss of traceability.
3. **Impersonation:** Commits made by unauthorized users appearing as the author.

## Mitigations
- Use of cryptographic checksums and manifests.
- Branch protection rules on GitHub.
- Signed commits and releases.
- Regular security audits of dependencies.
