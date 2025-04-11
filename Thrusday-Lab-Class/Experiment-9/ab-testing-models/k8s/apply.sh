kubectl apply -f deployment_v1.yaml
kubectl apply -f deployment_v2.yaml
kubectl apply -f service_a.yaml
kubectl apply -f service_b.yaml
kubectl apply -f ingress_main.yaml
kubectl apply -f ingress_canary.yaml