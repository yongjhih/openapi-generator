# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    OpenAPI spec version: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import petstore_api
from petstore_api.api.default_api import DefaultApi  # noqa: E501
from petstore_api.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = petstore_api.api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_foo_get(self):
        """Test case for foo_get

        """
        pass


if __name__ == '__main__':
    unittest.main()
