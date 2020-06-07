#!/usr/bin/env python

import requests

from .auth_helper import get_service_realm, scope_generate
from .log_helper import logger
import json


class Registry(object):
    def __init__(
        self,
        username,
        password,
        image,
        registry_url,
        new_image_tag,
        old_image_tag="latest",
    ):
        self.username = username
        self.password = password
        self.image = image
        self.registry_url = registry_url
        self.old_image_tag = old_image_tag
        self.new_image_tag = new_image_tag
        self.token = self.get_auth_token()

    def get_auth_token(self):
        auth = requests.auth.HTTPBasicAuth(self.username, self.password)
        service_realm_info = get_service_realm(self.registry_url)
        custom_headers = {"Content-Type": "application/json"}
        scope = scope_generate(self.image)
        if service_realm_info:
            payload = {"service": service_realm_info["service"], "scope": scope}
            auth_res = requests.post(
                service_realm_info["realm"],
                auth=auth,
                headers=custom_headers,
                params=payload,
            )
            return auth_res.json()["token"]
        logger.error("service_realm_info is None!")
        return None

    def _manifests_uri(self, image_tag):
        return "/v2/{}/manifests/{}".format(self.image, image_tag)

    def get_image_manifests(self):
        tag_api_uri = self._manifests_uri(self.old_image_tag)
        custom_headers = {
            "Content-Type": "application/json",
            "accept": "application/vnd.docker.distribution.manifest.v2+json",
            "Authorization": "Bearer {}".format(self.token),
        }
        manifest_res = requests.get(
            self.registry_url + tag_api_uri, headers=custom_headers,
        )
        return manifest_res.json()

    def add_new_tag_by_registry(self):
        tag_api_uri = self._manifests_uri(self.new_image_tag)
        old_image_manifests = self.get_image_manifests()
        if old_image_manifests:
            logger.info(old_image_manifests)
            custom_headers = {
                "Content-Type": "application/vnd.docker.distribution.manifest.v2+json",
                "Authorization": "Bearer {}".format(self.token),
            }
            add_new_tag_res = requests.put(
                self.registry_url + tag_api_uri,
                headers=custom_headers,
                data=json.dumps(old_image_manifests),
            )
            print(add_new_tag_res.text)
            add_new_tag_res.raise_for_status()
            logger.info(
                "add new tag {} for {} is ok!".format(self.new_image_tag, self.image)
            )
        else:
            logger.error("old_image_manifests is None")
