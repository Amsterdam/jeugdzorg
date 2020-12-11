from django.core.management.base import BaseCommand, CommandError
from jeugdzorg.models import Profiel
from django.core.cache import cache
from django.utils import timezone
import datetime
from dateutil.tz import tzlocal
from jeugdzorg.utils import update_profiel_cards


class Command(BaseCommand):
    name = 'render_profile_cards'
    help = 'render_profile_cards'

    def handle(self, *args, **options):
        update_profiel_cards([p for p in Profiel.objects.filter(profile_rendered__isnull=True)])