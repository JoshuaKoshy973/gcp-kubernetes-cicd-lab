# Monitoring screenshots

- [CPU utilization](20-gcp-monitoring-cpu-utilization.png) shows the filtered application time series, including the HPA load-test spike and return to baseline.
- [High CPU alert policy](21-gcp-monitoring-high-cpu-alert.png) shows the enabled `GCP CICD App High CPU` policy using Kubernetes CPU request utilization with an `0.8` threshold.

The lab also compared current snapshots from `kubectl top` with historical Cloud Monitoring time series and used Cloud Logging to investigate Gunicorn startup, shutdown, Pod creation, and restart activity.
