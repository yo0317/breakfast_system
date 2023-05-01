# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date, datetime
from dateutil.relativedelta import relativedelta

class BsProduct(models.Model):
    _name = "bs.product"

    name = fields.Char(string="產品名稱")
    price = fields.Integer(string="售價")

    @api.onchange('raw_material_ids')
    def cost_compute(self):
        for rec in self:
            res = 0
            for rec1 in rec.raw_material_ids:
                res += rec1.cost * rec1.amount
            rec.cost = res


    cost = fields.Integer(string="成本", compute=cost_compute)
    img = fields.Binary(string="圖片")
    is_stop = fields.Boolean(string="是否停售", default=False)



    @api.onchange('raw_material_ids')
    def amount_compute(self):
        for rec in self:
            res = []
            for rec1 in rec.raw_material_ids:
                num = rec1.raw_material_id.amount/rec1.amount
                if num < 1:
                    num = 0
                res.append(num)
            try:
                rec.amount = min(res)
                if min(res) <= 0:
                    rec.is_have = False
                    rec.amount = 0
                else:
                    rec.is_have = True
                    rec.amount = min(res)
            except:
                rec.amount = 0
                rec.is_have = False



    is_have = fields.Boolean(string="是否有原料製作", compute=amount_compute)
    amount = fields.Integer(string="可製作份數", compute=amount_compute)




    raw_material_ids = fields.One2many('bs.product.and.rm', 'product_id', string="原料表")

    def test(self):
        return 123

