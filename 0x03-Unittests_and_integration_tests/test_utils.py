#!/usr/bin/env python3

"""Parameterize a unit test."""

import unittest
import requests
from parameterized import parameterized
from unittest.mock import patch, Mock

from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """paremetized unit test."""

    @parameterized.expand(
        [
            ({"a": 1}, ["a"], 1),
            ({"a": {"b": 2}}, ["a"], {"b": 2}),
            ({"a": {"b": 2}}, ["a", "b"], 2),
        ]
    )
    def test_access_nested_map(self, input_map, key_path, expected_output):
        """Tests the the mehtod returns what it is supposed to."""
        self.assertEqual(
                access_nested_map(input_map, key_path), expected_output)

    @parameterized.expand([({}, ["a"]), ({"a": 1}, ["a", "b"])])
    def test_access_nested_map_exception(self, input_map, key_path):
        """Tests that the method raises an error appropriatesly."""
        self.assertRaises(KeyError, access_nested_map, input_map, key_path)


class TestGetJson(unittest.TestCase):
    """Mock HTTP calls."""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """ test that utils.get_json returns the expected result."""
        with patch('requests.get') as mock_get:
            mock_response = mock_get.return_value
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            result = get_json(test_url)

            # Assert calls and results
            self.assertEqual(result, test_payload)
            mock_get.assert_called_once_with(test_url)
