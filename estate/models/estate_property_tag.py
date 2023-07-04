from odoo import fields, models


class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "An estate property tag."

    name = fields.Char(required=True)

    _sql_constraints = [
        (
            "check_name_must_be_unique",
            "UNIQUE(name)",
            "The name of a property tag must be unique.",
        ),
    ]
