
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token_refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token_verify/', TokenVerifyView.as_view(), name='token_verify'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)