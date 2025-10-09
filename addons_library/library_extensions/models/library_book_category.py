# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LibraryBookCategory(models.Model):
    _name = "library.book.category"
    _description = "Book Category"
    _order = "name"

    name = fields.Char(string="Category Name", required=True)

    _sql_constraints = [
        ('unique_category_name', 'unique(name)', 'Category name must be unique!')
    ]
