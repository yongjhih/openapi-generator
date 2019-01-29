# coding: utf-8
# -*- coding: future_fstrings -*-
#

import asyncio
import ssl
import time
import uuid
from typing import Any, Dict, List, Optional, NewType, TypeVar

import aiohttp
import jsonpickle
import jsontofu
from aiohttp.client import ClientSession
from aiohttp.client_ws import ClientWebSocketResponse
from aiohttp.http_websocket import WSMessage
from dataclasses import dataclass
from requests.exceptions import HTTPError


class DefaultApi(Rests):


    async def devices_get(self, authorization: str, page: Optional[object] = 1.0, per_page: Optional[object] = 10.0, sort: Optional[str], has_group: Optional[bool]) -> List[Device]:
        """
        List devices

        method: GET
        path: /devices

        :param str authorization: Contains the JWT token issued by the User Administration and Authentication Service. (required)
        :param object page: Starting page.
        :param object per_page: Number of results per page.
        :param str sort: Supports sorting the device list by attribute values.  The parameter is formatted as a list of attribute names and sort directions, e.g.:  '?sort=attr1:asc, attr2:desc'  will sort by 'attr1' ascending, and then by 'attr2' descending. 'desc' is the default sort direction, and can be omitted. 
        :param bool has_group: If present, limits the results only to devices assigned/not assigned to a group.

        :return: List[Device]
        """


    async def devices_id_delete(self, authorization: str, id: str) -> None:
        """
        Remove selected device

        method: DELETE
        path: /devices/{id}

        :param str authorization: Contains the JWT token issued by the User Administration and Authentication Service. (required)
        :param str id: Device identifier. (required)

        :return: None
        """


    async def devices_id_get(self, authorization: str, id: str) -> Device:
        """
        Get a selected device

        method: GET
        path: /devices/{id}

        :param str authorization: Contains the JWT token issued by the User Administration and Authentication Service. (required)
        :param str id: Device identifier. (required)

        :return: Device
        """


    async def devices_id_group_get(self, authorization: str, id: str) -> Group:
        """
        Get a selected device&#39;s group

        method: GET
        path: /devices/{id}/group

        :param str authorization: Contains the JWT token issued by the User Administration and Authentication Service. (required)
        :param str id: Device identifier. (required)

        :return: Group
        """


    async def devices_id_group_name_delete(self, authorization: str, id: str, name: str) -> None:
        """
        Remove a device from a group

        method: DELETE
        path: /devices/{id}/group/{name}

        :param str authorization: Contains the JWT token issued by the User Administration and Authentication Service. (required)
        :param str id: Device identifier. (required)
        :param str name: Group name. (required)

        :return: None
        """


    async def devices_id_group_put(self, authorization: str, id: str, group: Group) -> None:
        """
        Add a device to a group

        method: PUT
        path: /devices/{id}/group

        :param str authorization: Contains the JWT token issued by the User Administration and Authentication Service. (required)
        :param str id: Device identifier. (required)
        :param Group group: Group descriptor. (required)

        :return: None
        """


    async def groups_get(self) -> List[str]:
        """
        List groups

        method: GET
        path: /groups


        :return: List[str]
        """


    async def groups_name_devices_get(self, authorization: str, name: str, page: Optional[object] = 1.0, per_page: Optional[object] = 10.0) -> List[str]:
        """
        List the devices belonging to a given group

        method: GET
        path: /groups/{name}/devices

        :param str authorization: Contains the JWT token issued by the User Administration and Authentication Service. (required)
        :param str name: Group name. (required)
        :param object page: Starting page.
        :param object per_page: Number of results per page.

        :return: List[str]
        """

