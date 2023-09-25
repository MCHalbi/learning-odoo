# -*- coding: utf-8 -*-
{
    "name": "Library Management",
    "summary": """Manage library catalog and book lengding.""",
    "author": "Lukas Halbritter",
    "category": "Services/Library",
    "depends": ["base"],
    "data": [
        "security/library_security.xml",
        "security/ir.model.access.csv",
        "views/library_menu.xml",
    ],
    "application": True,
}
