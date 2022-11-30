# -*- coding: utf-8 -*-
# from odoo import http


# class Upobebe(http.Controller):
#     @http.route('/upobebe/upobebe', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/upobebe/upobebe/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('upobebe.listing', {
#             'root': '/upobebe/upobebe',
#             'objects': http.request.env['upobebe.upobebe'].search([]),
#         })

#     @http.route('/upobebe/upobebe/objects/<model("upobebe.upobebe"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('upobebe.object', {
#             'object': obj
#         })
