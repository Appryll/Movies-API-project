# URL configuration for moviesapi project.
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

# Swagger documentation
schema_view = get_schema_view(
    openapi.Info(
        title="Movies API Project",
        default_version='v1',
        description="API REST pour gérer les films.",
        contact=openapi.Contact(email="nataliafabiano.dev@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # urls swagger
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # urls API Movies
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')),
]