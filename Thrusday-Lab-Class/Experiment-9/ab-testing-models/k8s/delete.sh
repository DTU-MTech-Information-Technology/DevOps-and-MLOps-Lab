kubectl delete -f deployment_v1.yaml
kubectl delete -f deployment_v2.yaml
kubectl delete -f service_a.yaml
kubectl delete -f service_b.yaml
kubectl delete -f ingress_main.yaml
kubectl delete -f ingress_canary.yaml