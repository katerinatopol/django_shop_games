from django.urls import path, include
from .views import gallery, game

app_name = "gallery"

urlpatterns = [
    path('', gallery, name="index"),
    path('category/<int:pk>/', gallery, name='category'),
    path('basket/', include('basketapp.urls', namespace='basket')),
    path('category/<int:pk>/page/<int:page>/', gallery, name='page'),
    path("games/<int:pk>/", game, name="games"),
]
