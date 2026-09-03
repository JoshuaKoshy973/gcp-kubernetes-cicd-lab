# GKE and Kubernetes screenshots

This phase provides the workload foundation:

- [GKE cluster](05-gke-cluster-running.png): Standard mode, two nodes, Running, `us-central1-a`.
- [Node validation](06-kubectl-gke-nodes.png): both nodes Ready, `10.10.1.x` node addresses, and `containerd` runtime.
- [Deployment and Pods](07-kubernetes-deployment-pods.png): two application Pods Running on separate nodes.
- [LoadBalancer Service](08-kubernetes-loadbalancer-service.png): ClusterIP `10.30.0.135`, external IP, and port 80 to 8080 mapping.
- [External application test](09-external-loadbalancer-app-test.png): successful requests to all application endpoints.
- [Health probes](17-kubernetes-health-probes.png): liveness/readiness configuration, Ready `True`, and restart count `0`.
