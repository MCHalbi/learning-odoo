from odoo import fields, models

class EstateProperty(models.Model):
    _inherit = "estate.property"

    def sell(self):
        return super().sell()
