from odoo import api, fields, models



class Product(models.Model):
    _name='nothing.products'
    
    
    name = fields.Char(string="Name")
    number_of_months = fields.Integer(string="Number of months")

class stafs(models.Model):
    _name = 'nothing.stafs'
    
    
    name = fields.Char(string="Name")

class items(models.Model):
    _name = 'nothing.items'

    product_name = fields.Char(string="product_name")