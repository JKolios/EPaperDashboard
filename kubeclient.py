import os

import kubernetes


def load_kubectl(kubeconfig_path=os.environ['KUBECTL_PATH']):
    kubernetes.config.load_kube_config(kubeconfig_path)


def core_v1_api():
    load_kubectl()
    return kubernetes.client.CoreV1Api()


def list_node():
    return core_v1_api().list_node()


def node_addreses(node):
    return ", ".join(
        [node_address.address for node_address in node.status.addresses])


def list_all_nodes():
    return [{
        'name': node.metadata.name,
        'addresses': node_addreses(node),
    } for node in list_node().items]


if __name__ == '__main__':
    load_kubectl()
    print(list_all_nodes())
