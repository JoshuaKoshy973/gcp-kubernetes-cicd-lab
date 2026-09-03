# GCP foundation screenshots

The foundation established the project boundary and the network ranges used by the rest of the lab.

### Project boundary

The [project screenshot](01-gcp-project-created.png) shows `GCP Kubernetes CICD Lab` selected with project ID `gcp-kubernetes-cicd-lab`. This project became the IAM, API, resource, and billing boundary for the lab.

### VPC and subnet design

The [VPC and subnet screenshot](02-gcp-vpc-subnet-created.png) shows `gcp-cicd-vpc`, `gcp-cicd-subnet` in `us-central1`, primary range `10.10.1.0/24`, Pod range `10.20.0.0/20`, and Service range `10.30.0.0/24`.
