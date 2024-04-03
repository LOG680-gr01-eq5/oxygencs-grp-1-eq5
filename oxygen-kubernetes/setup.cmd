kubectl apply -f configmap.yaml
kubectl apply -f secret.yaml
kubectl apply -f oxygen-deployment.yaml
kubectl --kubeconfig=kubeconf.yaml get pods

# Restart: kubectl rollout restart deployment log680-oxygen-deployment -n grp01eq5-namespace
# Get error/logs: kubectl logs nom-du-pod -n grp01eq5-namespace