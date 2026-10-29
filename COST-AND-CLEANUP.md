# Cost, Budgets & Lab Cleanup

## Before a lab
- Use a dedicated sandbox project and confirm billing.
- Set a budget and alert thresholds; alerts do not automatically stop spending.
- Check target-region pricing and free-tier eligibility.
- Define ownership labels and teardown checklist before provisioning.
- Avoid production data and credentials.

## Common cost drivers
Compute uptime and machine shape; disks and snapshots; load balancers, NAT and egress; GKE resources; database capacity, storage and backups; BigQuery queries/storage; Dataflow workers; log ingestion/retention; AI model usage.

## Cleanup checklist
- [ ] Remove deployed workloads.
- [ ] Remove idle VMs, disks, snapshots, IP addresses and forwarding rules.
- [ ] Remove temporary buckets and test data after checking retention needs.
- [ ] Delete test databases only after confirming they are not shared.
- [ ] Remove lab clusters, load balancers, NAT and test network resources.
- [ ] Review scheduled jobs, pipelines, logs and retained artifacts.
- [ ] Confirm resources are gone and inspect billing data.

Never automate cleanup without verifying project and target resources. Budget notifications are not spending caps.
