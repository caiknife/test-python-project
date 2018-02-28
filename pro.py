#!/usr/bin/env python
# coding:utf8

import httplib


def post_monitor_obj(metric, value, label="", app="qk"):
    """
    [prometheus]
    host="172.16.200.4"
    port=9091
    query_port=9090
    timeout=2
    ins="q-4"
    uri="/metrics/job/monitor"
    query_uri="/api/v1/query"
    """
    data = '%s{ins="%s", bu="lechuan", app="%s", group="monitor", label="%s", %s} ' % (
        metric, conf['ins'], app, metric, label)
    data = data + str(value) + '\n'
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = httplib.HTTPConnection(conf["host"], port=conf["port"], timeout=conf["timeout"])
    conn.request("POST", conf["uri"], data, headers)
    response = conn.getresponse()
    code = response.status
    conn.close()
    print "post_monitor_obj stat: code=%s, metric=%s, value=%s" % (code, metric, value)
    return code
