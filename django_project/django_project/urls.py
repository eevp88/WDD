from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DocDerWeb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    #(r'^admin/',  include(admin.site.urls)), # admin site
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('home.urls')),
    url(r'', include('userprofile.urls')),
    url(r'', include('documentos.urls')),
    
)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
