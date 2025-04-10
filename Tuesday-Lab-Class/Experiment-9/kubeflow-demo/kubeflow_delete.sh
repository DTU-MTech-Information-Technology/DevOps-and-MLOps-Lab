export PIPELINE_VERSION=2.4.0

kubectl delete -k "github.com/kubeflow/pipelines/manifests/kustomize/env/dev?ref=$PIPELINE_VERSION"
kubectl delete -k "github.com/kubeflow/pipelines/manifests/kustomize/cluster-scoped-resources?ref=$PIPELINE_VERSION"

kubectl delete -f https://github.com/kserve/kserve/releases/download/v0.15.0/kserve.yaml
