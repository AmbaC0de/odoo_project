# -*- coding: utf-8 -*-
# from odoo import http


# class TdsiGestionNote(http.Controller):
#     @http.route('/tdsi_gestion_note/tdsi_gestion_note', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tdsi_gestion_note/tdsi_gestion_note/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tdsi_gestion_note.listing', {
#             'root': '/tdsi_gestion_note/tdsi_gestion_note',
#             'objects': http.request.env['tdsi_gestion_note.tdsi_gestion_note'].search([]),
#         })

#     @http.route('/tdsi_gestion_note/tdsi_gestion_note/objects/<model("tdsi_gestion_note.tdsi_gestion_note"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tdsi_gestion_note.object', {
#             'object': obj
#         })

