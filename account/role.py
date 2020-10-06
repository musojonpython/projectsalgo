from django.contrib.auth import get_user_model
User = get_user_model()


def account_role(user_role, user_id):
    user = User.objects.get(id=user_id)
    if user_role == 'director':
        user.is_director = True
    elif user_role == 'accountant':
        user.is_accountant = True
    elif user_role == 'warehouseman':
        user.is_is_warehouseman = True
    elif user_role == 'staff':
        user.is_staff = True 
    user.save()