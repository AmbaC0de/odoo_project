from odoo import models, fields, api


class Etudiant(models.Model):
    _name = "tdsi_gestion_note.etudiant"
    _description = "Etudiants du labo TDSI"
    _rec_name = 'nom_complet'

    _sql_constraints = [
        ('unique_matricule',
         "unique(numero_carte_etudiant)",
         "Carte d'étudiant déjà utilisée déjà utilisé"),
    ]

    prenom = fields.Char("Prénom", required=True)
    nom = fields.Char("Nom", required=True)
    date_de_naissance = fields.Date("Date de naissance", default=fields.Date().from_string('2000-01-01'))
    numero_carte_etudiant = fields.Char("Numéro de carte d'étudiant")
    nom_complet = fields.Char(compute="_compute_nom_compet")
    moyenne_semestre_1 = fields.Char("Moyenne", compute="_compute_moyenne_sem_1", store=True)
    moyenne_semestre_2 = fields.Char("Moyenne", compute="_compute_moyenne_sem_2", store=True)

    evaluation_ids = fields.One2many(
        'tdsi_gestion_note.evaluation',
        'etudiant_id',
        'Evaluations',
        #readonly=True
    )

    inscription_ids = fields.One2many(
        'tdsi_gestion_note.inscription',
        'etudiant_id',
    )

    # Définit le nom complet d'un etudiant
    @api.depends('prenom', 'nom')
    def _compute_nom_compet(self):
        for record in self:
            if record.nom or record.prenom:
                record.nom_complet = f"{record.prenom} {record.nom}"
            else:
                record.nom_complet = ""

    @api.depends("evaluation_ids.note", "evaluation_ids.matiere_id.coefficient", "evaluation_ids.semestre")
    def _compute_moyenne_sem_1(self):
        for record in self:
            notes_by_coeff = sum(
                evaluation.note * evaluation.matiere_id.coefficient
                for evaluation in record.evaluation_ids
                if evaluation.semestre == "semestre1"
            )
            sum_coeff = sum(
                evaluation.matiere_id.coefficient
                for evaluation in record.evaluation_ids
                if evaluation.semestre == "semestre1"
            )

            if sum_coeff:
                record.moyenne_semestre_1 = notes_by_coeff / sum_coeff
            else:
                record.moyenne_semestre_1 = 0.0  # Évitez la division par zéro

    def _compute_annee_scolaire(self):
        annee_scolaire = []
        for record in self:
            annee_scolaire.append(record.annee_scolaire)
        print("annee  scolaire: ", annee_scolaire)
        return annee_scolaire

    @api.depends("evaluation_ids.note", "evaluation_ids.matiere_id.coefficient", "evaluation_ids.semestre")
    def _compute_moyenne_sem_2(self):
        for record in self:
            notes_by_coeff = sum(
                evaluation.note * evaluation.matiere_id.coefficient
                for evaluation in record.evaluation_ids
                if evaluation.semestre == "semestre2"
            )
            sum_coeff = sum(
                evaluation.matiere_id.coefficient
                for evaluation in record.evaluation_ids
                if evaluation.semestre == "semestre2"
            )

            if sum_coeff:
                record.moyenne_semestre_2 = notes_by_coeff / sum_coeff
            else:
                record.moyenne_semestre_2 = 0.0  # Évitez la division par zéro