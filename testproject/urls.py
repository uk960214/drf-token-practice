from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from testapp import views
from rest_framework.authtoken import views as authViews

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', authViews.obtain_auth_token),
    path('signup/', views.SignupView.as_view()),
    path('login/', views.LoginView.as_view()),
]