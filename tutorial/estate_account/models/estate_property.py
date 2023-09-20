from odoo import fields, models, Command


class EstateProperty(models.Model):
    _inherit = "estate.property"

    def sell(self):
        result = super().sell()
        journal = self.env["account.journal"].search([("type", "=", "sale")], limit=1)

        for estate_property in self:
            self.env["account.move"].create(
                {
                    "partner_id": estate_property.buyer_id.id,
                    "move_type": "out_invoice",
                    "journal_id": journal.id,
                    "invoice_line_ids": [
                        Command.create(
                            {
                                "name": estate_property.name,
                                "quantity": 1.0,
                                "price_unit": estate_property.selling_price * 6.0 / 100,
                            }
                        ),
                        Command.create(
                            {
                                "name": "Administrative fees",
                                "quantity": 1.0,
                                "price_unit": 100.00,
                            }
                        ),
                    ],
                }
            )

        return result
