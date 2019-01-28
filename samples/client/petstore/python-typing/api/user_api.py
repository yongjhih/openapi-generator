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


class UserApi(Rests):


    async def create_user(self, body: User) -> None:
        """
        Create user

        method: POST
        path: /user

        :param User body: Created user object (required)

        :return: None
        """


    async def create_users_with_array_input(self, body: List[User]) -> None:
        """
        Creates list of users with given input array

        method: POST
        path: /user/createWithArray

        :param List[User] body: List of user object (required)

        :return: None
        """


    async def create_users_with_list_input(self, body: List[User]) -> None:
        """
        Creates list of users with given input array

        method: POST
        path: /user/createWithList

        :param List[User] body: List of user object (required)

        :return: None
        """


    async def delete_user(self, username: str) -> None:
        """
        Delete user

        method: DELETE
        path: /user/{username}

        :param str username: The name that needs to be deleted (required)

        :return: None
        """


    async def get_user_by_name(self, username: str) -> User:
        """
        Get user by user name

        method: GET
        path: /user/{username}

        :param str username: The name that needs to be fetched. Use user1 for testing. (required)

        :return: User
        """


    async def login_user(self, username: str, password: str) -> str:
        """
        Logs user into the system

        method: GET
        path: /user/login

        :param str username: The user name for login (required)
        :param str password: The password for login in clear text (required)

        :return: str
        """


    async def logout_user(self) -> None:
        """
        Logs out current logged in user session

        method: GET
        path: /user/logout


        :return: None
        """


    async def update_user(self, username: str, body: User) -> None:
        """
        Updated user

        method: PUT
        path: /user/{username}

        :param str username: name that need to be deleted (required)
        :param User body: Updated user object (required)

        :return: None
        """

