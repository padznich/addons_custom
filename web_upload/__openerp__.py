{
    'name': 'Upload Multi Files',
    'sequence': 5,
    'version': '1.0',
    'summary': 'Upload Multi Files',
    'category': 'Extra Tools',
    'author': 'Bruce',
    'description':
        """
        Made upload multi files, Click Form view any model, Drag files from your local and to browse and drop
,Check Actions buttons , attachment fileds, you can see it.
        """,
    'data': [
        'import/import_js.xml',
    ],
    'depends': [
        'document'
    ],
    'qweb': ['static/src/xml/*.xml'],
    'application': True,
    'price': '0',
    'currency': 'USD',
}