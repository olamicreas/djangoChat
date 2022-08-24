
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from user import views as user_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('chat.urls') ),
    path('reg/', user_view.register, name='reg'),
    path('home/', user_view.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
