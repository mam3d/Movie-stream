
from rest_framework import serializers
from ..models import (
        Category,
        Movie,
        Rating
        )

class MovieDetailSerializer(serializers.ModelSerializer):
    actors = serializers.StringRelatedField(many=True)
    categories = serializers.HyperlinkedRelatedField("category_detail",read_only=True,many=True,lookup_field="slug")
    class Meta:
        model = Movie
        fields = ["id","name","description","categories","actors","rating"]


class MovieListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="movie_detail",lookup_field = "slug")
    categories = serializers.HyperlinkedRelatedField("category_detail",read_only=True,many=True,lookup_field="slug")
    class Meta:
        model = Movie
        fields = ["url","name","categories"]
        

class CategorySerializer(serializers.ModelSerializer):
    movies = MovieListSerializer(many=True)
    class Meta:
        model = Category
        fields = ["id","name","movies"]


class RatingSerializer(serializers.ModelSerializer):

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["user"].required = False
    class Meta:
        model = Rating
        fields = ["id","user","movie","number"]

    def save(self,user):
        movie = self.validated_data["movie"]
        if Rating.objects.filter(user=user,movie=movie):
            raise serializers.ValidationError("error: you have rated this movie before")
        return super().save(user)


