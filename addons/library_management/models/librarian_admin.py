from odoo import api, fields, models


class Library(models.Model):
    _name = 'library.admin'

    name_id = fields.Many2one('library.management',string="Studentname")
