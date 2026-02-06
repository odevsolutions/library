from odoo import models, fields, api

class LibraryBook(models.Model):
    _inherit = "library.book"

    author_id = fields.Many2one(
        comodel_name = "res.partner",
        string = "Author"
        required = True
    )

class LibraryBookCategory(models.Model):
        _name = "library.book.category"
        _description = "Book Category"

        name = fields.Char(string="Category Name", required=True, unique=True)

class LibraryBook(models.Model):
    _inherit = "library.book"

    category_id = fields.Many2many(
        comodel_name = "library.book.category",
        string = "Categories"
    )