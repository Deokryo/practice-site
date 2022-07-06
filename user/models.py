from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models



from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, nickname, password=None):
        if not email:
            raise ValueError("User must have an email address")
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            nickname=nickname,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, nickname, password=None):
        user = self.create_user(email, password=password, name=name, nickname=nickname)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    """
    유저 프로필사진
    유저 이름
    유저 닉네임
    유저 이메일
    """

    prof_img = models.TextField()
    name = models.CharField(max_length=30, null=True)
    nickname = models.CharField(max_length=30, null=True, unique=True)
    email = models.EmailField(unique=True)
    intro = models.TextField(null=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False, null=True)
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "User"

    objects = CustomUserManager()

    USERNAME_FIELD = "nickname"
    REQUIRED_FIELDS = ["email", "name"]

    def get_full_name(self):
        pass

    def get_short_name(self):
        pass

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    @is_staff.setter
    def is_staff(self, value):
        self._is_staff = value


# Create your models here.
