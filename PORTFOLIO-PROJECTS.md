# GCP Portfolio Projects

Build in a sandbox with budgets, least privilege and explicit teardown steps. Verify current service behavior and pricing before deploying.

## 1. Three-tier web application
**Services:** Cloud Load Balancing, Compute Engine or managed runtime, Cloud SQL, Cloud Monitoring.
- [ ] Diagram request and data flows.
- [ ] Define network and identity boundaries.
- [ ] Deploy HTTPS ingress and an application tier.
- [ ] Test database access, health checks, scaling, backup and restore.
- [ ] Capture cost and cleanup evidence.

## 2. Serverless API
**Services:** API Gateway, Cloud Run, Firestore, Secret Manager.
- [ ] Define API contract and authentication.
- [ ] Deploy a minimal service and restrict data access.
- [ ] Test error handling, timeouts and denied access.
- [ ] Document costs and teardown.

## 3. Kubernetes platform
**Services:** GKE, Artifact Registry, Cloud Build, Cloud Monitoring.
- [ ] Compare GKE Autopilot and Standard.
- [ ] Publish an image and deploy a sample workload.
- [ ] Configure workload identity and scaling.
- [ ] Test rollout/rollback, health checks and security boundaries.

## 4. Event-driven processing
**Services:** Cloud Storage, Pub/Sub, Eventarc, Cloud Run.
- [ ] Diagram event path and idempotency.
- [ ] Test retries and duplicate events.
- [ ] Restrict bucket and service access.
- [ ] Verify cleanup and charges.

## 5. Analytics pipeline
**Services:** Cloud Storage, Dataflow, BigQuery, Looker.
- [ ] Define schema and data quality checks.
- [ ] Ingest a small synthetic dataset.
- [ ] Transform and query it; define retention and access.
- [ ] Track processing and query cost.

## 6. Governed multi-project landing zone
**Services:** Resource Manager, IAM, Organization Policy, Shared VPC, Terraform.
- [ ] Design folder/project boundaries and policy inheritance.
- [ ] Add roles, labels, baseline logging and budgets.
- [ ] Build reusable modules and review a Terraform plan.
- [ ] Document rollback and limitations.

## 7. Vertex AI GenAI application
**Services:** Vertex AI, IAM, Cloud Logging/Monitoring.
- [ ] Define use case, safety constraints and evaluation criteria.
- [ ] Confirm model and region availability in official documentation.
- [ ] Restrict access and protect sensitive data.
- [ ] Measure quality, latency, cost and failure behavior.

## Deliverable standard
Include a diagram, README, IaC, deployment steps, validation, security analysis, cost assumptions, test evidence, cleanup, and known limitations.
