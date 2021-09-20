from django.test import TestCase, Client

from .models import Movie
from .serializers import MovieSerializer
from genres.models import Genre

import factory

class GenreFaker(factory.Factory):
    class Meta:
        model = Genre
    name = factory.Faker('word', locale='ru_RU')

class MovieFaker(factory.Factory):
    class Meta:
        model = Movie

    title = factory.Faker('sentence', nb_words=3, locale='ru_RU')
    year = factory.Faker('year')
    genre = factory.SubFactory(GenreFaker)

class MovieAPITest(TestCase):
    MAX_MOVIES_COUNT = 20

    def setUp(self):
        self.client = Client()
        self.movies = MovieFaker.create_batch(self.MAX_MOVIES_COUNT)
        for movie in self.movies:
            print(movie.title, movie.year, movie.genre)
            movie.genre.save()
            movie.save()

    def test_movies_get(self):
        response = self.client.get('/api/movies/')
        # Сколько у нас всего фильмов.
        self.assertEqual(Movie.objects.count(), self.MAX_MOVIES_COUNT)
        # Проверяем HTTP-код ответа.
        self.assertEqual(response.status_code, 200)
        # Проверяем содержимое ответа.
        expected = {'movies': MovieSerializer(self.movies, many=True).data}
        self.assertEqual(response.json(), expected)

    def tearDown(self):
        pass
