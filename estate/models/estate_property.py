from odoo import api, fields, models


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "An estate property."

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(
        copy=False,
        default=lambda self: fields.Date.add(fields.Date.today(), months=3),
    )
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        [
            ("N", "North"),
            ("S", "South"),
            ("E", "East"),
            ("W", "West"),
        ]
    )
    active = fields.Boolean(default=False)
    state = fields.Selection(
        selection=[
            ("new", "New"),
            ("offer_received", "Offer Received"),
            ("offer_accepted", "Offer Accepted"),
            ("sold", "Sold"),
            ("cancelled", "Canceled"),
        ],
        required=True,
        copy=False,
        default="new",
    )
    property_type_id = fields.Many2one("estate.property.type")
    salesperson_id = fields.Many2one(
        "res.partner", default=lambda self: self.env.user
    )
    buyer_id = fields.Many2one("res.users", copy=False)
    property_tag_ids = fields.Many2many("estate.property.tag", string="Tags")
    property_offer_ids = fields.One2many(
        "estate.property.offer", "property_id", string="Offers"
    )
    total_area = fields.Integer(compute="_compute_total_area")
    best_offer = fields.Float(compute="_compute_best_offer")

    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends("property_offer_ids.price")
    def _compute_best_offer(self) -> None:
        for record in self:
            record.best_offer = (
                max(record.property_offer_ids.mapped("price"))
                if record.property_offer_ids
                else 0.0
            )
