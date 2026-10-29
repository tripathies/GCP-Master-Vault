# DevOps, IaC & Operations

> Category learning tracker for GCP Master Vault. Service names and examples in this folder are GCP-specific.

## Category architecture

![DevOps, IaC & Operations architecture](architecture.svg)

- [Editable category diagram](architecture.drawio)
- [Mermaid source](architecture.mmd)
- [Full visual library](../../VISUAL-DIAGRAMS.md)
- [Master architecture](../../GCP-ENTERPRISE-REFERENCE-ARCHITECTURE.md)

## Component tracker

| Topic guide | SVG diagram | Editable draw.io |
|---|---|---|
| [Cloud Build](../../services/cloud-build.md) | [SVG](../../services/cloud-build/architecture.svg) | [draw.io](../../services/cloud-build/architecture.drawio) |
| [Cloud Deploy](../../services/cloud-deploy.md) | [SVG](../../services/cloud-deploy/architecture.svg) | [draw.io](../../services/cloud-deploy/architecture.drawio) |
| [Terraform on Google Cloud](../../services/terraform-on-google-cloud.md) | [SVG](../../services/terraform-on-google-cloud/architecture.svg) | [draw.io](../../services/terraform-on-google-cloud/architecture.drawio) |
| [Infrastructure Manager](../../services/infrastructure-manager.md) | [SVG](../../services/infrastructure-manager/architecture.svg) | [draw.io](../../services/infrastructure-manager/architecture.drawio) |
| [Config Controller](../../services/config-controller.md) | [SVG](../../services/config-controller/architecture.svg) | [draw.io](../../services/config-controller/architecture.drawio) |
| [Cloud Scheduler](../../services/cloud-scheduler.md) | [SVG](../../services/cloud-scheduler/architecture.svg) | [draw.io](../../services/cloud-scheduler/architecture.drawio) |
| [Cloud Monitoring](../../services/cloud-monitoring.md) | [SVG](../../services/cloud-monitoring/architecture.svg) | [draw.io](../../services/cloud-monitoring/architecture.drawio) |
| [Cloud Logging](../../services/cloud-logging.md) | [SVG](../../services/cloud-logging/architecture.svg) | [draw.io](../../services/cloud-logging/architecture.drawio) |
| [Cloud Trace and Profiler](../../services/cloud-trace-and-profiler.md) | [SVG](../../services/cloud-trace-and-profiler/architecture.svg) | [draw.io](../../services/cloud-trace-and-profiler/architecture.drawio) |

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
