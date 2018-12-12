from django.urls import path, include
from apps.core.views import UserViewSet, MagViewSet, ProdViewSet

urlpatterns = [
    path('Users/', UserViewSet.as_view()),
    path('universities/', MagViewSet.as_view()),
    path('faculties/', ProdViewSet.as_view()),
    path('frontend/', include('frontend.urls'))
]

# router.register(r'Users', UserViewSet)
# router.register(r'universities', MagViewSet)
# router.register(r'faculties', ProdViewSet)

app_name = 'core'

# urlpatterns = router.urls