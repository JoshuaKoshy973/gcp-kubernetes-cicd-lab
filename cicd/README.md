# CI/CD

The repository uses two Cloud Build triggers on the `main` branch:

| Trigger | Scope | Configuration | Purpose |
| --- | --- | --- | --- |
| `app-cicd-trigger` | `app/**` | `cloudbuild-app.yaml` | Test, build, push, and deploy application changes. |
| `kubernetes-cicd-trigger` | `kubernetes/**` | `cloudbuild-kubernetes.yaml` | Apply Kubernetes configuration changes while preserving the live application image. |

The application pipeline runs unit tests, builds a Docker image, pushes it to Artifact Registry, and deploys it to GKE. Images are tagged with `$COMMIT_SHA`, creating a traceable relationship between source commit, image, and deployment.

The lab also documented and corrected three pipeline issues: explicit logging for the custom service account, a `gke-deploy` output-directory conflict, and the need to escape `$${CURRENT_IMAGE}` so Bash—not Cloud Build substitution processing—expands the variable.
