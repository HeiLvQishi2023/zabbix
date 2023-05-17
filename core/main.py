#!/usr/bin/env python
# -*- coding:utf-8 -*-
from package.log import Log
from configparser import ConfigParser
from package.ping_address import ping
from package.system_load import get_system_load
from package.interface_traffic import get_net_io_counters


def sys_load():
    sys_load = get_system_load()
    print(sys_load)    
    

def interface_traffic(nic_name):
    rx_bytes, tx_bytes = get_net_io_counters(nic_name)
    print("以太网: Received {} bytes, Sent {} bytes".format(rx_bytes, tx_bytes))
    

def ping_address(ip_address):
    packet_loss_rate, avg_rtt = ping(ip_address)
    print(f'丢包率：{packet_loss_rate}, 平均时延：{avg_rtt}ms')


def main():
    
    cfg = ConfigParser()
    cfg.read('../conf/config.ini')
    cfg.sections()

    cfg.get('zabbix conf','Server')
    cfg.get('zabbix conf','ServerPort')
    cfg.get('zabbix conf','Hostname')
    cfg.get('zabbix conf','DiscoveryHours')

    if cfg.getboolean('zabbix item','Item.sys'):
        sys_load()
    
    if cfg.getboolean('zabbix item','Item.if'):
        interface_traffic('以太网')
        
    if cfg.getboolean('zabbix item','Item.ping'):
        ping_address('114.114.114.114')
    
    log = Log(__name__).getlog()
    log.debug('test.py: main()')
    log.warning('test.py: main()')
    
    