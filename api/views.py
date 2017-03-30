from rest_framework import generics, permissions
from .models import Account
from .serializers import AccountCreateSerializer, AccountSerializer


# Create your views here.


class AccountCreateView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountCreateSerializer
    permission_classes = [permissions.AllowAny]


class AccountListView(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]

