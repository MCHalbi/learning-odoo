from odoo import fields, models


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "An estate property type."

    name = fields.Char(required=True)

    _sql_constraints = [
        (
            "check_name_must_be_unique",
            "UNIQUE(name)",
            "The name of a property type must be unique.",
        ),
    ]
