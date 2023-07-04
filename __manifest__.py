# __manifest__.py
{
    'name': "Mi Módulo",
    'version': '1.0',
    'summary': "Resumen de lo que hace tu módulo",
    'description': """Descripción detallada de tu módulo""",
    'category': 'Categoría',
    'author': 'Tu Nombre',
    'website': 'https://www.tuweb.com',
    'depends': ['sale'],  # Dependencia con el módulo 'sale'
    'data': [
        'views/views.xml',  # Archivo que contiene las vistas
    ],
    'installable': True,
    'auto_install': False,
}
