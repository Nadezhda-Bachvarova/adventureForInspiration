from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from adventureProjectSia.advanture_app.forms import CommentForm, ArticleCreateForm
from adventureProjectSia.advanture_app.models import Article, Comment, Like, NewsAndEvents
from adventureProjectSia.adventure_core.clean_up import clean_up_files


class HomeView(views.TemplateView):
    template_name = 'home.html'


def unauthorised_message(request):
    return render(request, 'unauthorised.html')


class ArticleCreatView(LoginRequiredMixin, views.CreateView):
    template_name = 'article_create.html'
    model = Article
    form_class = ArticleCreateForm

    def get_success_url(self):
        url = reverse_lazy('article details or comment', kwargs={'pk': self.object.id})
        return url

    def form_valid(self, form):
        article = form.save(commit=False)
        article.user = self.request.user.userprofile
        article.save()
        return super().form_valid(form)


class UpdateArticleView(LoginRequiredMixin, views.UpdateView):
    template_name = 'article_edit.html'
    model = Article
    form_class = ArticleCreateForm

    def get_success_url(self):
        url = reverse_lazy('article details or comment', kwargs={'pk': self.object.id})
        return url

    def form_valid(self, form):
        old_image = self.get_object().image
        if old_image:
            clean_up_files(old_image.path)
            return super().form_valid(form)


class ArticlesListView(views.ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'articles'


@login_required
def article_details_or_comment(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'article': article,
            'form': CommentForm(),
            'can_delete': request.user == article.user.user,
            'can_edit': request.user == article.user.user,
            'can_like': request.user != article.user.user,
            'has_liked': article.like_set.filter(article_id=request.user.userprofile.id).exists(),
            'can_comment': request.user != article.user.user,
            'author': article.user.user,
        }
        return render(request, 'article_details.html', context)
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(text=form.cleaned_data['text'])
            comment.article = article
            comment.user = request.user.userprofile
            comment.save()
            return redirect('article details or comment', pk)
        context = {
            'article': article,
            'form': form,
        }

        return render(request, 'article_details.html', context)


@login_required
def delete_article(request, pk):
    article = Article.objects.get(pk=pk)
    if article.user.user != request.user:
        pass
    if request.method == 'GET':
        context = {
            'article': article,
        }
        return render(request, 'article_delete.html', context)
    else:
        article.delete()
        return redirect('articles')


@login_required
def like_article(request, pk):
    like = Like.objects.filter(user_id=request.user.userprofile.id, article_id=pk).first()
    if like:
        like.delete()
    else:
        article = Article.objects.get(pk=pk)
        like = Like(test=str(pk), user=request.user.userprofile)
        like.article = article
        like.save()

    return redirect('article details or comment', pk)


@login_required
def news_and_events(request):
    events = NewsAndEvents.objects.all()
    if request.method == 'GET':
        context = {
            'events': events,
        }
        return render(request, 'news_and_events.html', context)
