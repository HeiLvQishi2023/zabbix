#!/usr/bin/env python
# -*- coding:utf-8 -*-
import psutil

def get_system_load():
    """
    获取系统1、5、15负载情况和内存、磁盘使用率
    :return: 返回一个字典,包含1、5、15分钟负载情况、内存使用率和磁盘使用率
    """
    # 获取1、5、15分钟负载情况
    loadavg = psutil.getloadavg()
    load_1 = loadavg[0]
    load_5 = loadavg[1]
    load_15 = loadavg[2]

    # 获取内存使用率
    mem = psutil.virtual_memory()
    mem_used_percent = mem.percent

    # 获取磁盘使用率
    disk = psutil.disk_usage('/')
    disk_used_percent = disk.percent

    result = {
        'load_1': load_1,
        'load_5': load_5,
        'load_15': load_15,
        'mem_used_percent': mem_used_percent,
        'disk_used_percent': disk_used_percent
    }

    return result
