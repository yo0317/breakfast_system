# _*_ coding: utf-8 _*_

from odoo import api, models

class BsOrderReport(models.AbstractModel):
    _name = 'report.breakfast_system.bs_order_report'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['bs.order'].browse(docids)
        return {
              'doc_ids': docids,
              'docs': docs,
              'data': data,
        }