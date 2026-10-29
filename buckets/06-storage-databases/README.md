# Storage, Databases & Caching

> Category learning tracker for GCP Master Vault. Service names and examples in this folder are GCP-specific.

## Category architecture

![Storage, Databases & Caching architecture](architecture.svg)

- [Editable category diagram](architecture.drawio)
- [Mermaid source](architecture.mmd)
- [Full visual library](../../VISUAL-DIAGRAMS.md)
- [Master architecture](../../GCP-ENTERPRISE-REFERENCE-ARCHITECTURE.md)

## Component tracker

| Topic guide | SVG diagram | Editable draw.io |
|---|---|---|
| [Cloud Storage](../../services/cloud-storage.md) | [SVG](../../services/cloud-storage/architecture.svg) | [draw.io](../../services/cloud-storage/architecture.drawio) |
| [Persistent Disk](../../services/persistent-disk.md) | [SVG](../../services/persistent-disk/architecture.svg) | [draw.io](../../services/persistent-disk/architecture.drawio) |
| [Filestore](../../services/filestore.md) | [SVG](../../services/filestore/architecture.svg) | [draw.io](../../services/filestore/architecture.drawio) |
| [Cloud SQL](../../services/cloud-sql.md) | [SVG](../../services/cloud-sql/architecture.svg) | [draw.io](../../services/cloud-sql/architecture.drawio) |
| [AlloyDB for PostgreSQL](../../services/alloydb-for-postgresql.md) | [SVG](../../services/alloydb-for-postgresql/architecture.svg) | [draw.io](../../services/alloydb-for-postgresql/architecture.drawio) |
| [Cloud Spanner](../../services/cloud-spanner.md) | [SVG](../../services/cloud-spanner/architecture.svg) | [draw.io](../../services/cloud-spanner/architecture.drawio) |
| [Firestore](../../services/firestore.md) | [SVG](../../services/firestore/architecture.svg) | [draw.io](../../services/firestore/architecture.drawio) |
| [Bigtable](../../services/bigtable.md) | [SVG](../../services/bigtable/architecture.svg) | [draw.io](../../services/bigtable/architecture.drawio) |
| [Memorystore](../../services/memorystore.md) | [SVG](../../services/memorystore/architecture.svg) | [draw.io](../../services/memorystore/architecture.drawio) |

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
