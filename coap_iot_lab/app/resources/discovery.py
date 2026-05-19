"""
Arquivo: app/resources/discovery.py

Objetivo:
    Adicionar o recurso /.well-known/core ao site CoAP.
"""

import aiocoap.resource as resource

def add_discovery_resource(site: resource.Site):
    site.add_resource(
        [".well-known", "core"],
        resource.WKCResource(site.get_resources_as_linkheader)
    )