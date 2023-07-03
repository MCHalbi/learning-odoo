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


class EstatePropertyTagTests(TransactionCase):
    def setUp(self):
        self._model = self.env["estate.property.tag"]

    def test_create_new_estate_property_type(self):
        record = self._model.create({"name": "cozy"})
        self.assertEqual(record.name, "cozy")

    @mute_logger("odoo.sql_db")
    def test_estate_property_type_name_is_required(self):
        call = lambda: self._model.create({"name": None})
        self.assertRaises(NotNullViolation, call)
