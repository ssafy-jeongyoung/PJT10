from django.db import models
from django.contrib.auth.models import AbstractUser
from allauth.account.adapter import DefaultAccountAdapter


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=254, blank=True, unique=True)
    campus = models.CharField(max_length=10)
    generation = models.IntegerField()
    money = models.IntegerField()
    financial_products = models.TextField(blank=True, null=True)
    # 관리자 유형
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        # """
        # Saves a new `User` instance using information provided in the
        # signup form.
        # """
        from allauth.account.utils import user_email, user_field, user_username
        # 기존 코드를 참고하여 새로운 필드들을 작성해줍니다.
        data = form.cleaned_data
        # first_name = data.get("first_name")
        # last_name = data.get("last_name")
        email = data.get("email")
        username = data.get("username")
        campus = data.get("campus")
        generation = data.get("generation")
        money = data.get("money")

        financial_product = data.get("financial_products")
        user_email(user, email)
        user_username(user, username)
        # if first_name:
        #     user_field(user, "first_name", first_name)
        # if last_name:
        #     user_field(user, "last_name", last_name)
        if campus:
            user.campus = campus
        if money:
            user.money = money
        if generation:
            user.generation = generation
        if financial_product:
            financial_products = user.financial_products.split(',')
            financial_products.append(financial_product)
            if len(financial_products) > 1:
                financial_products = ','.join(financial_products)
            user_field(user, "financial_products", financial_products)
        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            user.save()
        return user
