# Setup guides

## Build sequence

1. Create the dedicated GCP project and budget guardrail.
2. Create the custom VPC, regional subnet, and GKE secondary ranges.
3. Enable required APIs and establish the deployment service account.
4. Build and test the Flask API locally.
5. Containerize the API with Gunicorn and validate it with Docker.
6. Push the image to Artifact Registry.
7. Create the two-node Standard GKE cluster and connect with `gcloud` credentials.
8. Apply the Deployment, Service, probes, resource settings, and HPA.
9. Validate node, Pod, Service, and external endpoint behavior.
10. Connect GitHub to Cloud Build and configure separate application and Kubernetes triggers.
11. Exercise scaling, self-healing, rolling updates, monitoring, alerting, and recovery.

## Validation pattern

The lab used a repeatable validation sequence:

```text
configuration → rollout/status → runtime state → endpoint test → logs/metrics
```

Examples include `kubectl get nodes`, `kubectl get deployments`, `kubectl get pods -o wide`, `kubectl get services`, `kubectl rollout status`, `curl`, `kubectl logs`, and `kubectl top`.

## Resource settings

The final application configuration used a CPU request of `50m`, CPU limit of `250m`, memory request of `128Mi`, and memory limit of `256Mi`. The HPA managed between 2 and 8 replicas with a 60% CPU request-utilization target.

## Cost and safety practices

The project used a dedicated GCP project and approximately `$20` monthly budget alert. The lab avoided committing credentials and used a dedicated service identity for Cloud Build. Temporary load generation was removed after testing so the HPA could scale back down.
