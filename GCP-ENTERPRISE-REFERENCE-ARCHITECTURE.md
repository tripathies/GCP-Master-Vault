# Google Cloud Enterprise Reference Architecture

## Purpose
A conceptual reference for learning how a governed Google Cloud estate can be organized. Adapt it to business, regulatory, availability, residency and threat-model requirements.

## Core layers
1. **Resource hierarchy:** Organization → folders → projects → resources, with billing, quotas, labels and environment boundaries.
2. **Identity and governance:** Cloud IAM, service accounts, workload identity federation, Organization Policy and audit logs.
3. **Network foundation:** VPC, subnets, routes, firewall policies, Cloud NAT, DNS, private access, VPN/Interconnect and Shared VPC where appropriate.
4. **Ingress and edge:** Cloud Load Balancing, Cloud Armor, managed certificates and API management where needed.
5. **Compute/runtime:** Compute Engine, managed instance groups, Cloud Run, GKE or App Engine selected to match workload requirements.
6. **Data and messaging:** Cloud Storage, Cloud SQL, Spanner, Firestore, Bigtable and Pub/Sub chosen by access patterns and consistency needs.
7. **Data/AI:** BigQuery, Dataflow, Dataplex and Vertex AI where justified.
8. **Delivery and operations:** Terraform or approved infrastructure tooling, Cloud Build/Deploy, Cloud Logging and Cloud Monitoring.
9. **Security and recovery:** Cloud KMS, Secret Manager, Security Command Center, backups and tested recovery plans.

## Architecture decisions
- Use projects as administrative, quota, billing and policy boundaries.
- Document network reachability, ingress/egress and DNS assumptions.
- Compare managed runtime choices against required control, portability, latency and compliance.
- Choose data stores based on consistency, transactions, scale, latency, backup and recovery.
- Define SLO, RTO, RPO and test zonal/regional failure assumptions.
- Model steady-state and peak costs; assign workload owners.

## Production-readiness checklist
- [ ] Threat model and data classification completed.
- [ ] Least-privilege IAM reviewed; no long-lived credentials committed.
- [ ] Network flows and ingress/egress documented.
- [ ] SLOs, dashboards, actionable alerts and runbooks defined.
- [ ] Backup/restore and DR tested against RTO/RPO.
- [ ] Quota, load, dependency failure and rollback tested.
- [ ] Cost model, budgets, ownership labels and cleanup process set.

## Official references
- [Google Cloud Architecture Framework](https://cloud.google.com/architecture/framework)
- [Resource hierarchy](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy)
- [Cloud IAM](https://cloud.google.com/iam/docs/overview)
