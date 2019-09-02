import jenkins
import json
import xmldict
import pprint

# Jenkins_URL = 'http://10.1.2.3:8080'
# username = 'chuanhao.qu'
# password = '123'

Jenkins_URL = 'http://192.168.1.5:8080'
username = 'admin'
password = 'password'

def connect():
    server = jenkins.Jenkins(Jenkins_URL, username=username, password=password)
    user = server.get_whoami()
    version = server.get_version()
    print('Hello %s from Jenkins %s' % (user['fullName'], version))
    jobs = server.get_jobs()
    print jobs
    print server.jobs_count()
    return server

def create_job(server):
    server.create_job('empty', jenkins.EMPTY_CONFIG_XML)
    jobs = server.get_jobs()
    print jobs
    my_job = server.get_job_config('api_test_framework')
    print(my_job) # prints XML configuration

    server.build_job('empty')
    server.disable_job('empty')
    server.copy_job('empty', 'empty_copy')
    server.enable_job('empty_copy')
    server.reconfig_job('empty_copy', jenkins.RECONFIG_XML)

    server.delete_job('empty')
    server.delete_job('empty_copy')

    # build a parameterized job
    # requires creating and configuring the api-test job to accept 'param1' & 'param2'
    server.build_job('api-test', {'param1': 'test value 1', 'param2': 'test value 2'})
    last_build_number = server.get_job_info('api-test')['lastCompletedBuild']['number']
    build_info = server.get_build_info('api-test', last_build_number)
    print build_info

    # get all jobs from the specific view
    jobs = server.get_jobs(view_name='test')
    print jobs

def nodes(server):
    nodes = server.get_nodes()
    print nodes
    for node in nodes:
        if node['name']=='slave1':
            server.delete_node("slave1")
    # create node with parameters
    params = {
        'port': '22',
        'username': 'quc',
        'credentialsId': 'adcbf6e0-8188-47dc-ba7e-15f00dcd69ef',
        'host': '192.168.1.5'
    }
    server.create_node(
        'slave1',
        nodeDescription='my test slave',
        remoteFS='/home/quc/slave1',
        labels='precise',
        exclusive=True,
        launcher=jenkins.LAUNCHER_SSH,
        launcher_params=params)
    nodes = server.get_nodes()
    print nodes
    node_config = server.get_node_info('slave1')
    print node_config
    #server.delete_node("slave1")
    nodes = server.get_nodes()
    print nodes

def get_job_config(server):
    conf_xml = server.get_job_config('api_test_framework')

    conf_xml = conf_xml.split("\n", 1)[1]
    print conf_xml
    conf = xmldict.xml_to_dict(str(conf_xml))
    import pprint
    pprint.pprint(conf)


if __name__=='__main__':
    server = connect()
    get_job_config(server)
