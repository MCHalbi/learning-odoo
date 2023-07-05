from odoo import api, fields, models, exceptions
from odoo.tools import float_utils


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "An estate property."
    _order = "id desc"

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()

    date_availability = fields.Date(
        copy=False,
        default=lambda self: fields.Date.add(fields.Date.today(), months=3),
    )
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    best_offer = fields.Float(compute="_compute_best_offer")

    active = fields.Boolean(default=True)
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
    total_area = fields.Integer(compute="_compute_total_area")

    property_type_id = fields.Many2one("estate.property.type")
    salesperson_id = fields.Many2one("res.users", default=lambda self: self.env.user)
    buyer_id = fields.Many2one("res.partner", copy=False, readonly=True)
    property_tag_ids = fields.Many2many("estate.property.tag", string="Tags")
    property_offer_ids = fields.One2many("estate.property.offer", "property_id", string="Offers")

    _sql_constraints = [
        (
            "check_expected_price_must_be_positive",
            "CHECK(expected_price > 0)",
            "The expected price must be greater than 0.",
        ),
        (
            "check_selling_price_must_be_positive",
            "CHECK(selling_price > 0)",
            "The selling price must be greater than 0.",
        ),
    ]

    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends("property_offer_ids.price")
    def _compute_best_offer(self) -> None:
        for record in self:
            record.best_offer = max(record.property_offer_ids.mapped("price")) if record.property_offer_ids else 0.0

    @api.onchange("garden")
    def _onchange_garden(self):
        self.garden_area, self.garden_orientation = (10, "N") if self.garden else (None, None)

    def cancel(self) -> bool:
        for estate_property in self:
            if self.state == "sold":
                raise exceptions.UserError("A sold property cannot be cancelled.")

            self.state = "cancelled"

        return True

    def sell(self) -> bool:
        for estate_property in self:
            if self.state == "cancelled":
                raise exceptions.UserError("A cancelled property cannot be sold.")

            self.state = "sold"

        return True

    @api.constrains("selling_price", "expected_price")
    def _check_selling_price_is_high_enough(self) -> None:
        for estate_property in self:
            if estate_property.selling_price == 0.0:
                return

            selling_price_is_too_low = (
                float_utils.float_compare(estate_property.expected_price * 0.9, estate_property.selling_price, precision_digits=2) == 1
            )

            if selling_price_is_too_low:
                raise exceptions.ValidationError("The selling price must be at least 90 % of the expected price.")
