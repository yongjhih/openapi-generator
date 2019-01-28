# -*- coding: future_fstrings -*-

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


    async def deleteOrder(self, orderId: String = null ):
    """
    Delete purchase order by ID
    method: DELETE
    path: /store/order/{orderId}
    """


    async def getInventory(self) -> Map:
    """
    Returns pet inventories by status
    method: GET
    path: /store/inventory
    """


    async def getOrderById(self, orderId: Long = null ) -> Order:
    """
    Find purchase order by ID
    method: GET
    path: /store/order/{orderId}
    """


    async def placeOrder(self, bodyOrder ) -> Order:
    """
    Place an order for a pet
    method: POST
    path: /store/order
    """

