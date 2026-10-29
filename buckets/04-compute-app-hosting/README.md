# 04. Compute & Application Hosting

> GCP Master Vault learning tracker. This category uses GCP-native services, identity models, networking and governance terminology.

## Category architecture

![04. Compute & Application Hosting architecture](architecture.svg)

- [Editable category diagram](architecture.drawio)
- [Mermaid source](architecture.mmd)
- [Visual architecture library](../../VISUAL-DIAGRAMS.md)
- [Enterprise reference architecture](../../GCP-ENTERPRISE-REFERENCE-ARCHITECTURE.md)

## Component checklist

| Topic | Learning guide | Diagram (SVG) | Editable diagram |
|---|---|---|---|
| Compute Engine | [Open guide](../../services/compute-engine.md) | [View](../../services/compute-engine/architecture.svg) | [draw.io](../../services/compute-engine/architecture.drawio) |
| Managed Instance Groups | [Open guide](../../services/managed-instance-groups.md) | [View](../../services/managed-instance-groups/architecture.svg) | [draw.io](../../services/managed-instance-groups/architecture.drawio) |
| Cloud Run | [Open guide](../../services/cloud-run.md) | [View](../../services/cloud-run/architecture.svg) | [draw.io](../../services/cloud-run/architecture.drawio) |
| App Engine | [Open guide](../../services/app-engine.md) | [View](../../services/app-engine/architecture.svg) | [draw.io](../../services/app-engine/architecture.drawio) |
| Google Kubernetes Engine (GKE) | [Open guide](../../services/gke.md) | [View](../../services/gke/architecture.svg) | [draw.io](../../services/gke/architecture.drawio) |
| Batch | [Open guide](../../services/batch.md) | [View](../../services/batch/architecture.svg) | [draw.io](../../services/batch/architecture.drawio) |

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
