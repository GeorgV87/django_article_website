
from django.shortcuts import redirect, get_object_or_404
from article_app.form import ArticleForm, LoginForm
from django.views.generic import TemplateView, FormView, ListView, UpdateView
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from article_app.models import Article

# Create your views here.


class LoginView(FormView):
    template_name = "article_app/login_form.html"
    form_class = LoginForm
    success_url = reverse_lazy("article_app:home")

    def form_valid(self, form):
        request = self.request
        user = authenticate(
            username=form.cleaned_data["name"],
            password=form.cleaned_data["password"],
        )
        if user:
            request.session["user_id"] = user.id
            return redirect(self.get_success_url())
        else:
            return redirect("article_app:login_form")


class HomeView(TemplateView):
    template_name = "article_app/base.html"

    def dispatch(self, request, *args, **kwargs):
        user_id = request.session.get("user_id")
        if not user_id:
            return redirect("article_app:login_form")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.request.session.get("user_id")
        if user_id:
            user = User.objects.get(pk=user_id)
            context["user"] = user
        return context


class ArticleView(FormView):
    template_name = "article_app/article_form.html"
    form_class = ArticleForm
    success_url = reverse_lazy("article_app:article_success")

    def form_valid(self, form):
        # Save the form data to the database
        Article.objects.create(
            title=form.cleaned_data["title"],
            article=form.cleaned_data["article"],
            created_by=form.cleaned_data["created_by"],
        )
        return super().form_valid(form)


class ArticleListView(ListView):
    model = Article
    template_name = "article_app/article_list.html"
    context_object_name = "articles"


def like_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.likes += 1
    article.save()
    return redirect("article_app:article_list")


class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = "article_app/article_form.html"
    success_url = reverse_lazy("article_app:article_list")
