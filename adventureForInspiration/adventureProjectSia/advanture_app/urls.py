from django.urls import path

from adventureProjectSia.advanture_app import views
from adventureProjectSia.advanture_app.views import article_details_or_comment, unauthorised_message, \
    delete_article, like_article, news_and_events

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('news&events/', news_and_events, name='news and events'),
    path('details/<int:pk>/', article_details_or_comment, name='article details or comment'),
    path('creat/', views.ArticleCreatView.as_view(), name='article creat'),
    path('edit/<int:pk>', views.UpdateArticleView.as_view(), name='edit article'),
    path('delete/<int:pk>', delete_article, name='delete article'),
    path('like/<int:pk>/', like_article, name='like article'),
    path('unknown/', unauthorised_message, name='message'),
    path('list/', views.ArticlesListView.as_view(), name='articles'),
]
