from djoser.serializers import UserCreateSerializer
from djangoauth.models import CustomUser

class UserCreateSerializer(UserCreateSerializer):
  class Meta(UserCreateSerializer):
    model=CustomUser
    fields=('id','email','firstname','lastname','password')