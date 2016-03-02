#!/usr/bin/env python
#
# media.py - This files contains classes to be instantiated in
# 'entertainment.py'. Currently, this is only class called Movie, which contains
# attributes and a method that we can use to create a favorite movie page.

import webbrowser

class Movie():
    """Contains various data and methods for a movie object."""

    def __init__(self, movie_title, movie_quote, poster_image, trailer_youtube):
        """Constructor.

        Args:
            movie_title: string, title of movie
            movie_quote: string, quote from movie
            poster_image: string (URL), link to movie poster art
            trailer_youtube: string (URL), link to YouTube movie trailer
        """
        self.title = movie_title
        self.quote = movie_quote
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Opens a web browser and plays the YouTube movie trailer."""
        webbrowser.open(self.trailer_youtube_url)
