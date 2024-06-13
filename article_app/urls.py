from django.urls import path
from article_app.views import (
    HomeView,
    ArticleView,
    LoginView,
    TemplateView,
    ArticleListView,
    like_article,
    ArticleUpdateView,
)

app_name = "article_app"
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("login/", LoginView.as_view(), name="login_form"),
    path("create_article/", ArticleView.as_view(), name="article_form"),
    path(
        "article_succcess/",
        TemplateView.as_view(template_name="article_app/article_success.html"),
        name="article_success",
    ),
    path(
        "articles",
        ArticleListView.as_view(template_name="article_app/article_list"),
        name="article_list",
    ),
    path("articles/like/<int:pk>/", like_article, name="like_article"),
    path(
        "articles/edit/<int:pk>/",
        ArticleUpdateView.as_view(template_name="article_app/article_form.html"),
        name="edit_article",
    ),
]
