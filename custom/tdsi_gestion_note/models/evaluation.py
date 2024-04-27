from odoo import models, fields


class Evaluation(models.Model):
    _name = "tdsi_gestion_note.evaluation"
    _description = "Différents type d'évaluations"
    _rec_name = 'etudiant_id'
    _sql_constraints = [
        ('check_note_positive', 'CHECK(0 < note)', 'La note doit être positive.'),
        ('check_note_range', 'CHECK(note <= 20)', 'La note ne peut pas dépasser 20.')
    ]

    note = fields.Integer("Note", required=True)
    semestre = fields.Selection(
        [('semestre1', 'Semestre 1'), ('semestre2', 'Semestre 2')],
        "Semestre"
    )
    session = fields.Selection(
        [('normale', 'Normale'), ('rattrapage', 'Rattrapage')],
        "Session"
    )

    etudiant_id = fields.Many2one('tdsi_gestion_note.etudiant', 'Etudiant')
    matiere_id = fields.Many2one('tdsi_gestion_note.matiere', 'Matière')



