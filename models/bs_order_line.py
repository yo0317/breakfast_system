# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date, datetime
from dateutil.relativedelta import relativedelta

class BsOrderLine(models.Model):
    _name = "bs.order.line"

    name = fields.Many2one('bs.product', string="產品名稱")
    price = fields.Integer(string="售價", related='name.price')
    cost = fields.Integer(string="成本", related='name.cost')
    img = fields.Binary(string="圖片", related='name.img')
    is_stop = fields.Boolean(string="是否停售", related='name.is_stop')
    is_have = fields.Boolean(string="是否有原料製作", related='name.is_have')
    amount = fields.Integer(string="可製作份數", related='name.amount')
    buy_amount = fields.Integer(string="購買份數", required=True)
    total = fields.Integer(string="小計", compute='_compute_total')
    order_id = fields.Many2one('bs.order', string="訂單", default=lambda self: self.env.browse(self._context.get('active_id')))



    @api.depends('buy_amount', 'price')
    def _compute_total(self):
        for rec in self:
            rec.total = rec.buy_amount * rec.price