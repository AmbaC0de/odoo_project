from odoo import fields, models


class Matiere(models.Model):
    _name = "tdsi_gestion_note.matiere"
    _description = "Matieres enseignées"
    _rec_name = 'libelle'
    _sql_constraints = [
        ('check_coefficient_positive', 'CHECK(coefficient > 0)', 'Le coefficient doit être strictement positif.'),
        ('check_coefficient_range', 'CHECK(coefficient <= 10)', 'Le coefficient ne peut pas dépasser 10.'),
    ]

    libelle = fields.Char("Libellé", required=True)
    coefficient = fields.Integer("Coefficient", required=True)
    evaluation_ids = fields.One2many('tdsi_gestion_note.evaluation', 'matiere_id', "Evaluation")

