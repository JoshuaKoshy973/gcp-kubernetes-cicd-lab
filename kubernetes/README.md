# Kubernetes

The Kubernetes layer is intentionally split by responsibility:

- `deployment.yaml` defines the application container, health probes, labels, ports, and resource requests/limits.
- `service.yaml` provides a stable `LoadBalancer` frontend on port 80 and routes to the container on port 8080.
- `hpa.yaml` owns replica-count decisions with a 2–8 replica range and a 60% CPU request-utilization target.

Observed relationships:

```text
Deployment → ReplicaSet → Pods → containers
Service → matching Pod labels → stable traffic path
HPA → Deployment replica count
kubelet → probes, container lifecycle, and restarts
```

The lab validated four-replica scaling, Pod replacement after deletion, rolling updates to v2, readiness/liveness behavior, scheduling failures caused by CPU requests, and HPA scale-up and scale-down.
