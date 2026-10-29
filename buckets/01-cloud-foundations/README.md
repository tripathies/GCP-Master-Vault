# Cloud Foundations & Resource Hierarchy

> Category learning tracker for GCP Master Vault. Service names and examples in this folder are GCP-specific.

## Category architecture

![Cloud Foundations & Resource Hierarchy architecture](architecture.svg)

- [Editable category diagram](architecture.drawio)
- [Mermaid source](architecture.mmd)
- [Full visual library](../../VISUAL-DIAGRAMS.md)
- [Master architecture](../../GCP-ENTERPRISE-REFERENCE-ARCHITECTURE.md)

## Component tracker

| Topic guide | SVG diagram | Editable draw.io |
|---|---|---|
| [Resource Manager](../../services/resource-manager.md) | [SVG](../../services/resource-manager/architecture.svg) | [draw.io](../../services/resource-manager/architecture.drawio) |
| [Organizations and Folders](../../services/organizations-and-folders.md) | [SVG](../../services/organizations-and-folders/architecture.svg) | [draw.io](../../services/organizations-and-folders/architecture.drawio) |
| [Projects](../../services/projects.md) | [SVG](../../services/projects/architecture.svg) | [draw.io](../../services/projects/architecture.drawio) |
| [Cloud Billing](../../services/cloud-billing.md) | [SVG](../../services/cloud-billing/architecture.svg) | [draw.io](../../services/cloud-billing/architecture.drawio) |
| [Quotas and Locations](../../services/quotas-and-locations.md) | [SVG](../../services/quotas-and-locations/architecture.svg) | [draw.io](../../services/quotas-and-locations/architecture.drawio) |
| [Google Cloud Architecture Framework](../../services/google-cloud-architecture-framework.md) | [SVG](../../services/google-cloud-architecture-framework/architecture.svg) | [draw.io](../../services/google-cloud-architecture-framework/architecture.drawio) |

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
