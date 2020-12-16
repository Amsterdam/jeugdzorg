from django.core.management import CommandError
from django.contrib.auth import (get_user_model, )
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.contrib.sites.models import Site
from django.conf import settings
import sendgrid
from sendgrid.helpers.mail import Mail
from jeugdzorg.statics import *
from jeugdzorg.utils import *
from jeugdzorg.context_processors import app_settings
from django.template.loader import render_to_string
from django.core.cache import cache
import datetime
from dateutil.tz import tzlocal

UserModel = get_user_model()


def get_users():
    """Given an email, return matching user(s) who should receive a reset.

    This allows subclasses to more easily customize the default policies
    that prevent inactive users and users with unusable passwords from
    resetting their password.
    """
    active_users = UserModel._default_manager.filter(**{
        'is_active': True,
    }).exclude(profiel=None)
    return (u for u in active_users if u.has_usable_password())


class Command(BaseCommand):
    help = 'mail_account_active_check'
    name = 'mail_account_active_check'

    def handle(self, *args, **options):
        sg = sendgrid.SendGridAPIClient(settings.SENDGRID_API_KEY)
        now = datetime.datetime.now(tzlocal())
        if get_container_id() != cache.get(get_cronjob_worker_cache_key()):
            raise CommandError("You're not the worker!")
        print('%s: %s' % (now.strftime('%Y-%m-%d %H:%M'), self.__module__.split('.')[-1]))
        site = Site.objects.get_current()
        if site.instelling:
            subject = 'VraagMij - Is je profiel up-to-date?'

            for u in get_users():
                if u.profiel.hou_me_op_de_hoogte_mail:
                    o = {
                        'naam': u.profiel.naam_volledig,
                        'profiel': u.profiel,
                    }
                    o.update(app_settings())

                    body = render_to_string('email/mail_account_active_check.txt',  o)
                    body_html = render_to_string('email/mail_account_active_check.html', o)

                    mail = Mail(
                        from_email=('noreply@%s' % site.domain, 'VraagMij'),
                        to_emails=(u.email, u.profiel.naam_volledig),
                        subject=subject,
                        plain_text_content=body,
                        html_content=body_html,
                    )

                    if settings.ENV != 'develop':
                        try:
                            response = sg.send(mail)
                            print(response.status_code)
                            print(response.body)
                            print(response.headers)
                        except Exception as e:
                            print(e.message)
                    else:
                        print(body)


