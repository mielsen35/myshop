from django.urls import path
from . import views
from . import webhooks
from django.utils.translation import gettext_lazy as _

app_name = 'payment'

urlpatterns = [
    path(_('process/'), views.payment_process, name='process'),
    path(_('done/'), views.payment_completed, name='done'),
    path(_('canceled/'), views.payment_canceled, name='canceled'),
]
