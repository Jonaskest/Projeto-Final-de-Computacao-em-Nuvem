# api/index.py
import os
import sys

from django.core.wsgi import get_wsgi_application

# Adiciona o diretório do projeto ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Projeto_django.settings')

app = get_wsgi_application()
