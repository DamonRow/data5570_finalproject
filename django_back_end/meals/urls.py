from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MealViewSet, IngredientViewSet, home_view

router = DefaultRouter()
router.register(r'meals', MealViewSet)
router.register(r'ingredients', IngredientViewSet)

urlpatterns = [
    path('', home_view, name='home'),  # home page still works!
    path('api/', include(router.urls)),  # 👈 this adds /api/meals/ and /api/ingredients/
]
