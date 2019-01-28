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


class UserApi(Rests):


    async def createUser(self, bodyUser ):
    """
    Create user
    method: POST
    path: /user
    """


    async def createUsersWithArrayInput(self, bodyList ):
    """
    Creates list of users with given input array
    method: POST
    path: /user/createWithArray
    """


    async def createUsersWithListInput(self, bodyList ):
    """
    Creates list of users with given input array
    method: POST
    path: /user/createWithList
    """


    async def deleteUser(self, username: String = null ):
    """
    Delete user
    method: DELETE
    path: /user/{username}
    """


    async def getUserByName(self, username: String = null ) -> User:
    """
    Get user by user name
    method: GET
    path: /user/{username}
    """


    async def loginUser(self, username: String = null , password: String = null ) -> String:
    """
    Logs user into the system
    method: GET
    path: /user/login
    """


    async def logoutUser(self):
    """
    Logs out current logged in user session
    method: GET
    path: /user/logout
    """


    async def updateUser(self, username: String = null , bodyUser ):
    """
    Updated user
    method: PUT
    path: /user/{username}
    """

