# -*- coding: utf-8 -*-
# from odoo import http


# class PwWhTransit(http.Controller):
#     @http.route('/pw_wh_transit/pw_wh_transit', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pw_wh_transit/pw_wh_transit/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pw_wh_transit.listing', {
#             'root': '/pw_wh_transit/pw_wh_transit',
#             'objects': http.request.env['pw_wh_transit.pw_wh_transit'].search([]),
#         })

#     @http.route('/pw_wh_transit/pw_wh_transit/objects/<model("pw_wh_transit.pw_wh_transit"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pw_wh_transit.object', {
#             'object': obj
#         })
