from odoo import api, fields, models


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "An estate property offer."

    price = fields.Float(string="Price")
    status = fields.Selection(
        selection=[("accepted", "Accepted"), ("refused", "Refused")],
        copy=False,
        string="Status",
    )
    partner_id = fields.Many2one("res.partner", required=True, string="Partner")
    property_id = fields.Many2one("estate.property", required=True)
    validity = fields.Integer(default=7, string="Validity (days)")
    date_deadline = fields.Date(
        compute="_compute_date_deadline",
        inverse="_compute_validity",
        string="Deadline",
    )

    @api.depends("validity", "create_date")
    def _compute_date_deadline(self):
        for offer in self:
            offer.date_deadline = fields.Date.add(
                offer.create_date, days=offer.validity
            )

    @api.depends("date_deadline", "create_date")
    def _compute_validity(self):
        for offer in self:
            offer.validity = (
                offer.date_deadline - offer.create_date.date()
            ).days
