from ldap3 import Server, Connection, ALL, MODIFY_ADD, MODIFY_REPLACE, MODIFY_DELETE


def test_ldap():
    server = 'vc.go.com'
    user = 'cn=administrator,cn=Users,dc=vsphere,dc=local'
    password = 'password'
    server = Server(host=server, get_info=ALL)
    conn = Connection(server=server, user=user, password=password)
    t = conn.bind()
    print(t)
    r = conn.search(search_base="dc=vsphere,dc=local", search_filter='(cn=*admin*)')
    print(r)
    if r:
        print('response:')
        print(conn.response)


def test_ldap_ssl():
    server = 'ldap.go.com'
    port = 636
    user = 'account@go.com'
    password = 'password'
    server_obj = Server(host=server, port=port, get_info=ALL, use_ssl=True)
    print('availability:', server_obj.check_availability())
    conn = Connection(server=server_obj, user=user, password=password)
    t = conn.bind()
    print('bind:', t)


if __name__ == "__main__":
    # test_ldap()
    test_ldap_ssl()
# a = Connect_ldap()
# a.add_user()
