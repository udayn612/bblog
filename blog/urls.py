from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/',include('accounts.urls')),
    url(r'^articles/',include('articles.urls')),
    url(r'^about/$',views.about),
    url(r'^$',views.homepage,name='home'),
]

urlpatterns+=staticfiles_urlpatterns()
