from odoo import api, fields, models


class author(models.Model):
    _name = 'library.author'
    _description = 'author library'

    name = fields.Char(string="Authorname")
    date_of_birth = fields.Date(string="DOB")
    awards = fields.Text(string="Awards")
    biography = fields.Text(string="Biography")
    image = fields.Binary(string="Image")
    Books_ids = fields.Many2many('library.books',string="Books")

