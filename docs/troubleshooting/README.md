# Troubleshooting documentation

The lab used layered troubleshooting instead of immediately changing configuration:

```text
symptom
  ↓
identify affected layer
  ↓
collect state, events, logs, and metrics
  ↓
form or update a hypothesis
  ↓
correct the smallest confirmed cause
  ↓
retest and document recovery
```

Recommended layer order:

```text
Git/source → Cloud Build → Artifact Registry → container process
→ Pod → Deployment → Service → LoadBalancer/network → Node/infrastructure
```

## Incidents

- [Deployment update failure](deployment-imagepullbackoff.md): nonexistent image tag causing `ImagePullBackOff`.
- [Application instability](application-crashloopbackoff.md): command override causing `CrashLoopBackOff`.
- [Reported connectivity issue](reported-connectivity.md): ticket could not be reproduced because the full request path was healthy.

## Additional troubleshooting evidence

The project also encountered and resolved a CPU scheduling failure, probe-triggered restart, Cloud Build logging failure, Cloud Build substitution issue, `gke-deploy` output-directory conflict, and application-image drift between Git-managed YAML and live Kubernetes state.
