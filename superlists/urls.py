from django.conf.urls import include, url
# from django.contrib import admin

from lists import urls as list_urls

urlpatterns = [
    url(r'^$', 'lists.views.home_page', name='home'),
    url(r'^lists/', include(list_urls)),
    # url(r'^admin/', include(admin.site.urls)),
]
