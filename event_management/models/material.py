# -*- coding: utf-8 -*-

from odoo import models, fields, api , _


class Material(models.Model):
    _name = 'material'
    _description = 'material'

    name = fields.Char()
    type_equipment = fields.Selection([('sound_equipment', 'Sound Equipment'), ('projection_equipment', 'Projection Equipment')])
    description = fields.Char()


