from datetime import datetime

project = 'BioTranslator'
copyright = f'{datetime.now():%Y}, BioTranslator team.'
author = 'BioTranslator team'

# -- General configuration ---------------------------------------------------
extensions = ['myst-parser']

templates_path = ['_templates']
master_doc = 'index'
pygments_style = 'sphinx'
exclude_patterns = []

html_theme = 'alabaster'
html_static_path = ['_static']
