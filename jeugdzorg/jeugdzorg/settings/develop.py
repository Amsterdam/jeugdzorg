from .base import *

DEBUG = True

CRONJOBS = [
    ('*/1 * * * *', 'jeugdzorg.cron.update_regeling_bron_job', '>> /var/log/scheduled_job.log 2>&1')
]

try:
    from .local import *
except ImportError:
    pass
