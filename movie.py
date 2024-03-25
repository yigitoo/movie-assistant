from speech import SpeechServices
from imdb import Cinemagoer
import datetime

imdbClient = Cinemagoer()

speech = SpeechServices()
# what film do you want to see?
film_name = ''

while (film_name == ''):
    film_name = speech.listen()
    print(film_name)
# get movie
movie = imdbClient.search_movie(film_name)

if len(movie) != 0:
    movie = movie[0]
    if movie.data.get('title') == None:
        print('We couldnt find it sir.')
        exit(1)

    print(f'''
    {movie._getitem('title')}
    ----------------
    MovieID: {movie.getID()}
    Title: {movie._getitem('title')}
    Movie Data: {movie.data}
    ''')

else:
    print('We couldn\'t find it sir.')
