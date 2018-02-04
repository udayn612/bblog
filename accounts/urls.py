from django.conf.urls import url,patterns
from django.contrib.auth import views as auth_views
from .import views


app_name='accounts'

urlpatterns=[
        url(r'^signup/$',views.signup_view,name="signup"),
        url(r'^success/$',views.register_success,name="success"),
        url(r'^login/$',views.login_view,name="login"),
        url(r'^logout/$',views.logout_view,name="logout"),
        url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
        url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
        url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
        url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),

]
