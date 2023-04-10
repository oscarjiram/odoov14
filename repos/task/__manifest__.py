{
    'name': 'Módulo de tareas',
    'version': '1.0',
    'description': 'Un módulo básico de Odoo para administrar una lista de tareas.',
    'depends': ['base', 'calendar'],
    'data': [
        'views/task_views.xml',
     #   'security/groups.xml',
        'security/ir.model.access.csv'],

}

