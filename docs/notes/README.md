# Operational notes

## Core mental models

| Component | Operational responsibility |
| --- | --- |
| `gcloud` | Google Cloud infrastructure and GKE access. |
| `kubectl` | Kubernetes resources inside the cluster. |
| Deployment | Maintains the desired application workload. |
| ReplicaSet | Maintains the desired number of matching Pods. |
| Pod | Schedulable unit containing the application container. |
| Node | Compute VM where Pods run. |
| Service | Stable network frontend for replaceable Pods. |
| HPA | Adjusts replicas from observed utilization. |
| kubelet | Node agent that runs probes and manages containers. |

## Important distinctions

- A resource request influences scheduling; a limit caps runtime usage.
- HPA utilization is calculated relative to the CPU request, not the CPU limit.
- Readiness controls traffic eligibility; liveness controls restart behavior.
- `kubectl get` shows current state, `describe` shows configuration/events, `logs` shows application output, and `top` shows a current utilization snapshot.
- Cloud Monitoring provides historical time series; `kubectl top` is a point-in-time view.
- Application version strings and container image tags are separate identifiers.
- Direct cluster changes can be useful for diagnosis but create drift if Git and CI/CD are not updated.

## Lessons from failure

The most valuable learning came from investigating failures across multiple layers. `ImagePullBackOff` pointed to image availability, `CrashLoopBackOff` required examining the process exit behavior, and a successful `curl` test showed that a reported connectivity problem was not reproducible. The recurring pattern was to use evidence to update the hypothesis rather than forcing the first explanation.
