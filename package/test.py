#!/usr/bin/env python
# -*- coding:utf-8 -*-
# from zabbix_requst import ZabbixSender

# zabbix_sender = ZabbixSender("http://101.36.128.38:6868/", "pogo_pe_1")

# zabbix_sender.send("sysload_get[load_avg_1]", 1)


from interface_traffic import get_net_io_counters

rx_bytes, tx_bytes = get_net_io_counters('以太网')
print("以太网: Received {} bytes, Sent {} bytes".format(rx_bytes, tx_bytes))


from system_load import get_system_load
sys_load = get_system_load()

print(sys_load)

from ping_address import ping
packet_loss_rate, avg_rtt = ping('8.8.8.8')
print(f'丢包率：{packet_loss_rate}, 平均时延：{avg_rtt}ms')

# 导入日志模块
from log import Log

# 实例化日志模块
log = Log(__name__).getlog()
log.debug('test.py: main()')
log.warning('test.py: main()')





