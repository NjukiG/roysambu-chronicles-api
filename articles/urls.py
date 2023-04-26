from django.urls import path

from .views import ArticlesList, ArticlesDetail


urlpatterns = [
    path("<int:pk>/", ArticlesDetail.as_view(), name="articles_detail"),
    path("", ArticlesList.as_view(), name="articles_list"),
]