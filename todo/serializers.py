from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Todo
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email',] # add fields to json
        
        
class TodoSerializer(serializers.HyperlinkedModelSerializer):
    # user = UserSerializer()
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault()) # adds user id
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'created_at', 'user', 'time_passed'] # add fields to json