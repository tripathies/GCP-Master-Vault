# GCP Master Vault ☁️
### Google Cloud Architecture • Services • Hands-on Labs • Enterprise Design

A structured learning tracker and reference repository for progressing from foundational services to enterprise architecture. Work through the categories, read service pages, complete labs in a sandbox and capture your own validation evidence.

> **Status:** Initial learning vault scaffold. Service guides and architecture diagrams are conceptual learning resources, not individually production-validated runbooks. Verify current product capabilities, IAM roles, quotas, regional availability, Terraform syntax and pricing against official Google Cloud docs before implementation.

## Quick navigation
- [Enterprise reference architecture](GCP-ENTERPRISE-REFERENCE-ARCHITECTURE.md)
- [Architecture diagram (SVG)](architecture.svg) · [Editable draw.io](architecture.drawio) · [Architecture notes](ARCHITECTURE.md)
- [Portfolio projects](PORTFOLIO-PROJECTS.md) · [Learning roadmap](LEARNING-ROADMAP.md) · [Cost and cleanup](COST-AND-CLEANUP.md)
- [Official sources](SOURCES.md) · [Machine-readable catalog](catalog.json)

## Learning progress

**Suggested path:** Foundations → Identity → Networking → Compute → Storage/Data → Security → DevOps/Operations → Resilience and FinOps.

<details>
<summary><strong>01. Cloud Foundations & Resource Hierarchy</strong></summary>

[Open category learning guide](buckets/01-cloud-foundations/README.md)

- [ ] [Resource Manager](services/resource-manager.md)
- [ ] [Organizations and Folders](services/organizations-and-folders.md)
- [ ] [Projects](services/projects.md)
- [ ] [Cloud Billing](services/cloud-billing.md)
- [ ] [Quotas and Locations](services/quotas-and-locations.md)
- [ ] [Google Cloud Architecture Framework](services/google-cloud-architecture-framework.md)

</details>

<details>
<summary><strong>02. Identity, Access & Governance</strong></summary>

[Open category learning guide](buckets/02-identity-governance/README.md)

- [ ] [Cloud IAM](services/cloud-iam.md)
- [ ] [Service Accounts](services/service-accounts.md)
- [ ] [Workload Identity Federation](services/workload-identity-federation.md)
- [ ] [IAM Conditions](services/iam-conditions.md)
- [ ] [Organization Policy Service](services/organization-policy-service.md)
- [ ] [Policy Analyzer](services/policy-analyzer.md)

</details>

<details>
<summary><strong>03. Networking & Connectivity</strong></summary>

[Open category learning guide](buckets/03-networking/README.md)

- [ ] [VPC Networks](services/vpc-networks.md)
- [ ] [Subnets and Routes](services/subnets-and-routes.md)
- [ ] [Firewall Rules and Policies](services/firewall-rules-and-policies.md)
- [ ] [Cloud NAT](services/cloud-nat.md)
- [ ] [Private Google Access](services/private-google-access.md)
- [ ] [Private Service Connect](services/private-service-connect.md)
- [ ] [Cloud VPN](services/cloud-vpn.md)
- [ ] [Cloud Interconnect](services/cloud-interconnect.md)
- [ ] [Cloud DNS](services/cloud-dns.md)
- [ ] [Cloud Load Balancing](services/cloud-load-balancing.md)

</details>

<details>
<summary><strong>04. Compute & Application Hosting</strong></summary>

[Open category learning guide](buckets/04-compute-app-hosting/README.md)

- [ ] [Compute Engine](services/compute-engine.md)
- [ ] [Managed Instance Groups](services/managed-instance-groups.md)
- [ ] [Cloud Run](services/cloud-run.md)
- [ ] [App Engine](services/app-engine.md)
- [ ] [Google Kubernetes Engine (GKE)](services/gke.md)
- [ ] [Batch](services/batch.md)

</details>

<details>
<summary><strong>05. Containers & Kubernetes</strong></summary>

[Open category learning guide](buckets/05-containers-kubernetes/README.md)

- [ ] [GKE Standard](services/gke-standard.md)
- [ ] [GKE Autopilot](services/gke-autopilot.md)
- [ ] [Artifact Registry](services/artifact-registry.md)
- [ ] [GKE Workload Identity Federation](services/gke-workload-identity-federation.md)
- [ ] [GKE Autoscaling](services/gke-autoscaling.md)
- [ ] [Cloud Service Mesh](services/cloud-service-mesh.md)

</details>

<details>
<summary><strong>06. Storage, Databases & Caching</strong></summary>

[Open category learning guide](buckets/06-storage-databases/README.md)

- [ ] [Cloud Storage](services/cloud-storage.md)
- [ ] [Persistent Disk](services/persistent-disk.md)
- [ ] [Filestore](services/filestore.md)
- [ ] [Cloud SQL](services/cloud-sql.md)
- [ ] [AlloyDB for PostgreSQL](services/alloydb-for-postgresql.md)
- [ ] [Cloud Spanner](services/cloud-spanner.md)
- [ ] [Firestore](services/firestore.md)
- [ ] [Bigtable](services/bigtable.md)
- [ ] [Memorystore](services/memorystore.md)

</details>

<details>
<summary><strong>07. Serverless, APIs & Integration</strong></summary>

[Open category learning guide](buckets/07-serverless-integration/README.md)

- [ ] [Cloud Run functions](services/cloud-run-functions.md)
- [ ] [API Gateway](services/api-gateway.md)
- [ ] [Apigee](services/apigee.md)
- [ ] [Pub/Sub](services/pub-sub.md)
- [ ] [Eventarc](services/eventarc.md)
- [ ] [Workflows](services/workflows.md)
- [ ] [Cloud Tasks](services/cloud-tasks.md)
- [ ] [Application Integration](services/application-integration.md)

</details>

<details>
<summary><strong>08. Data Engineering & Analytics</strong></summary>

[Open category learning guide](buckets/08-data-analytics/README.md)

- [ ] [BigQuery](services/bigquery.md)
- [ ] [Dataflow](services/dataflow.md)
- [ ] [Dataproc](services/dataproc.md)
- [ ] [Dataform](services/dataform.md)
- [ ] [Datastream](services/datastream.md)
- [ ] [BigLake](services/biglake.md)
- [ ] [Dataplex Universal Catalog](services/dataplex-universal-catalog.md)
- [ ] [Looker](services/looker.md)

</details>

<details>
<summary><strong>09. AI, ML & Generative AI</strong></summary>

[Open category learning guide](buckets/09-ai-ml-genai/README.md)

- [ ] [Vertex AI](services/vertex-ai.md)
- [ ] [Gemini on Vertex AI](services/gemini-on-vertex-ai.md)
- [ ] [Vertex AI Model Garden](services/vertex-ai-model-garden.md)
- [ ] [Vertex AI Search](services/vertex-ai-search.md)
- [ ] [Document AI](services/document-ai.md)
- [ ] [Cloud Vision API](services/cloud-vision-api.md)
- [ ] [Speech-to-Text](services/speech-to-text.md)
- [ ] [Text-to-Speech](services/text-to-speech.md)

</details>

<details>
<summary><strong>10. Security, Threat Detection & Compliance</strong></summary>

[Open category learning guide](buckets/10-security-compliance/README.md)

- [ ] [Cloud KMS](services/cloud-kms.md)
- [ ] [Secret Manager](services/secret-manager.md)
- [ ] [Cloud Armor](services/cloud-armor.md)
- [ ] [Security Command Center](services/security-command-center.md)
- [ ] [Cloud Audit Logs](services/cloud-audit-logs.md)
- [ ] [Cloud IDS](services/cloud-ids.md)
- [ ] [Sensitive Data Protection](services/sensitive-data-protection.md)
- [ ] [Certificate Authority Service](services/certificate-authority-service.md)

</details>

<details>
<summary><strong>11. DevOps, IaC & Operations</strong></summary>

[Open category learning guide](buckets/11-devops-iac-operations/README.md)

- [ ] [Cloud Build](services/cloud-build.md)
- [ ] [Cloud Deploy](services/cloud-deploy.md)
- [ ] [Terraform on Google Cloud](services/terraform-on-google-cloud.md)
- [ ] [Infrastructure Manager](services/infrastructure-manager.md)
- [ ] [Config Controller](services/config-controller.md)
- [ ] [Cloud Scheduler](services/cloud-scheduler.md)
- [ ] [Cloud Monitoring](services/cloud-monitoring.md)
- [ ] [Cloud Logging](services/cloud-logging.md)
- [ ] [Cloud Trace and Profiler](services/cloud-trace-and-profiler.md)

</details>

<details>
<summary><strong>12. Resilience, Migration, Cost & Architecture Patterns</strong></summary>

[Open category learning guide](buckets/12-resilience-migration-cost/README.md)

- [ ] [Backup and DR Service](services/backup-and-dr-service.md)
- [ ] [Migrate to Virtual Machines](services/migrate-to-virtual-machines.md)
- [ ] [Database Migration Service](services/database-migration-service.md)
- [ ] [Cloud Billing Budgets](services/cloud-billing-budgets.md)
- [ ] [Billing Export to BigQuery](services/billing-export-to-bigquery.md)
- [ ] [FinOps and Cost Optimization](services/finops-and-cost-optimization.md)
- [ ] [High Availability and Disaster Recovery Patterns](services/high-availability-and-disaster-recovery-patterns.md)

</details>

## Portfolio checkpoints
- [ ] Three-tier application: HTTPS load balancing + Compute Engine + Cloud SQL.
- [ ] Serverless API: API Gateway + Cloud Run + Firestore.
- [ ] Container platform: GKE + Artifact Registry.
- [ ] Event-driven pipeline: Cloud Storage + Pub/Sub + Eventarc.
- [ ] Analytics pipeline: Cloud Storage + Dataflow + BigQuery.
- [ ] Terraform-governed multi-project environment with least privilege.
- [ ] Vertex AI application with controlled access and observability.

## Lab evidence template
For each lab record the goal, architecture, prerequisites, identity model, deploy steps, validation, a failure test, actual cost observations, cleanup proof and lessons learned.

## Safety reminders
- Use a dedicated sandbox project where possible and set budgets/alerts. Budget notifications are not hard spending caps.
- Never commit credentials, service-account keys, secrets or production data.
- Prefer least privilege and workload identity patterns.
- Plan teardown before deployment and verify billable resources are removed.

## Official starting points
- [Google Cloud documentation](https://cloud.google.com/docs)
- [Google Cloud Architecture Framework](https://cloud.google.com/architecture/framework)
- [Google Cloud Skills Boost](https://www.cloudskillsboost.google/)
- [Google Cloud pricing](https://cloud.google.com/pricing)
