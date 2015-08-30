import os,sys
app_root = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(app_root, 'BeautifulSoup-3.2.1'))
sys.path.insert(0, os.path.join(app_root, 'djangorestframework-0.4.0'))
sys.path.insert(0, os.path.join(app_root, 'requests-2.2.1'))
sys.path.insert(0, os.path.join(app_root, 'South-1.0.2'))
sys.path.insert(0, os.path.join(app_root, 'django-grappelli'))
sys.path.insert(0, os.path.join(app_root, 'django-filebrowser'))
sys.path.insert(0, os.path.join(app_root, 'URLObject-2.4.0'))
sys.path.insert(0, os.path.join(app_root, 'django-groundwork'))
sys.path.insert(0, os.path.join(app_root, 'py-oauth2'))

import sae
from reservation import wsgi

application = sae.create_wsgi_app(wsgi.application)
