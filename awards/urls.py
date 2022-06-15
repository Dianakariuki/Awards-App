from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth import views as auth_views




urlpatterns=[
    path('',views.index, name='index'),
    path('project/post/',views.post,name='post'),
    path('profile/',views.profile,name='profile'),
    path('project/<int:project_id>',views.project_detail,name='details'),
    path('search/projects/results/',views.search,name="search"),
    path('api/projects/',views.ProjectList.as_view()),
    path('api/profile/',views.ProfileList.as_view()),
    path('token/', obtain_auth_token),
    path('developer/api/',views.apiView,name='api'),
    path('register/',views.register,name="register"),
    # path('login/',views.login_user,name="login"),
    # path('logout/', auth_views.logout_then_login),
    path( 'login/',auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    # path( 'logout/',auth_views.LogoutView.as_view(template_name="registration/logout.html"), name="logout"),
    
    
    
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
