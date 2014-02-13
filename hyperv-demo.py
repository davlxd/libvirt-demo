#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Acknowlegement:
# 
#  - Openstack/Nova source code (https://github.com/openstack/nova/blob/master/nova/virt/libvirt/driver.py)
#  - libvirt App Dev Guide (http://libvirt.org/guide/html/Application_Development_Guide-Connections.html#virtConnectOpenAuth-Example2)
#  - libvirt-python source code (where its public repo ???)

import libvirt
import sys
import json

authname_passphrase = """
{
    "authname": "Administrator",
    "passphrase": "1234!@#$asdf"
}
"""
remote_uri = 'hyperv://10.18.3.79/?transport=http'

def load_config():
    # f_config = open('winserv12-password.json')
    # return json.load(f_config)
    return json.loads(authname_passphrase)


libvirt_connection = None
def _connect_auth_cb(creds, opaque):
    passwd = load_config()
    
    for cred in creds:
        if cred[0] == libvirt.VIR_CRED_AUTHNAME:
            cred[4] = passwd["authname"]
        elif cred[0] == libvirt.VIR_CRED_PASSPHRASE:
            cred[4] = passwd["passphrase"]
    
    return 0

auth = [[libvirt.VIR_CRED_AUTHNAME,
         libvirt.VIR_CRED_PASSPHRASE],
        _connect_auth_cb,
        None]

def connect():
    libvirt_connection = libvirt.openAuth(remote_uri, auth, 0)
    if libvirt_connection == None:
        print 'Failed to open connection to the hypervisor'
        sys.exit(1)


def select_domain(name):
    try:
        dom0 = conn.lookupByName(name)
    except:
        print 'Failed to find the main domain'
        sys.exit(1)

    print "Domain 0: id %d running %s" % (dom0.ID(), dom0.OSType())
    print dom0.info()
    


def main():
    connect()
    select_domain('TW-DEV1')


if __name__ == '__main__':
    main()

