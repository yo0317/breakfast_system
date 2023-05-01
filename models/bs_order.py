# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError, UserError


class BsOrder(models.Model):
    _name = "bs.order"

    name = fields.Char(string="訂單編號", readonly=True)
    order_date = fields.Date(string='日期', default=fields.Date.today, required=True, readonly=True)
    order_user = fields.Many2one('res.users', string='點餐人員', default=lambda self: self.env.uid, required=True)
    order_lines = fields.One2many('bs.order.line', 'order_id', string="訂單明細")
    count = fields.Integer(string="計數")

    def order_checkout(self):
        count = self.env['bs.order'].search(
            [('order_date', '=', datetime.today().strftime('%Y-%m-%d')), ('id', '!=', self.id)], order='count desc', limit=1).count
        if (datetime.today().year - 1911) < 100:
            year = '0' + str(datetime.today().year - 1911)
        else:
            year = str(datetime.today().year - 1911)
        if datetime.today().month < 10:
            month = '0' + str(datetime.today().month)
        else:
            month = str(datetime.today().month)
        if datetime.today().day < 10:
            day = '0' + str(datetime.today().day)
        else:
            day = str(datetime.today().day)
        if count < 10:
            count_1 = '00' + str(count + 1)
        elif count < 100 and count >= 10:
            count_1 = '0' + str(count + 1)
        else:
            count_1 = str(count + 1)
        num = year + month + day + count_1
        for rec in self.order_lines:
            for rec1 in rec.name:
                for rec2 in rec1.raw_material_ids:
                    rec2.raw_material_id.amount -= rec2.amount * rec.buy_amount
                    if rec2.raw_material_id.amount <= 0:
                        raise UserError(_('「%s」原料庫存不足' % (rec.name.name)))
        self.update({
            'name': num,
            'count': count + 1,
            'order_user': self.order_user.id,
        })


    def cancel_order(self):
        for rec in self.order_lines:
            rec.unlink()









