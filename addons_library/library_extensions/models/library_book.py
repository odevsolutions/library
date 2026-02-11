# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LibraryBook(models.Model):
    _inherit = "library.book"

    # Task 2: Added Author field
    author_id = fields.Many2one(
        'res.partner', 
        string="Author", 
        required=True
    )

    # Task 3: Added Category field
    category_ids = fields.Many2many(
        'library.book.category', 
        string="Categories"
    )

    ######################
    # Fields declaration #
    ######################

    ##############################
    # Compute and search methods #
    ##############################

    ############################
    # Constrains and onchanges #
    ############################

    #########################
    # CRUD method overrides #
    #########################

    ##################
    # Action methods #
    ##################

    ####################
    # Business methods #
    ####################
