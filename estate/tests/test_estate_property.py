# Author: Lukas Halbritter <lukas.halbritter@jobrad.org>
# Copyright 2023
# pylint: disable=missing-docstring
import unittest
import pprint
from odoo import fields
from odoo.tests.common import TransactionCase


class EstatePropertyTests(TransactionCase):
    def setUp(self):
        self._model = self.env["estate.property"]

    def test_estate_property_has_required_attributes(self):
        self.assertModelHasAttributeWithType("name", fields.Char)
        self.assertModelHasAttributeWithType("description", fields.Text)
        self.assertModelHasAttributeWithType("postcode", fields.Char)
        self.assertModelHasAttributeWithType("date_availability", fields.Date)

    def test_estate_property_uses_correct_form_view(self):
        # Check, that not the default view is used
        actual_view_id = self._model.get_view(view_type="form")["id"]
        self.assertTrue(actual_view_id)

        # Check, that the XML id of the used view is correct
        actual_view_xml_id = (
            self.env["ir.ui.view"].browse(actual_view_id).xml_id
        )
        self.assertEqual(actual_view_xml_id, "estate.estate_property_view_form")

    def assertModelHasAttributeWithType(
        self, attributeName: str, attributeType: fields.MetaField
    ):
        self.assertModelHasAttribute(attributeName)
        self.assertModelAttributeHasType(attributeName, attributeType)

    def assertModelHasAttribute(self, attributeName: str):
        self.assertTrue(
            hasattr(self._model, attributeName),
            f'Field "{attributeName}" is missing from model "{type(self._model).__name__}".',
        )

    def assertModelAttributeHasType(
        self, attributeName: str, attributeType: fields.MetaField
    ):
        self.assertIsInstance(
            self._model._fields[attributeName],
            attributeType,
            f"Actual type is {type(self._model._fields[attributeName])}.",
        )
