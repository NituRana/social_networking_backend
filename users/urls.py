from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SignupView, LoginView, FriendRequestViewSet, FriendListView, UserSearchView


router = DefaultRouter()
router.register(r'friend_requests', FriendRequestViewSet, basename='friend_request')

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('friends/', FriendListView.as_view(), name='friends'),
    path('search/', UserSearchView.as_view(), name='user-search'),
    path('', include(router.urls)),
]