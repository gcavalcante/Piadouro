from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #Piados and home page
    url(r'^$', 'piadouro_website.views.home', name='home'),     
    url(r'^mypiados/$', 'piadouro_website.views.mypiados', name='mypiados'),        
    url(r'^newpiado/$', 'piadouro_website.views.piado_add', name='new_piado'),    
    #Users pages
    url(r'^users/$', 'piadouro_website.views.users', name='users'),    
    url(r'^users/(?P<username>\w+)/','piadouro_website.views.profile',name='profile'),
    #Login/Logout
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'admin/login.html'},name="my_login"),
    url(r'^logout$', 'django.contrib.auth.views.logout', {'template_name': 'piadouro_website/home.html'},name="my_logout"),
    
    #Admin
    url(r'^admin/', include(admin.site.urls)),
)
