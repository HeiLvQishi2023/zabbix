#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
from zabbix_api import ZabbixAPI

class ZabbixReporter:
    def __init__(self, server, host_name, item_key):
        self.server = server
        self.host_name = host_name
        self.item_key = item_key
        self.zabbix = ZabbixAPI(server)
        # self.zabbix.session.verify = False
        self.zabbix.session.auth = None
        
    def report(self, value):
        # self.zabbix.login("Admin", "zabbix")
        # host = self.zabbix.host.get(filter={"host": self.host_name})[0]
        item = self.zabbix.item.get(host=self.host_name, search={"key_": self.item_key})[0]
        self.zabbix.item.update(itemid=item["itemid"], status=0, value=value)
        self.zabbix.logout()
'''

import json
import requests


class ZabbixSender:
    def __init__(self, zabbix_server_url, zabbix_host):
        self.zabbix_server_url = zabbix_server_url.rstrip('/')
        self.zabbix_host = zabbix_host
        self.zabbix_sender_url = f'{self.zabbix_server_url}/api_jsonrpc.php'
        self.auth_token = None

    def send(self, item_key, value):
        data = {
            'jsonrpc': '2.0',
            'method': 'item.create',
            'params': {
                'host': self.zabbix_host,
                'key_': item_key,
                'value_type': 0,
                'history': 0,
                'data_type': 0,
                'delay': 1,
                'value': value,
            },
            'id': 1,
        }

        headers = {'Content-Type': 'application/json-rpc'}
        response = requests.post(self.zabbix_sender_url, headers=headers, data=json.dumps(data), verify=False)
        response_json = response.json()

        if 'error' in response_json:
            raise Exception(f'ZabbixSender error: {response_json["error"]["message"]}')

