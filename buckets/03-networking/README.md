# Networking & Connectivity

> Category learning tracker for GCP Master Vault. Service names and examples in this folder are GCP-specific.

## Category architecture

![Networking & Connectivity architecture](architecture.svg)

- [Editable category diagram](architecture.drawio)
- [Mermaid source](architecture.mmd)
- [Full visual library](../../VISUAL-DIAGRAMS.md)
- [Master architecture](../../GCP-ENTERPRISE-REFERENCE-ARCHITECTURE.md)

## Component tracker

| Topic guide | SVG diagram | Editable draw.io |
|---|---|---|
| [VPC Networks](../../services/vpc-networks.md) | [SVG](../../services/vpc-networks/architecture.svg) | [draw.io](../../services/vpc-networks/architecture.drawio) |
| [Subnets and Routes](../../services/subnets-and-routes.md) | [SVG](../../services/subnets-and-routes/architecture.svg) | [draw.io](../../services/subnets-and-routes/architecture.drawio) |
| [Firewall Rules and Policies](../../services/firewall-rules-and-policies.md) | [SVG](../../services/firewall-rules-and-policies/architecture.svg) | [draw.io](../../services/firewall-rules-and-policies/architecture.drawio) |
| [Cloud NAT](../../services/cloud-nat.md) | [SVG](../../services/cloud-nat/architecture.svg) | [draw.io](../../services/cloud-nat/architecture.drawio) |
| [Private Google Access](../../services/private-google-access.md) | [SVG](../../services/private-google-access/architecture.svg) | [draw.io](../../services/private-google-access/architecture.drawio) |
| [Private Service Connect](../../services/private-service-connect.md) | [SVG](../../services/private-service-connect/architecture.svg) | [draw.io](../../services/private-service-connect/architecture.drawio) |
| [Cloud VPN](../../services/cloud-vpn.md) | [SVG](../../services/cloud-vpn/architecture.svg) | [draw.io](../../services/cloud-vpn/architecture.drawio) |
| [Cloud Interconnect](../../services/cloud-interconnect.md) | [SVG](../../services/cloud-interconnect/architecture.svg) | [draw.io](../../services/cloud-interconnect/architecture.drawio) |
| [Cloud DNS](../../services/cloud-dns.md) | [SVG](../../services/cloud-dns/architecture.svg) | [draw.io](../../services/cloud-dns/architecture.drawio) |
| [Cloud Load Balancing](../../services/cloud-load-balancing.md) | [SVG](../../services/cloud-load-balancing/architecture.svg) | [draw.io](../../services/cloud-load-balancing/architecture.drawio) |

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
