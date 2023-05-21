#!/usr/bin/env python
# -*- coding:utf-8 -*-
from pyzabbix import ZabbixSender, ZabbixMetric

def report_to_zabbix(server_ip, server_port, hostname, key, value, timestamp):
    # 创建 ZabbixSender 实例
    sender = ZabbixSender(zabbix_server=server_ip, zabbix_port=server_port)

    # 构建要发送的数据
    data = ZabbixMetric(hostname, key, value, timestamp)

    # 发送数据
    response = sender.send([data])

    # 根据返回结果输出 OK 或 Error
    if response.failed:
        return "Error"
    else:
        return "OK"

# 示例用法
# server_ip = "1.1.1.1"
# server_port = 10051
# hostname = "hostname"
# key = "itme[key]"
# value = 999999
# timestamp = int(time.time())

# report_to_zabbix(server_ip, server_port, hostname, key, value, timestamp)