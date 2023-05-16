#!/usr/bin/env python
# -*- coding:utf-8 -*-
from package.log import Log
from package.ping_address import ping
from package.system_load import get_system_load
from package.interface_traffic import get_net_io_counters


def main():
    
    sys_load = get_system_load()
    print(sys_load)
    
    rx_bytes, tx_bytes = get_net_io_counters('以太网')
    print("以太网: Received {} bytes, Sent {} bytes".format(rx_bytes, tx_bytes))
    
    packet_loss_rate, avg_rtt = ping('8.8.8.8')
    print(f'丢包率：{packet_loss_rate}, 平均时延：{avg_rtt}ms')
    
    log = Log(__name__).getlog()
    log.debug('test.py: main()')
    log.warning('test.py: main()')
    
    