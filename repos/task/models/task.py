from odoo import models, fields

class Task(models.Model):
    _name = 'task'
    _description = 'Tarea'

    name = fields.Char('Nombre', required=True)
    description = fields.Text('Descripción')
    deadline = fields.Date('Fecha límite')
    completed = fields.Boolean('Completado', default=False)
