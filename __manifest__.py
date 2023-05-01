

{
    'name': '我的早餐店',
    'summary': 'Odoo16 Breakfast system',
    'version': '1.0.0',
    'license': "AGPL-3",
    'author': 'Yo',
    "application": True,
    "category": "My application/Breakfast System",

    'depends': [
        'base',
    ],
    'excludes': [
    ],
    'data': [
        'report/bs_order_report.xml',
        'views/bs_raw_material.xml',
        'views/bs_product.xml',
        'views/bs_product_and_rm.xml',
        'views/bs_order.xml',
        'views/bs_order_line.xml',
        'views/menu.xml',
        'security/ir.model.access.csv',

    ],
    'assets': {
            'web.assets_backend': [
                'breakfast_system/static/src/css/style.css']},
    'installable': True,

    'images': [
        'static/description/icon.png',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
