#!/usr/bin/env python
#
# entertainment_center.py - This file contains instantiations of class Movie
# (defined in 'media.py') that are put into a list and rendered by the fancy
# stuff in 'fresh_tomatoes.py'. We end up with a tidy webpage that will play
# movie trailers when clicking on the image.

import fresh_tomatoes
import media

# Instantiate favorite movie objects from class Movie defined in 'media.py'.
# Favorite movie #1
blade_runner = media.Movie(
    'Blade Runner',
    'I want more life, fucker.',
    'https://upload.wikimedia.org/wikipedia/en/5/53/Blade_Runner_poster.jpg',
    'https://www.youtube.com/watch?v=4lW0F1sccqk')

# Favorite movie #2
dune = media.Movie(
    'Dune',
    'Tell me of your homeworld, Usul.',
    'https://upload.wikimedia.org/wikipedia/en/5/51/Dune_1984_Poster.jpg',
    'https://www.youtube.com/watch?v=KwPTIEWTYEI')

# Favorite movie #3
mad_max_beyond_thunderdome = media.Movie(
    'Mad Max: Beyond Thunderdome',
    '''I ain't Captain Walker. I'm the guy who carries Mr. Dead in his pocket.''',
    'https://upload.wikimedia.org/wikipedia/en/e/e0/Mad_max_beyond_thunderdome.jpg',
    'https://www.youtube.com/watch?v=n3horf9QVbQ')

# Favorite movie #4
moon = media.Movie(
    'Moon',
    '''Gerty, we're not programmed. We're people, do you understand?''',
    'https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Moon_%282008%29_film_poster.jpg/215px-Moon_%282008%29_film_poster.jpg',
    'https://www.youtube.com/watch?v=twuScTcDP_Q')

# Favorite movie #5
flash_gordon = media.Movie(
    'Flash Gordon',
    '''GORDON'S ALIVE!''',
    'https://upload.wikimedia.org/wikipedia/en/5/50/Flash_gordon_movie_poster.jpg',
    'https://www.youtube.com/watch?v=OROLRvKamdE')

# Favorite movie #6
the_fifth_element = media.Movie(
    'The Fifth Element',
    'Me fifth element - supreme being. Me protect you.',
    'https://upload.wikimedia.org/wikipedia/en/6/65/Fifth_element_poster_%281997%29.jpg',
    'https://www.youtube.com/watch?v=VkX7dHjL-aY')

# Put our movie objects into a list.
movies = [blade_runner, dune, mad_max_beyond_thunderdome, moon, flash_gordon,
the_fifth_element]

# Call the open_movies_page function (defined in 'fresh_tomatoes.py') and render
# our movie site using instantiated movie objects.
fresh_tomatoes.open_movies_page(movies)
