from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.crypto import get_random_string

from .tasks import send_activation_code



class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, email, password, phone, **kwargs):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, phone=phone, **kwargs)
        # self.model = User
        user.set_password(password)  # хеширование пароля
        user.create_activation_code()
        user.save(using=self._db)  # созраняем юзера в бд
        send_activation_code.delay(user.email, user.activation_code)
        return user

    def create_superuser(self,username, email, password, phone, **kwargs):
        if not email:
            raise ValueError("Email is required")
        kwargs["is_staff"] = True  # даем права суперадмина
        kwargs["is_superuser"] = True
        kwargs["is_active"] = True
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, phone=phone, **kwargs)
        # self.model = User
        user.set_password(password)  # хеширование пароля
        user.save(using=self._db)  # созраняем юзера в бд
        return user
    


class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)  # когда регитр-ся чтобы выходило "Польз-ль с таким имененем уже сущ-ет
    phone = models.CharField(max_length=50)
    bio = models.TextField()
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    is_active = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=8, null=True)


    USERNAME_FIELD = 'username'    # указываем какое поле использовать при логине
    REQUIRED_FIELDS = ['email', 'phone']

    objects = UserManager()  # указываем нового менеджера

    def create_activation_code(self):
        self.activation_code = get_random_string(8, 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890')
