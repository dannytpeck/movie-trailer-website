class Movie():
    """A class representing a single movie.

    Attributes:
        title (str): The movie's title
        poster_image_url (str): A url for a poster image
        trailer_youtube_url (str): A url for a youtube trailer
    """
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
