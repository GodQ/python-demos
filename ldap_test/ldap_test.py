from ldap3 import Server, Connection, ALL, MODIFY_ADD, MODIFY_REPLACE, MODIFY_DELETE
# pip install asn1tools


# def test_ldap(server, user, password, search_base, search_filter, port=80):
#     server_obj = Server(host=server, get_info=ALL)
#     print('availability:', server_obj.check_availability())
#     conn = Connection(server=server_obj, user=user, password=password)
#     t = conn.bind()
#     print('bind:', t)
#     r = conn.search(search_base=search_base, search_filter=search_filter)
#     print('search:', r)
#     if r:
#         print('response:')
#         print(conn.response)


def ldap_connect(server, user, password, use_ssl=False, port=None):
    if not port:
        if use_ssl is True:
            port = 636
        else:
            port = 389

    server_obj = Server(host=server, port=port, get_info=ALL, use_ssl=use_ssl)
    print('availability:', server_obj.check_availability())
    conn = Connection(server=server_obj, user=user, password=password)
    t = conn.bind()
    print('bind:', t)
    print('who_am_i:', conn.extend.standard.who_am_i())
    return conn


def ldap_search(conn, search_base, search_filter):
    r = conn.search(search_base=search_base, search_filter=search_filter)
    print('search:', r)
    if r:
        print('response:')
        print(conn.response)


if __name__ == "__main__":
    pass

    server = '10.139.113.211'
    # user = 'cn=administrator,cn=Users,dc=oss,dc=local'
    user = 'administrator@oss.local'
    password = 'password'
    search_base = 'dc=oss,dc=local'
    search_filter = '(cn=*admin*)'
    conn = ldap_connect(server, user, password, use_ssl=False)
    ldap_search(conn, search_base=search_base, search_filter=search_filter)

    # server = 'ldap.a.com'
    # user = 'a@a.com'
    # password = 'password'
    # search_base = 'dc=a,dc=com'
    # search_filter = '(cn=*user*)'
    # conn = ldap_connect(server, user, password, use_ssl=True)
    # ldap_search(conn, search_base=search_base, search_filter=search_filter)

