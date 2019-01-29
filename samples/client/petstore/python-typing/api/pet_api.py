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


class Rests():
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = aiohttp.ClientSession()

    def url(url: str) -> str:
        return url if url.startswith('http://') or url.startswith('https://') else f'{self.base_url} {url}'

    async def get(self, url: str):
        async with self.session.get(url(url)) as response:
            return await response

    async def post(self, url: str, data: Optional[Dict]):
        async with self.session.post(url(url)) as response:
            return await response

    async def put(self, url: str, data: Optional[Dict]):
        async with self.session.put(url(url)) as response:
            return await response

    async def delete(self, url: str):
        async with self.session.delete(url(url)) as response:
            return await response

    async def head(self, url: str):
        async with self.session.head(url(url)) as response:
            return await response

    async def options(self, url: str):
        async with self.session.head(url(url)) as response:
            return await response

    async def patch(self, url: str, data: Optional[Dict]):
        async with self.session.head(url(url)) as response:
            return await response

class PetApi(Rests):


    async def add_pet(self, body: Pet) -> None:
        """
        Add a new pet to the store

        method: POST
        path: /pet

        :param Pet body: Pet object that needs to be added to the store (required)

        :return: None
        """


    async def delete_pet(self, pet_id: int, api_key: Optional[str]) -> None:
        """
        Deletes a pet

        method: DELETE
        path: /pet/{petId}

        :param int pet_id: Pet id to delete (required)
        :param str api_key:

        :return: None
        """


    async def find_pets_by_status(self, status: List[str]) -> List[Pet]:
        """
        Finds Pets by status

        method: GET
        path: /pet/findByStatus

        :param List[str] status: Status values that need to be considered for filter (required)

        :return: List[Pet]
        """


    async def find_pets_by_tags(self, tags: List[str]) -> List[Pet]:
        """
        Finds Pets by tags

        method: GET
        path: /pet/findByTags

        :param List[str] tags: Tags to filter by (required)

        :return: List[Pet]
        """


    async def get_pet_by_id(self, pet_id: int) -> Pet:
        """
        Find pet by ID

        method: GET
        path: /pet/{petId}

        :param int pet_id: ID of pet to return (required)

        :return: Pet
        """


    async def update_pet(self, body: Pet) -> None:
        """
        Update an existing pet

        method: PUT
        path: /pet

        :param Pet body: Pet object that needs to be added to the store (required)

        :return: None
        """


    async def update_pet_with_form(self, pet_id: int, name: Optional[str], status: Optional[str]) -> None:
        """
        Updates a pet in the store with form data

        method: POST
        path: /pet/{petId}

        :param int pet_id: ID of pet that needs to be updated (required)
        :param str name: Updated name of the pet
        :param str status: Updated status of the pet

        :return: None
        """


    async def upload_file(self, pet_id: int, additional_metadata: Optional[str], file: Optional[file]) -> ApiResponse:
        """
        uploads an image

        method: POST
        path: /pet/{petId}/uploadImage

        :param int pet_id: ID of pet to update (required)
        :param str additional_metadata: Additional data to pass to server
        :param file file: file to upload

        :return: ApiResponse
        """

