from odoo import models, fields


class Inscription(models.Model):
    _name = "tdsi_gestion_note.inscription"
    _description = "Inscription d'un etudiant dans une classe"
    _rec_name = "etudiant_id"

    annee_scolaire = fields.Char('Année scolaire', required=True)
    date_inscription = fields.Date("Date d'inscription", default=fields.Date().today())
    etudiant_id = fields.Many2one("tdsi_gestion_note.etudiant", 'Etudiant')

    classe_id = fields.Many2one("tdsi_gestion_note.classe", "Classe")
