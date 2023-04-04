from odoo import models, fields


class Task(models.Model):
    _name = 'tarea.prueba'
    _description = 'Tarea'

    name = fields.Char('Nombre', required=True)
    description = fields.Text('Descripción')
    deadline = fields.Date('Fecha límite')
    completed = fields.Boolean('Completado', default=False)
    duration = fields.Integer(string='Duración de la tarea (min)')
    user_id = fields.Many2one('res.users', string='Asignado a')
    state = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('progreso', 'En Progreso'),
        ('pausada', 'Pausada'),
        ('finalizada', 'Finalizada'),
    ], default='pendiente')

    def action_iniciar(self):
        self.write({'state': 'progreso'})

    def action_pausar(self):
        self.write({'state': 'pausada'})

    def action_finalizar(self):
        self.write({'state': 'finalizada'})


class ResUsers(models.Model):
    _inherit = 'res.users'

    task_ids = fields.One2many('tarea.prueba', 'user_id', string='Tareas')
