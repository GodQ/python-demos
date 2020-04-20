from kubernetes import client, config, utils
import json
import base64

namespace = 'kube-system'
sa_name = 'alp-admin'
cluster_role_binding_name = 'alp-admin-role-binding'


def sa_clean_up(api_client):
    # delete the service account and binding
    api_core = client.CoreV1Api(api_client)
    api_rabc = client.RbacAuthorizationV1Api(api_client)
    # try:
    #     api_core.delete_namespace(namespace)
    #     while True:
    #         try:
    #             api_core.read_namespace(namespace)
    #             print('namespace is being deleted')
    #             time.sleep(2)
    #         except Exception as e:
    #             break
    # except Exception as e:
    #     pass
    try:
        api_core.delete_namespaced_service_account(name=sa_name, namespace=namespace)
    except Exception as e:
        pass
    try:
        api_rabc.delete_cluster_role_binding(name=cluster_role_binding_name)
    except Exception as e:
        pass


def sa_create():
    # get the api client by kube config file
    kube_config_file = "./k8s_config"
    client0 = config.new_client_from_config(config_file=kube_config_file)
    api_core = client.CoreV1Api(client0)
    # clean up the old config
    sa_clean_up(client0)
    # create service account and cluster role binding
    utils.create_from_yaml(client0, 'admin_sa.yaml', verbose=True)
    # search the secret by the service account
    sa_list = api_core.list_namespaced_service_account(namespace=namespace)
    secret_name = None
    for sa in sa_list.items:
        if sa.metadata.name == sa_name:
            secret_name = sa.secrets[0].name
    assert secret_name
    # get the token
    secret = api_core.read_namespaced_secret(secret_name, namespace=namespace)
    sa_token = base64.b64decode(secret.data['token']).decode()
    # get api service ip:port
    k8s_url = client0.configuration.host

    with open('token.txt', 'w') as fd:
        fd.write(json.dumps({'api_server': k8s_url, 'token': sa_token}))


def sa_usage():
    with open('token.txt', 'r') as fd:
        info = json.loads(fd.read())
    api_server = info['api_server']
    sa_token = info['token']
    configuration = client.Configuration()
    configuration.host = api_server
    configuration.verify_ssl = False
    configuration.api_key = {"authorization": "Bearer " + sa_token}
    client1 = client.api_client.ApiClient(configuration=configuration)
    api_core = client.CoreV1Api(client1)
    ret = api_core.list_namespace()
    print(ret)


sa_create()
sa_usage()
