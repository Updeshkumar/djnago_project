
from django.contrib import admin
from django.urls import path , include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _


urlpatterns = [
    path(_('admin/'), admin.site.urls),
    
]
if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]


urlpatterns += i18n_patterns (
    path('admin/', admin.site.urls),
    path('' , include('account.urls' , namespace="account")) ,
    path('' , include('df_user.urls' , namespace="df_user")) ,
    path('' , include('driver.urls' , namespace="driver")) ,
    path('' , include('labour_contructor.urls' , namespace="labour_contructor")) ,
    path('' , include('sub_contructor.urls' , namespace="sub_contructor")) ,
    path('' , include('vehicle_owner.urls' , namespace="vehicle_owner")),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

