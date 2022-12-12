# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from _datetime import date, datetime
import time
import logging
import xmlrpc.client

_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    di_transfer = fields.Boolean(string='Transfered', default=False)
    
    def btn_transfer(self):
        _logger.warning('BTN TRANSFERT')
        url = "https://clemenceamelineau-test-v15-staging-6618804.dev.odoo.com"
        db = "clemenceamelineau-test-v15-staging-6618804"
        username = "admin"
        password = "admin"
        
        print('AVANT CONNEXION')
        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url)) 
        
        print('AVANT AUTHENTIFICATION')
        uid = common.authenticate(db, username, password, {}) #Cette ligne qui plante si l'url est en local, fonctionne sur url sur un serveur
        #ConnectionResetError: [WinError 10054] Une connexion existante a dû être fermée par l’hôte distant
        
        print('AVANT REQUEST')
        models = xmlrpc.client.ServerProxy("{}/xmlrpc/2/object".format(url))  
        
        print('APRES REQUEST')
        order_line = models.execute_kw(db, uid, password, 'sale.order', 'search_read', [[['di_transfer', '=', False]]])
        print(order_line)
        
        for line in order_line:
            print(line.get('name'))