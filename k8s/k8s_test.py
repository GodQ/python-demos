from kubernetes.client import api_client
from kubernetes.client.apis import core_v1_api


def test_service_apis():
    from kubernetes import client
    k8s_url = 'https://127.0.0.1:6443'
    with open('token.txt', 'r') as file:
        token = file.read().strip('\n')
    configuration = client.Configuration()
    configuration.host = k8s_url
    configuration.verify_ssl = False
    configuration.api_key = {"authorization": "Bearer " + token}
    client1 = api_client.ApiClient(configuration=configuration)
    api = core_v1_api.CoreV1Api(client1)
    ret = api.list_pod_for_all_namespaces(watch=False)
    print(ret)


test_service_apis()