# Author: Lukas Halbritter <halbi93@gmx.de>
# Copyright 2023
# pylint: disable=missing-docstring
import unittest
from odoo import fields
from odoo.tools import mute_logger
from odoo.tests.common import TransactionCase
from psycopg2.errors import NotNullViolation
from lxml import html
from typing import Dict


class EstatePropertyTypeTests(TransactionCase):
    def setUp(self):
        self._model = self.env["estate.property.type"]

    def test_create_new_estate_property_type(self):
        record = self._model.create({"name": "foobar"})
        self.assertEqual(record.name, "foobar")

    @mute_logger("odoo.sql_db")
    def test_estate_property_type_name_is_required(self):
        call = lambda: self._model.create({"name": None})
        self.assertRaises(NotNullViolation, call)

    def test_estate_property_type_tree_has_desired_columns(self):
        tree_view = self.get_tree_view_for_model("estate.property.type")
        architecture = tree_view["arch"]
        architecture_xpath = html.fromstring(architecture)

        column_names = [
            field.get("name")
            for field in architecture_xpath.xpath("//tree/field")
        ]

        expected_column_names = ["sequence", "name"]

        self.assertListEqual(column_names, expected_column_names)

    def get_tree_view_for_model(self, model_name: str) -> Dict:
        return self._get_view_for_model(model_name, "tree")

    def _get_view_for_model(self, model_name: str, view_type: str) -> Dict:
        model = self.env[model_name]
        return model.get_view(view_type=view_type)
