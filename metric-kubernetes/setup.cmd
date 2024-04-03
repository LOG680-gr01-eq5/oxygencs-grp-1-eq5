kubectl apply -f configmap.yaml
kubectl apply -f secret.yaml
kubectl apply -f kanban-deployment.yaml
kubectl --kubeconfig=kubeconf.yaml get pods

# Restart: kubectl rollout restart deployment log680-kanban-deployment -n grp01eq5-namespace
# Get error/logs: kubectl logs nom-du-pod -n grp01eq5-namespace
# Get deployments: kubectl get deployment -n grp01eq5-namespace