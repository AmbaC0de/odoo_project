from odoo import models, fields, api


class Classe(models.Model):
    _name = "tdsi_gestion_note.classe"
    _description = "La classe d'un etudiant"
    _rec_name = "nom_niveau"

    niveau = fields.Selection(
        [
            ('licence1', 'Licence 1'),
            ('licence2', 'Licence 2'),
            ('licence3', 'Licence 3'),
            ('master1', 'Master 1'),
            ('master2', 'Master 2'),
        ],
        "Niveau"
    )

    nom = fields.Char("Nom", required=True)

    inscription_ids = fields.One2many(
        "tdsi_gestion_note.inscription",
        "classe_id",
        "Inscription"
    )

    nom_niveau = fields.Char(compute='_compute_nom_niveau')

    # Définit le nom complet comme combinaison de nom et niveau
    @api.depends('nom', 'niveau')
    def _compute_nom_niveau(self):
        for record in self:
            record.nom_niveau = f"{record.niveau} {record.nom}"

