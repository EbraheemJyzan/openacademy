# -*- coding: utf-8 -*-

from odoo import models, fields, api , _


class event_management(models.Model):
    _inherit = 'event.event'

    event = fields.Char(String='event')



class organizer(models.Model):
    _name = 'organizer'

    first_name = fields.Char(String='First_name')
    last_name = fields.Char(String='Last_name')
    phon = fields.Integer(String='Phon')
    email = fields.Char(String='Email')
    mr = fields.Boolean(String='Mr.')
    mrs = fields.Boolean(String='Mrs.')
    event_organizer = fields.Many2one('event.event','event_organizer',)

    
    def hala(self):
        print('uuuuuuuuuuuuuuuuuuuuu')
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

