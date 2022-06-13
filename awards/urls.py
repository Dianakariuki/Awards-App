from . import views
from django.urls import re_path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token


#url urlpatterns

urlpatterns=[
    re_path(r'^$',views.index, name='index'),
    re_path(r'project/post/$',views.post,name='post'),
    re_path(r'^user/profile/$',views.profile,name='profile'),
    re_path(r'^project/(\d+)/',views.project_detail,name='details'),
    re_path(r'^search/projects/results/$',views.search,name="search"),
    re_path(r'^api/projects/$',views.ProjectList.as_view()),
    re_path(r'^api/profile/$',views.ProfileList.as_view()),
    re_path(r'^token/', obtain_auth_token),
    re_path(r'^developer/api/$',views.apiView,name='api'),
    
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
