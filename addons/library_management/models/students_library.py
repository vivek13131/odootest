from odoo import api, fields, models


class StudentsDetails(models.Model):
    _name = 'library.management'
    _description = "library Students"

    roll_no = fields.Integer(string='Roll Number')
    name = fields.Char(string='Name')
    address = fields.Text(string='Address')
    mobile_no = fields.Char(string='Mobile Number')
    course = fields.Selection([
        ('information technology','INFOMATION TECHNOLOGY'),
        ('computer Engineering','COMPUTER ENGINEERING'),
    ], string=' Course ')
    product_id= fields.Many2many('library.books',string="product")
