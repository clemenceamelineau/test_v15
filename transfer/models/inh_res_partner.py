# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    di_transfer = fields.Boolean(string='Partner Transfered', default=False)