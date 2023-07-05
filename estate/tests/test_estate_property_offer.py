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


class EstatePropertyOfferTests(TransactionCase):
    def setUp(self):
        super().setUp()
        self._model = self.env["estate.property.offer"]
        self._property_mock = self.env["estate.property"].create(
            {
                "name": "Foo",
                "expected_price": 42,
            }
        )
        self._valid_offer_data = {
            "price": 3.141,
            "status": "accepted",
            "partner_id": 1,
            "property_id": self._property_mock.id,
        }

    def test_create_new_estate_property_offer(self):
        record = self._model.create(self._valid_offer_data)

        self.assertEqual(record.price, self._valid_offer_data["price"])
        self.assertEqual(record.status, self._valid_offer_data["status"])
        self.assertEqual(record.partner_id.id, self._valid_offer_data["partner_id"])
        self.assertEqual(record.property_id.id, self._valid_offer_data["property_id"])

    @mute_logger("odoo.sql_db")
    def test_estate_property_offer_partner_id_is_required(self):
        invalid_offer_data = self._valid_offer_data.copy()
        del invalid_offer_data["partner_id"]

        call = lambda: self._model.create(invalid_offer_data)

        self.assertRaises(NotNullViolation, call)

    @mute_logger("odoo.sql_db")
    def test_estate_property_offer_property_id_is_required(self):
        invalid_offer_data = self._valid_offer_data.copy()
        del invalid_offer_data["property_id"]

        call = lambda: self._model.create(invalid_offer_data)

        self.assertRaises(NotNullViolation, call)
