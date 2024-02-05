#!/usr/bin/env python3

"""Parameterize a unit test."""

import unittest
from parameterized import parameterized

from utils import access_nested_map


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
