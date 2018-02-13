"""jeugdzorg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('', RegelingList.as_view(), name='regelingen'),
    path('regeling-maken/', RegelingCreate.as_view(), name='create_regeling'),
    path('regeling/<int:pk>/', RegelingUpdate.as_view(), name='update_regeling'),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
    path('admin/', admin.site.urls),
    path('admin/dumpjeugdzorg/', dump_jeugdzorg, name='dumpjeugdzorg'),
    path('admin/loadjeugdzorg/', load_jeugdzorg, name='loadjeugdzorg'),
]

urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)