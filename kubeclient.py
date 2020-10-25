import os

import kubernetes

core_v1_api_client = None

def load_kubectl(kubeconfig_path=os.environ['KUBECONFIG']):
    kubernetes.config.load_kube_config(kubeconfig_path)


def core_v1_api():
    if core_v1_api_client:
        return core_v1_api_client
    load_kubectl()
    return kubernetes.client.CoreV1Api()


def list_node():
    return core_v1_api().list_node()

def list_service_for_all_namespaces():
    return core_v1_api().list_service_for_all_namespaces()

def node_addreses(node):
    return ", ".join(
        [node_address.address for node_address in node.status.addresses])

def list_all_nodes():
    return [{
        'name': node.metadata.name,
        'addresses': node_addreses(node),
    } for node in list_node().items]

def list_all_services():
     return [{
         'name': service.metadata.name,
         'ip': service.status.load_balancer.ingress[0].ip
         } for service in list_service_for_all_namespaces().items if service.spec.type == 'LoadBalancer']

if __name__ == '__main__':
    load_kubectl()
    print(list_all_nodes())
    print(list_all_services())
