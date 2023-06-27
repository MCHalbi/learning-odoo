# Author: Lukas Halbritter <lukas.halbritter@jobrad.org>
# Copyright 2023
# pylint: disable=missing-docstring
import unittest
import pprint
from odoo import fields
from odoo.tests.common import TransactionCase


class EstatePropertyTests(TransactionCase):
    def setUp(self):
        self._model = self.env['estate.property']
        pprint.PrettyPrinter(indent=2).pprint(dir(self._model))

    def test_estate_property_has_required_attributes(self):
        self.assertModelHasAttributeWithType("name", fields.Char)
        self.assertModelHasAttributeWithType("description", fields.Text)
        self.assertModelHasAttributeWithType("postcode", fields.Char)
        self.assertModelHasAttributeWithType("date_availability", fields.Date)

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
