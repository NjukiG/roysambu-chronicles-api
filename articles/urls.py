from django.urls import path

# from .views import ArticlesList, ArticlesDetail, UserList, UserDetail  # new
from rest_framework.routers import SimpleRouter

from .views import UserViewSet, ArticlesViewSet

router = SimpleRouter()
router.register("users", UserViewSet, basename="users")
router.register("", ArticlesViewSet, basename="articles")

urlpatterns = router.urls


# urlpatterns = [
#     path("users/", UserList.as_view()), # new
#     path("users/<int:pk>/", UserDetail.as_view()),  # new
#     path("<int:pk>/", ArticlesDetail.as_view(), name="articles_detail"),
#     path("", ArticlesList.as_view(), name="articles_list"),
# ]