# Incident: Application instability

## Reported symptom

New workload instances were not remaining healthy and users reported abnormal application behavior.

## Investigation

1. Checked Pods and found `CrashLoopBackOff`.
2. Considered a health-probe failure as an initial hypothesis.
3. Reviewed probe configuration and checked current and previous container logs.
4. Used `kubectl describe pod` when logs did not provide the cause.
5. Found `Last State: Terminated`, exit code `1`, increasing restart count, and a command override of `/bin/sh -c exit 1`.

## Root cause

The Deployment overrode the image’s normal Gunicorn command with `exit 1`. The container started and immediately exited, causing Kubernetes to restart it repeatedly.

## Recovery and validation

Removed the bad command override, allowed the image’s normal startup command to run, and verified healthy Pods and rollout recovery.

## Lesson

The first hypothesis was reasonable but wrong. Probe symptoms and process failures can look similar; `describe` output and exit status provided the decisive evidence.
