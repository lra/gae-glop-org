import os
from google.appengine.ext.webapp import template
from django.http import HttpResponse
from random import choice
from urllib import quote_plus


def index(request):
    fonts = [
        'Cantarell',
        'Cardo',
        'Crimson Text',
        'Droid Sans',
        'Droid Sans Mono',
        'Droid Serif',
        'IM Fell DW Pica',
        'Inconsolata',
        'Josefin Sans Std Light',
        'Lobster',
        'Molengo',
        'Nobile',
        'OFL Sorts Mill Goudy TT',
        'Old Standard TT',
        'Reenie Beanie',
        'Tangerine',
        'Vollkorn',
        'Yanone Kaffeesatz',
    ]
    font = choice(fonts)
    template_values = {
        'font': font,
        'url_encoded_font': quote_plus(font),
    }
    path = os.path.join(os.path.dirname(__file__), 'index.html')

    return HttpResponse(template.render(path, template_values))
