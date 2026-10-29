# 05. Containers & Kubernetes

> GCP Master Vault learning tracker. This category uses GCP-native services, identity models, networking and governance terminology.

## Category architecture

![05. Containers & Kubernetes architecture](architecture.svg)

- [Editable category diagram](architecture.drawio)
- [Mermaid source](architecture.mmd)
- [Visual architecture library](../../VISUAL-DIAGRAMS.md)
- [Enterprise reference architecture](../../GCP-ENTERPRISE-REFERENCE-ARCHITECTURE.md)

## Component checklist

| Topic | Learning guide | Diagram (SVG) | Editable diagram |
|---|---|---|---|
| GKE Standard | [Open guide](../../services/gke-standard.md) | [View](../../services/gke-standard/architecture.svg) | [draw.io](../../services/gke-standard/architecture.drawio) |
| GKE Autopilot | [Open guide](../../services/gke-autopilot.md) | [View](../../services/gke-autopilot/architecture.svg) | [draw.io](../../services/gke-autopilot/architecture.drawio) |
| Artifact Registry | [Open guide](../../services/artifact-registry.md) | [View](../../services/artifact-registry/architecture.svg) | [draw.io](../../services/artifact-registry/architecture.drawio) |
| GKE Workload Identity Federation | [Open guide](../../services/gke-workload-identity-federation.md) | [View](../../services/gke-workload-identity-federation/architecture.svg) | [draw.io](../../services/gke-workload-identity-federation/architecture.drawio) |
| GKE Autoscaling | [Open guide](../../services/gke-autoscaling.md) | [View](../../services/gke-autoscaling/architecture.svg) | [draw.io](../../services/gke-autoscaling/architecture.drawio) |
| Cloud Service Mesh | [Open guide](../../services/cloud-service-mesh.md) | [View](../../services/cloud-service-mesh/architecture.svg) | [draw.io](../../services/cloud-service-mesh/architecture.drawio) |

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
