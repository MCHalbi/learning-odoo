# Author: Lukas Halbritter <lukas.halbritter@jobrad.org>
# Copyright 2023
# pylint: disable=missing-docstring
import unittest

# from models.estate_property import EstateProperty


class EstatePropertyTests(unittest.TestCase):
    def setUp(self):
        self._estate_properties = None

    def test_estate_property_attributes(self):
        self.assertTrue(hasattr(self._estate_properties, "name"))
