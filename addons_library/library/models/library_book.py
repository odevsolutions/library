# -*- coding: utf-8 -*-
from odoo import models, fields

class LibraryBook(models.Model):
    _name = "library.book"
    _description = "Book"
    _order = "name"

    name = fields.Char(string="Name", required=True)
    isbn_13 = fields.Char(string="ISBN 13", required=True)
    author_id = fields.Many2one(
        'res.partner',
        string='Author',
        domain=[('is_company', '=', False)]
    )
    category_id = fields.Many2one(
        'library.book.category',
        string='Category'
    )
