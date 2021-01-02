from django.urls import path, include

from adventureProjectSia.accounts.views import SignUpView, signin_user, signout_user, user_profile

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', signin_user, name='signin user'),
    path('signout/', signout_user, name='signout user'),
    path('profile/<int:pk>/', user_profile, name='user profile'),
    path('profile/', user_profile, name='current user profile'),
]
