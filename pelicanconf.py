#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Shu'
SITENAME = 'You Know Nothing'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'
DATE_FORMATS = {
	'zh_CN':'%Y-%m-%d %H:%M:%S',
}
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
DEFAULT_DATE = 'fs'


DEFAULT_LANG = 'zh'

FILENAME_METADATA = '(?P<slug>.*)'

TEMPLATE_PAGES = {"/Users/xususu/pelican-themes/my-elegant/templates/search.html" : "search.html", "/Users/xususu/pelican-themes/my-elegant/templates/404.html" : "404.html"}

THEME = "/Users/xususu/pelican-themes/my-elegant"
TYPOGRIFY = False
STATIC_PATHS = ['images','pdfs']
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PLUGIN_PATHS = ["/Users/xususu/pelican-plugins"]
PLUGINS = ['multi_neighbors', 'tipue_search', 'sitemap']

# DISQUS_SITENAME = "xutree"

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10
USE_FOLDER_AS_CATEGORY = False
DISPLAY_PAGES_ON_MENU = False
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

ARTICLE_URL = 'pages/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'pages/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

## 配置sitemap 插件
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.7,
        "indexes": 0.5,
        "pages": 0.3,
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly",
    }
}

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}