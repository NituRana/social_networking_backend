from django.shortcuts import render

from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework import generics
from django.db.models import Q
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from django_ratelimit.decorators import ratelimit
from django.utils.decorators import method_decorator

from .models import User, FriendRequest
from .serializers import FriendRequestSerializer, UserSerializer, CustomAuthTokenSerializer


class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class LoginView(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

# for search
class UserSearchView(generics.ListAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = UserSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        return User.objects.filter(
            Q(email__iexact=query) | Q(full_name__icontains=query)
        )

class FriendRequestViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer

    def get_queryset(self):
        return self.queryset.filter(to_user=self.request.user, accepted=False, rejected=False)

    @method_decorator(ratelimit(key='user', rate='3/m', method='POST', block=True))
    
    @action(detail=False, methods=['post'])
    def send(self, request):
        from_user = request.user
        to_user_id = request.data.get('to_user')
        try:
            to_user = User.objects.get(id=to_user_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if from_user == to_user:
            return Response({'error': 'You cannot send a friend request to yourself'}, status=status.HTTP_400_BAD_REQUEST)

        if FriendRequest.objects.filter(from_user=from_user, to_user=to_user).exists():
            return Response({'error': 'Friend request already sent'}, status=status.HTTP_400_BAD_REQUEST)

        friend_request = FriendRequest(from_user=from_user, to_user=to_user)
        friend_request.save()
        return Response(FriendRequestSerializer(friend_request).data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def accept(self, request, pk=None):
        friend_request = self.get_object()
        friend_request.accepted = True
        friend_request.save()
        return Response({'status': 'Request accepted'})

    @action(detail=True, methods=['post'])
    def reject(self, request, pk=None):
        friend_request = self.get_object()
        friend_request.rejected = True
        friend_request.save()
        return Response({'status': 'Request rejected'})

class FriendListView(generics.ListAPIView):
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        friends = FriendRequest.objects.filter(to_user=user, accepted=True).values_list('from_user', flat=True)
        return User.objects.filter(id__in=friends)

class PendingFriendRequestsView(generics.ListAPIView):
    serializer_class = FriendRequestSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return FriendRequest.objects.filter(to_user=user, accepted=False, rejected=False)