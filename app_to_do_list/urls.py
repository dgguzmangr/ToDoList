"""
URL configuration for app_to_do_list project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from rest_framework.authtoken import views
from authApp.views import appView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="API for To do List",
        contact=openapi.Contact(email="dgguzmangr@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # JWT token urls
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Token authentication
    path('api/token-auth/', views.obtain_auth_token),

    # Login
    path('api/login/', appView.login),

    # project urls
    path('show_projects/', appView.show_projects),
    path('create_project/', appView.create_project),
    path('update_project/<int:pk>/', appView.update_project),
    path('delete_project/<int:pk>/', appView.delete_project),

    # task urls
    path('show_tasks/', appView.show_tasks),
    path('create_task/', appView.create_task),
    path('update_task/<int:pk>/', appView.update_task),
    path('delete_task/<int:pk>/', appView.delete_task),

    # subtask urls
    path('show_subtasks/', appView.show_subtasks),
    path('create_subtask/', appView.create_subtask),
    path('update_subtask/<int:pk>/', appView.update_subtask),
    path('delete_subtask/<int:pk>/', appView.delete_subtask),

    # person urls
    path('show_persons/', appView.show_persons),
    path('create_person/', appView.create_person),
    path('update_person/<int:pk>/', appView.update_person),
    path('delete_person/<int:pk>/', appView.delete_person),

    # token
    path('generate_token/', views.obtain_auth_token),

    #login
    path('login/', appView.login),
]

# http://localhost:8000/swagger/