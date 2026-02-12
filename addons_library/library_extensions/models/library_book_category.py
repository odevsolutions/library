# -*- coding: utf-8 -*-
from odoo import models, fields

class LibraryBookCategory(models.Model):
    _name = "library.book.category"
    _description = "Book Category"

    name = fields.Char(string="Name", required=True)
    # Added to fix error when adding category for adding a book entry.
    color = fields.Integer(
        string="Color Index",
        default=lambda self: random.randint(1, 11)
        )

    _sql_constraints = [
        ('name_unique', 'unique(name)', 'The category name must be unique!')
    ]