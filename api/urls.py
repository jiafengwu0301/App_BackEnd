from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^accounts/$', views.AccountListView.as_view(), name='Account List'),
    url(r'^accounts/create/$', views.AccountCreateView.as_view(), name='Account Create'),
    url(r'^accounts/(?P<pk>[^/]+)/$', views.AccountRetrieveView.as_view(), name='Account Retrieve'),
    url(r'^accounts/(?P<pk>[^/]+)/update/$', views.UpdateAccountView.as_view(), name='Account Update'),
    url(r'^api-auth/$',views.AccountAuthenticationView.as_view(), name = 'Account Authentication')
]