# Identity, Access & Governance

> Category learning tracker for GCP Master Vault. Service names and examples in this folder are GCP-specific.

## Category architecture

![Identity, Access & Governance architecture](architecture.svg)

- [Editable category diagram](architecture.drawio)
- [Mermaid source](architecture.mmd)
- [Full visual library](../../VISUAL-DIAGRAMS.md)
- [Master architecture](../../GCP-ENTERPRISE-REFERENCE-ARCHITECTURE.md)

## Component tracker

| Topic guide | SVG diagram | Editable draw.io |
|---|---|---|
| [Cloud IAM](../../services/cloud-iam.md) | [SVG](../../services/cloud-iam/architecture.svg) | [draw.io](../../services/cloud-iam/architecture.drawio) |
| [Service Accounts](../../services/service-accounts.md) | [SVG](../../services/service-accounts/architecture.svg) | [draw.io](../../services/service-accounts/architecture.drawio) |
| [Workload Identity Federation](../../services/workload-identity-federation.md) | [SVG](../../services/workload-identity-federation/architecture.svg) | [draw.io](../../services/workload-identity-federation/architecture.drawio) |
| [IAM Conditions](../../services/iam-conditions.md) | [SVG](../../services/iam-conditions/architecture.svg) | [draw.io](../../services/iam-conditions/architecture.drawio) |
| [Organization Policy Service](../../services/organization-policy-service.md) | [SVG](../../services/organization-policy-service/architecture.svg) | [draw.io](../../services/organization-policy-service/architecture.drawio) |
| [Policy Analyzer](../../services/policy-analyzer.md) | [SVG](../../services/policy-analyzer/architecture.svg) | [draw.io](../../services/policy-analyzer/architecture.drawio) |

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
