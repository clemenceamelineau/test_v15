# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class ProductProduct(models.Model):
    _inherit = 'product.product'
    
    di_transfer = fields.Boolean(string='Product Transfered', default=False)
    
class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    di_transfer = fields.Boolean(string='Product Template Transfered', default=False)
    