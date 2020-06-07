#!/usr/bin/env python
import requests


def kv2dict(kvinfo):
    kv = {}
    for item in kvinfo.split(","):
        item_list = item.split("=")
        kv[item_list[0]] = item_list[1].strip('"')
    return kv


def get_service_realm(registry_url):
    registry_api_url = (
        registry_url if registry_url.endswith("/v2/") else registry_url + "/v2/"
    )
    registry_res = requests.get(registry_api_url)
    www_authenticate_header = registry_res.headers.get("Www-Authenticate")
    print(www_authenticate_header)
    if www_authenticate_header:
        return kv2dict(www_authenticate_header.split()[-1])
    return None


def scope_generate(image):

    return "repository:{}:pull,push".format(image)
