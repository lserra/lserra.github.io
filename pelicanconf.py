#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = 'lserra'
SITEURL = 'https://lserra.github.io'
# SITEURL = 'localhost:8000'
DOMAIN = SITEURL
FEED_DOMAIN = SITEURL
HTTPS = True
SITENAME = 'Good Combination'
SITETITLE = '{ m, d, c }'
SITESUBTITLE = 'Matemática, dados e código'
SITEDESCRIPTION = 'Ideias e reflexões sobre matemática, dados e programação'
SITELOGO = '/images/profile.png'
# FAVICON = '/images/favicon.ico'
ROBOTS = "index, follow"
CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike",
    "version": "4.0",
    "slug": "by-sa"
}
COPYRIGHT_YEAR = datetime.now().year
DISQUS_SITENAME = 'goodcombination'

THEME = 'themes/Flex'
TIMEZONE = 'America/Sao_Paulo'
DEFAULT_LANG = 'pt-BR'
PLUGINS = ['sitemap', 'post_stats', 'feed_summary']

PATH = 'content'
PLUGIN_PATHS = ['./custom-plugins', './pelican-plugins']
STATIC_PATHS = ['images', 'extra']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}

# Code highlighting the theme
PYGMENTS_STYLE = 'monokai'

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'

ARCHIVES_SAVE_AS = 'archives.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_USE_SUMMARY = True
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# HOME_HIDE_TAGS = True

MAIN_MENU = True

LINKS = (
    ('ideias e reflexoes', SITEURL),
    ('portfolio', SITEURL),
)

SOCIAL = (
    # ('envelope', 'mailto:laercio.serra@gmail.com'),
    ('github', 'https://github.com/lserra'),
    ('linkedin','https://www.linkedin.com/in/laerciosserra/'),
    ('x','https://x.com/laercio_serra'),
)

MENUITEMS = (
    ('Arquivos', '/archives'),
    ('Categorias', '/categories'),
    ('Tags', '/tags')
)

DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
