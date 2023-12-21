import cronitor

from django.core.management.base import BaseCommand
from django.conf import settings

from cronitor_config_decorator import discover_cronitor_tasks


class Command(BaseCommand):
    def handle(self, *args, **options):

        cronitor_jobs = discover_cronitor_tasks('core.celery.tasks')
        cronitor_job_defaults = getattr(settings, 'CRONITOR_JOB_DEFAULTS', {})
        cronitor_checks = getattr(settings, 'CRONITOR_CHECKS', [])
        cronitor_check_defaults = getattr(settings, 'CRONITOR_CHECK_DEFAULTS', {})

        cronitor.api_key = settings.CRONITOR_API_KEY

        monitors = []
        for job in cronitor_jobs:
            job.update(cronitor_job_defaults)
            monitors.append(job)

        for check in cronitor_checks:
            check.update(cronitor_check_defaults)
            monitors.append(check)

        monitors = cronitor.Monitor.put(monitors)
