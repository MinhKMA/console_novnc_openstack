#!/usr/bin/python3.5
from keystoneauth1.identity import v3
from keystoneauth1 import session
from keystoneclient.v3 import client
import novaclient.client as nova_client

import conf


def auth():
    auth = v3.Password(auth_url=conf.URL, username=conf.USERNAME,
                       password=conf.PASSWORD, project_name=conf.PROJECT_NAME,
                       user_domain_id=conf.USER_DOMAIN_ID,
                       project_domain_id=conf.PROJECT_DOMAIN_ID)
    sess = session.Session(auth=auth)
    return sess


def main():
    sess = auth()
    nova = nova_client.Client("2.1", session=sess)
    for host in nova.servers.list():
        print(host.name, ":",  host.get_console_url(console_type='novnc'))
