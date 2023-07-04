from odoo import api, fields, models, exceptions


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

    _sql_constraints = [
        (
            "check_price_must_be_positive",
            "CHECK(price > 0)",
            "The offer price must be greater than 0.",
        ),
    ]

    @api.depends("validity", "create_date")
    def _compute_date_deadline(self):
        for offer in self:
            if not offer.create_date:
                offer.create_date = fields.Datetime.now()

            offer.date_deadline = fields.Date.add(
                offer.create_date, days=offer.validity
            )

    @api.depends("date_deadline", "create_date")
    def _compute_validity(self):
        for offer in self:
            if not offer.create_date:
                offer.create_date = fields.Datetime.now()

            offer.validity = (
                offer.date_deadline - offer.create_date.date()
            ).days

    def action_accept(self) -> bool:
        for offer in self:
            if any(
                offer_for_property.status == "accepted"
                for offer_for_property in offer.property_id.property_offer_ids
            ):
                raise exceptions.UserError("Only one offer can be accepted.")

            offer.status = "accepted"
            offer.property_id.buyer_id = offer.partner_id
            offer.property_id.selling_price = offer.price

        return True

    def action_refuse(self) -> bool:
        for offer in self:
            offer.status = "refused"

        return True
