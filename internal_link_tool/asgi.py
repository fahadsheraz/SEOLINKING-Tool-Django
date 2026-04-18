import os
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "internal_link_tool.settings")
application = get_asgi_application()
