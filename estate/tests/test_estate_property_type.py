# Author: Lukas Halbritter <halbi93@gmx.de>
# Copyright 2023
# pylint: disable=missing-docstring
import unittest
from odoo import fields
from odoo.tests.common import TransactionCase

class EstatePropertyTypeTests(TransactionCase):
    def setUp(self):
        self._model = self.env['estate.property.type']

    def test_estate_property_type_has_required_attributes(self):
        self.assertModelHasAttributeWithType("name", fields.Char)
        self.assertTrue(self._model._fields["name"].required)

    def assertModelHasAttributeWithType(
            self,
            attributeName: str,
            attributeType: fields.MetaField):
        self.assertModelHasAttribute(attributeName)
        self.assertModelAttributeHasType(attributeName, attributeType)

    def assertModelHasAttribute(self, attributeName: str):
        self.assertTrue(
            hasattr(self._model, attributeName),
            f"Field \"{attributeName}\" is missing from model \"{type(self._model).__name__}\".")

    def assertModelAttributeHasType(
            self,
            attributeName: str,
            attributeType: fields.MetaField):
        self.assertIsInstance(
            self._model._fields[attributeName],
            attributeType,
            f"Actual type is {type(self._model._fields[attributeName])}.")
