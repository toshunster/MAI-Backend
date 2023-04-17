from rest_framework import serializers

from movies.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    genre = serializers.CharField(read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'
        #fields = ('title', 'year', 'genre')
