from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from .models import Account
from .serializers import AccountSerializer
from .role import account_role
from django.contrib.auth import authenticate
User = get_user_model()


class RegisterUserAPIView(APIView):
    def post(self, request):
        data = request.data
        phone_number = data['phone_number']
        password = data['password']
        user_role = data['role']
        new_user = User.objects.create_user(phone_number, password)
        token, _ = Token.objects.get_or_create(user=new_user)
        user = User.objects.get(phone_number=phone_number).id
        data['user'] = user
        account_role(user_role, user)
        serializer = AccountSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)


class LoginUserAPIView(APIView):
    """
            post:
            Login users.
    """

    def post(self, request):
        data = request.data
        phone_number = data['phone_number']
        password = data['password']
        user = authenticate(phone_number=phone_number, password=password)
        if not user:
            return Response({'error': 'Invalid Credentials'})
        else:
            token, _ = Token.objects.get_or_create(user=user)
            role = {
                'is_director':user.is_director,
                'is_accountant':user.is_accountant,
                'is_warehouseman':user.is_warehouseman,
                'is_staff':user.is_staff
            }
            return Response({'token': token.key, 'user_id': user.id, 'role':role})
