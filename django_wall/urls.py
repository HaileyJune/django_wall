from django.conf.urls import url, include	# added an import!
# from django.contrib import admin              # comment out, or just delete
urlpatterns = [
    url(r'^wall/', include('apps.wall.urls')),	# use your app_name here
    url(r'^', include('apps.login_registration.urls')),	# use your app_name here
    # url(r'^admin/', admin.sites.urls)         # comment out, or just delete
]