from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SignupView, LoginView, UserSearchView, FriendRequestViewSet, FriendListView, PendingFriendRequestsView


router = DefaultRouter()
router.register(r'friend-request', FriendRequestViewSet, basename='friend_request')

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('search/', UserSearchView.as_view(), name='user-search'),
    path('friends/', FriendListView.as_view(), name='friends'),
    path('pending-friend-request/', PendingFriendRequestsView.as_view(), name='pending-friend-requests'),
    path('', include(router.urls)),
]