#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Ethan'
SITENAME = 'Ethan King'
SITEURL = 'http://localhost:8000'

PATH = 'content'
STATIC_PATHS = ['images', 'pdfs']

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'https://getpelican.com/'),
#          ('Python.org', 'https://www.python.org/'),
#          ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#         )

# Social widget

SOCIAL = (('linkedin', 'https://www.linkedin.com/in/ethan-king'),
          ('github', 'https://github.com/ethan-king'),
          ('twitter', 'https://twitter.com/k1ngethan'),
          )

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = '/Users/ethan/Documents/Projects/github_pages/themes/pelican-blue'

SIDEBAR_DIGEST = 'Data Engineering and Business Intelligence'

FAVICON = '/images/ek_favicon.ico'

DISPLAY_PAGES_ON_MENU = True

TWITTER_USERNAME = 'k1ngethan'

MENUITEMS = (
                # ('About', f'{SITEURL}/about'),
                ('Home', SITEURL),
                ('Resume', f'{SITEURL}/pdfs/Ethan_King_Resume.pdf'),
            )

PROFILE_PICTURE = '/content/images/DSC_0378edit.jpg'