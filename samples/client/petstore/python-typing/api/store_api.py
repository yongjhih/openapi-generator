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


class StoreApi(Rests):


    async def delete_order(self, order_id: str) -> None:
        """
        Delete purchase order by ID

        method: DELETE
        path: /store/order/{orderId}

        :param str order_id: ID of the order that needs to be deleted (required)

        :return: None
        """


    async def get_inventory(self) -> Dict(str, int):
        """
        Returns pet inventories by status

        method: GET
        path: /store/inventory


        :return: Dict(str, int)
        """


    async def get_order_by_id(self, order_id: int) -> Order:
        """
        Find purchase order by ID

        method: GET
        path: /store/order/{orderId}

        :param int order_id: ID of pet that needs to be fetched (required)

        :return: Order
        """


    async def place_order(self, body: Order) -> Order:
        """
        Place an order for a pet

        method: POST
        path: /store/order

        :param Order body: order placed for purchasing the pet (required)

        :return: Order
        """

