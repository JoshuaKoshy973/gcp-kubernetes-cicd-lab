# Application

The project uses a deliberately small Flask API so infrastructure behavior is easy to observe.

Endpoints:

| Endpoint | Purpose |
| --- | --- |
| `/` | Returns the application greeting and internal release version. |
| `/health` | Returns the health payload used by Kubernetes probes. |
| `/version` | Returns the current application version. |

The application was tested locally, packaged with Gunicorn in `Dockerfile`, pushed to Artifact Registry, and deployed to GKE. The internal application version (`v1`, `v2`, or `v3`) is separate from the immutable Git commit SHA used as the Cloud Build image tag.

Run the unit tests from this directory with:

```bash
python -m unittest test_app.py
```
