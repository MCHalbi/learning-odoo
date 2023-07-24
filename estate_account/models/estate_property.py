from odoo import fields, models


class EstateProperty(models.Model):
    _inherit = "estate.property"

    def sell(self):
        result = super().sell()
        journal = self.env["account.journal"].search(
            [("type", "=", "sale")], limit=1
        )

        for estate_property in self:
            invoice_data = {
                "partner_id": estate_property.buyer_id.id,
                "move_type": "out_invoice",
                "journal_id": journal.id,
            }
            print(invoice_data)

            self.env["account.move"].create(invoice_data)

        return result
