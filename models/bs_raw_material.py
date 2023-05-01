# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date, datetime
from dateutil.relativedelta import relativedelta

class BsRawMaterial(models.Model):
    _name = "bs.raw.material"

    name = fields.Char(string="原料品名")
    cost = fields.Integer(string="成本")
    is_stop = fields.Boolean(string="是否停售", default=False)
    is_have = fields.Boolean(string="是否有庫存", default=True, compute='_is_have')
    amount = fields.Integer(string="庫存數量")
    product_ids = fields.One2many("bs.product.and.rm", 'raw_material_id', string="產品", readonly=True)


    def _is_have(self):
        for rec in self:
            if rec.amount <= 0:
                rec.is_have = False
            else:
                rec.is_have = True


