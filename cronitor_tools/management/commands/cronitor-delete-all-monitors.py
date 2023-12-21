import requests
from requests.auth import HTTPBasicAuth

from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    def handle(self, *args, **options):
        monitors_url = 'https://cronitor.io/api/monitors'
        response = requests.get(
            monitors_url,
            auth=HTTPBasicAuth(settings.CRONITOR_API_KEY, '')
        )

        for monitor in response.json().get('monitors', []):
            url = f'https://cronitor.io/api/monitors/{monitor["key"]}'
            response = requests.delete(url, auth=HTTPBasicAuth(settings.CRONITOR_API_KEY, ''))
