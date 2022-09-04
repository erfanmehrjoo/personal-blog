from blog.models import Post , Tag
from rest_framework.serializers import ModelSerializer

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"