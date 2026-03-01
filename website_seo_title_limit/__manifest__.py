# -*- coding: utf-8 -*-
{
    'name': 'Website SEO Title Limit',
    'version': '16.0.1.0.0',
    'summary': 'Restrict website meta title length to 160 characters across all pages',
    'description': 'Overrides the global SEO metadata mixin to cap the meta title at 160 characters.\nThis is provided as a standalone module so it can be installed independently of other SEO kits.',
    'author': 'Custom',
    'category': 'Website',
    'depends': ['website'],
    'data': [
        'views/seo_metadata_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'AGPL-3',
}