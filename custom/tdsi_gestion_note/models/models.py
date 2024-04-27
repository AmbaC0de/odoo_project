# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class tdsi_gestion_note(models.Model):
#     _name = 'tdsi_gestion_note.tdsi_gestion_note'
#     _description = 'tdsi_gestion_note.tdsi_gestion_note'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

