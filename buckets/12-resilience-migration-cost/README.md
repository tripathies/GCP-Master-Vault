# 12. Resilience, Migration, Cost & Architecture Patterns

> GCP Master Vault learning tracker. This category uses GCP-native services, identity models, networking and governance terminology.

## Category architecture

![12. Resilience, Migration, Cost & Architecture Patterns architecture](architecture.svg)

- [Editable category diagram](architecture.drawio)
- [Mermaid source](architecture.mmd)
- [Visual architecture library](../../VISUAL-DIAGRAMS.md)
- [Enterprise reference architecture](../../GCP-ENTERPRISE-REFERENCE-ARCHITECTURE.md)

## Component checklist

| Topic | Learning guide | Diagram (SVG) | Editable diagram |
|---|---|---|---|
| Backup and DR Service | [Open guide](../../services/backup-and-dr-service.md) | [View](../../services/backup-and-dr-service/architecture.svg) | [draw.io](../../services/backup-and-dr-service/architecture.drawio) |
| Migrate to Virtual Machines | [Open guide](../../services/migrate-to-virtual-machines.md) | [View](../../services/migrate-to-virtual-machines/architecture.svg) | [draw.io](../../services/migrate-to-virtual-machines/architecture.drawio) |
| Database Migration Service | [Open guide](../../services/database-migration-service.md) | [View](../../services/database-migration-service/architecture.svg) | [draw.io](../../services/database-migration-service/architecture.drawio) |
| Cloud Billing Budgets | [Open guide](../../services/cloud-billing-budgets.md) | [View](../../services/cloud-billing-budgets/architecture.svg) | [draw.io](../../services/cloud-billing-budgets/architecture.drawio) |
| Billing Export to BigQuery | [Open guide](../../services/billing-export-to-bigquery.md) | [View](../../services/billing-export-to-bigquery/architecture.svg) | [draw.io](../../services/billing-export-to-bigquery/architecture.drawio) |
| FinOps and Cost Optimization | [Open guide](../../services/finops-and-cost-optimization.md) | [View](../../services/finops-and-cost-optimization/architecture.svg) | [draw.io](../../services/finops-and-cost-optimization/architecture.drawio) |
| High Availability and Disaster Recovery Patterns | [Open guide](../../services/high-availability-and-disaster-recovery-patterns.md) | [View](../../services/high-availability-and-disaster-recovery-patterns/architecture.svg) | [draw.io](../../services/high-availability-and-disaster-recovery-patterns/architecture.drawio) |

## Practice workflow
1. Read the official documentation and note service scope, limits and alternatives.
2. Map identity, network paths, data flows, dependencies and ownership.
3. Complete a sandbox lab and capture validation evidence.
4. Test an access-denied or failure scenario where safe.
5. Record monitoring, cost observations and teardown proof.

## Official references
- [GCP documentation](https://cloud.google.com/docs)
- [Architecture framework](https://cloud.google.com/architecture/framework)
- [Pricing](https://cloud.google.com/pricing/)

> Diagrams are conceptual learning resources, not production-certified designs. Verify service capabilities, IAM permissions, network behavior, quotas, regional availability and pricing before deployment.
