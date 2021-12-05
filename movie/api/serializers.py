from rest_framework import serializers
from ..models import (
        Category,
        Movie,
        )

class MovieDetailSerializer(serializers.ModelSerializer):
    actors = serializers.StringRelatedField(many=True)
    categories = serializers.HyperlinkedRelatedField("category_detail",read_only=True,many=True,lookup_field="slug")
    class Meta:
        model = Movie
        fields = ["id","name","description","categories","actors"]


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
