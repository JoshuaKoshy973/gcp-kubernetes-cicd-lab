# Architecture documentation

## End-to-end flow

```text
Developer
  ↓ git push
GitHub
  ↓ matching Cloud Build trigger
Cloud Build
  ↓ tests and Docker build
Artifact Registry
  ↓ immutable image reference
GKE Deployment
  ↓ ReplicaSet reconciliation
Pods on GKE Nodes
  ↓ Service selector
Kubernetes LoadBalancer
  ↓ external IP
Client
```

## GCP foundation

The lab uses project `gcp-kubernetes-cicd-lab`, VPC `gcp-cicd-vpc`, and regional subnet `gcp-cicd-subnet` in `us-central1`.

| Range | Role |
| --- | --- |
| `10.10.1.0/24` | Subnet primary range for GKE node and VM addresses. |
| `10.20.0.0/20` | GKE secondary range for Pod IPs. |
| `10.30.0.0/24` | GKE secondary range for Service ClusterIPs. |

This separation made it possible to identify whether an address belonged to infrastructure, a workload Pod, or a Kubernetes Service during troubleshooting.

## Kubernetes responsibilities

`Deployment` defines the application workload and desired Pod template. `ReplicaSet` maintains the requested number of matching Pods. `Service` provides a stable frontend while Pod IPs change. `HPA` adjusts the replica count based on CPU request utilization. The node kubelet executes probes, manages container lifecycle, and reports state to the control plane.

## Identity and delivery

Cloud Build uses the dedicated `gcp-cicd-deployer` service account rather than a human identity. The application trigger handles `app/**` changes; the Kubernetes trigger handles `kubernetes/**` changes. Application images are published with commit-SHA tags so a source commit can be traced to an exact image and deployment.

## Observability

Cloud Logging provides historical container output and lifecycle events. Cloud Monitoring provides historical metrics and alert policies. HPA responds automatically at its configured target, while the high-CPU alert provides a human-facing signal for sustained elevated utilization.
