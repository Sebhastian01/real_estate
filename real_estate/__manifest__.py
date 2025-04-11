{
    'name': 'Real Estate',
    'version': '1.0.1',
    'depends': ['base'],
    'category': 'Custom',  # Puedes poner una categoría que tenga más sentido en tu caso
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_menus.xml',
        'views/audio_note_views.xml',
    ],
    'application': True,
    'installable': True,
}
