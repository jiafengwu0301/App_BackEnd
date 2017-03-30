from rest_framework import generics, permissions, views, response,status
from .models import Account
from .serializers import AccountCreateSerializer, AccountSerializer, AuthenticateSerializer, \
    UpdateAccountSerializer, AccountRetrieveSerializer


# Create your views here.


class AccountCreateView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountCreateSerializer
    permission_classes = [permissions.AllowAny]


class AccountListView(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]


class AccountRetrieveView(generics.RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountRetrieveSerializer


class UpdateAccountView(generics.UpdateAPIView):
    queryset = Account.objects.all()
    serializer_class = UpdateAccountSerializer
    # permission_classes = [permissions.IsAuthenticated]


class AccountAuthenticationView(views.APIView):
    queryset = Account.objects.all()
    serializer_class = AuthenticateSerializer

    def post(self, request):
        data = request.data
        serializer = AuthenticateSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_date = serializer.data
            return response.Response(new_date,status=status.HTTP_200_OK)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)