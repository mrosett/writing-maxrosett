from __future__ import unicode_literals

AUTHOR = 'Max Rosett'
SITENAME = 'Max Rosett'
SITEDESCRIPTION = 'Articles, Essays, and Musings'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

DEFAULT_PAGINATION = 10
DISPLAY_CATEGORIES_ON_MENU = False

THEME = '/Users/maxrosett/Github/medius'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
