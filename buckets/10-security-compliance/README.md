# Security, Threat Detection & Compliance

> Category learning tracker for GCP Master Vault. Service names and examples in this folder are GCP-specific.

## Category architecture

![Security, Threat Detection & Compliance architecture](architecture.svg)

- [Editable category diagram](architecture.drawio)
- [Mermaid source](architecture.mmd)
- [Full visual library](../../VISUAL-DIAGRAMS.md)
- [Master architecture](../../GCP-ENTERPRISE-REFERENCE-ARCHITECTURE.md)

## Component tracker

| Topic guide | SVG diagram | Editable draw.io |
|---|---|---|
| [Cloud KMS](../../services/cloud-kms.md) | [SVG](../../services/cloud-kms/architecture.svg) | [draw.io](../../services/cloud-kms/architecture.drawio) |
| [Secret Manager](../../services/secret-manager.md) | [SVG](../../services/secret-manager/architecture.svg) | [draw.io](../../services/secret-manager/architecture.drawio) |
| [Cloud Armor](../../services/cloud-armor.md) | [SVG](../../services/cloud-armor/architecture.svg) | [draw.io](../../services/cloud-armor/architecture.drawio) |
| [Security Command Center](../../services/security-command-center.md) | [SVG](../../services/security-command-center/architecture.svg) | [draw.io](../../services/security-command-center/architecture.drawio) |
| [Cloud Audit Logs](../../services/cloud-audit-logs.md) | [SVG](../../services/cloud-audit-logs/architecture.svg) | [draw.io](../../services/cloud-audit-logs/architecture.drawio) |
| [Cloud IDS](../../services/cloud-ids.md) | [SVG](../../services/cloud-ids/architecture.svg) | [draw.io](../../services/cloud-ids/architecture.drawio) |
| [Sensitive Data Protection](../../services/sensitive-data-protection.md) | [SVG](../../services/sensitive-data-protection/architecture.svg) | [draw.io](../../services/sensitive-data-protection/architecture.drawio) |
| [Certificate Authority Service](../../services/certificate-authority-service.md) | [SVG](../../services/certificate-authority-service/architecture.svg) | [draw.io](../../services/certificate-authority-service/architecture.drawio) |

## Practice workflow
1. Read the official documentation for each selected service.
2. Map its account/project boundary, identity, network and data flows.
3. Complete a sandbox lab and capture validation evidence.
4. Test one denied-access or failure scenario.
5. Record cost, teardown proof and design trade-offs.

## Official references
- [Google Cloud documentation](https://cloud.google.com/docs)
- [Google Cloud Architecture Framework](https://cloud.google.com/architecture/framework)
- [Google Cloud pricing](https://cloud.google.com/pricing)

> Diagram files are conceptual learning resources, not production-certified designs. Validate current service capabilities, permissions, routing, quotas, regional availability and prices before deployment.
