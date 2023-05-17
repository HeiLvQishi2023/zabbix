#!/usr/bin/env python
# -*- coding:utf-8 -*-
from package.log import Log
from configparser import ConfigParser
from package.ping_address import ping
from package.system_load import get_system_load
from package.interface_traffic import get_net_io_counters


log = Log(__name__).getlog()


def sys_load():
    sys_load = get_system_load()
    log.info(f' 系统负载：{sys_load}')
    # print(sys_load)    
    

def interface_traffic(nic_name):
    rx_bytes, tx_bytes = get_net_io_counters(nic_name)
    log.info(f' {nic_name}: Received {rx_bytes} bytes, Sent {tx_bytes} bytes')
    # print("以太网: Received {} bytes, Sent {} bytes".format(rx_bytes, tx_bytes))
    

def ping_address(ip_address):
    packet_loss_rate, avg_rtt = ping(ip_address)
    log.info(f' 地址: {ip_address} ,丢包率：{packet_loss_rate}, 平均时延：{avg_rtt}ms')
    # print(f'丢包率：{packet_loss_rate}, 平均时延：{avg_rtt}ms')


def main():
    
    cfg = ConfigParser()
    cfg.read('./conf/config.ini')
    cfg.sections()

    cfg.get('zabbix conf','Server')
    cfg.get('zabbix conf','ServerPort')
    cfg.get('zabbix conf','Hostname')
    cfg.get('zabbix conf','DiscoveryHours')

    if cfg.getboolean('zabbix item','Item.sys'):
        sys_load()
    
    if cfg.getboolean('zabbix item','Item.if'):
        interface_traffic('eno1')
        
    if cfg.getboolean('zabbix item','Item.ping'):
        ping_address('8.8.8.6')
    
    log.debug('main.py: main()')
    log.warning('main.py: main()')