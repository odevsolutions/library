{
    'name': 'Library Extensions',
    'version': '1.0',
    'author': 'Your Name',
    'depends': ['library', 'contacts'],
   'data': [
    'security/ir.model.access.csv',
    'views/library_book_views.xml',
    'views/library_book_category_views.xml',
],

    'installable': True,
    'application': False,
}
