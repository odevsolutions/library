# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LibraryBook(models.Model):
    ######################
    # Private attributes #
    ######################
    _name = "library.book"
    _description = "Book"
    _order = "name"

    ###################
    # Default methods #
    ###################
    name = fields.Char(string="Name",
                       required=True)
    isbn_13 = fields.Char(string="ISBN 13",
                          required=True)

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
