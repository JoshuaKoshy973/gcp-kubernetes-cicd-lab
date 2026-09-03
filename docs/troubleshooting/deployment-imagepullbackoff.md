# Incident: Deployment update failure

## Reported symptom

A recent deployment change did not complete normally, and the service might have been only partially available.

## Investigation

1. Checked Deployment and Pod state.
2. Found `ImagePullBackOff`.
3. Inspected the Deployment’s image reference.
4. Found the workload requested `gcp-cicd-app:incident-1-test`.
5. Checked Artifact Registry and confirmed that tag did not exist.

## Root cause

The Deployment referenced a nonexistent container image tag. Kubernetes could not pull the requested image, so the Pod could not start.

## Recovery and validation

Retrieved the live image reference, restored the known-good immutable commit-SHA image, and verified rollout completion with `kubectl rollout status` and healthy Pods.

## Lesson

An image-pull failure should be investigated at the image and registry layer before changing Service or application settings. Direct live edits can also create drift from Git and should be followed by a source-of-truth update.
