from rest_framework import serializers
from ..models import (
        Category,
        Movie,
        )
class MovieListSerializer(serializers.ModelSerializer):
    categories = serializers.HyperlinkedRelatedField("category_detail",read_only=True,many=True,lookup_field="slug")
    class Meta:
        model = Movie
        fields = ["id","name","categories"]


class CategorySerializer(serializers.ModelSerializer):
    movies = MovieListSerializer(many=True)
    class Meta:
        model = Category
        fields = ["id","name","movies"]

    # def get_movies(self,obj):
    #     return obj.movies.all()