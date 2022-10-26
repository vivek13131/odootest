from odoo import api, fields, models


class BooksDeatil(models.Model):
    _name = 'library.books'
    _description = "library books"

    isbn = fields.Char(string="ISBN_no")
    author_id = fields.Many2one('library.author',string="Author",)
    book_reference= fields.Text(string="Book Reference")
    name = fields.Char(string="Name")
    edition_mark = fields.Char(string="Edition Mark")
    date_of_publication = fields.Date(string="Date of Publication")
    volume_number = fields.Integer(string="Volume_numbers")
    publication = fields.Char(string="Publication")
    category = fields.Selection([(
        'noval','Noval'),
        ('fiction','Fiction'),
        ('documentary','ocumentary'),
        ('documentary','Documentary'),
    ],string="Category")
    img = fields.Binary(string="image")
    status = fields.Boolean(string="Available")
    student_id = fields.Many2one('library.management',string="Studentname")

