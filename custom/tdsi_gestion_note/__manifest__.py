# -*- coding: utf-8 -*-
{
    'name': "tdsi_gestion_note",

    'summary': "Module de gestion de notes de la tdsi",

    'description': """
Ce module permet une gestion facile des notes des etudiants de la TDSI, ainsi que de la generation de
leur releve de notes en pdf 
    """,

    'author': "Amadou BA",
    'website': "https://www.yourcompany.com",

    'application': True,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/tdsi_security.xml',
        'security/ir.model.access.csv',

        #'views/views.xml',
        #'views/templates.xml',

        'views/etudiant.xml',
        'views/evaluation.xml',
        'views/matiere.xml',
        'views/inscription.xml',
        'views/classe.xml',
        'views/tdsi_menu_root.xml',
        'report/releve_etudiant.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

