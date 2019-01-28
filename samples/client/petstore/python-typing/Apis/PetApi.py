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


class PetApi(Rests):


    async def addPet(self, bodyPet ):
    """
    Add a new pet to the store
    method: POST
    path: /pet
    """


    async def deletePet(self, petId: Long = null , apiKey: Optional[String] = null ):
    """
    Deletes a pet
    method: DELETE
    path: /pet/{petId}
    """


    async def findPetsByStatus(self, statusList = null ) -> List:
    """
    Finds Pets by status
    method: GET
    path: /pet/findByStatus
    """


    async def findPetsByTags(self, tagsList = null ) -> List:
    """
    Finds Pets by tags
    method: GET
    path: /pet/findByTags
    """


    async def getPetById(self, petId: Long = null ) -> Pet:
    """
    Find pet by ID
    method: GET
    path: /pet/{petId}
    """


    async def updatePet(self, bodyPet ):
    """
    Update an existing pet
    method: PUT
    path: /pet
    """


    async def updatePetWithForm(self, petId: Long = null , name: Optional[String] = null , status: Optional[String] = null ):
    """
    Updates a pet in the store with form data
    method: POST
    path: /pet/{petId}
    """


    async def uploadFile(self, petId: Long = null , additionalMetadata: Optional[String] = null , file: Optional[File] = null ) -> ApiResponse:
    """
    uploads an image
    method: POST
    path: /pet/{petId}/uploadImage
    """

