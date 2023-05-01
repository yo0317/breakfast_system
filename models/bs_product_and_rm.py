# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date, datetime
from dateutil.relativedelta import relativedelta

class BsProductAndRm(models.Model):
    _name = "bs.product.and.rm"

    product_id = fields.Many2one('bs.product', string="產品")
    raw_material_id = fields.Many2one('bs.raw.material', string="原料")
    amount = fields.Integer(string="數量", default=1)
    cost = fields.Integer(string="成本", related="raw_material_id.cost")
    last_amount = fields.Integer(string="庫存數量", default=0, related="raw_material_id.amount")






