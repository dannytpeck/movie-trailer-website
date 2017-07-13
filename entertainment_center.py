import media
import fresh_tomatoes

back_to_the_future = media.Movie("Back to the Future",
                        "https://upload.wikimedia.org/wikipedia/en/d/d2/Back_to_the_Future.jpg", # NOQA
                        "https://www.youtube.com/watch?v=qvsgGtivCgs")

robocop = media.Movie("Robocop",
                      "https://upload.wikimedia.org/wikipedia/en/1/16/RoboCop_%281987%29_theatrical_poster.jpg", # NOQA
                      "https://www.youtube.com/watch?v=clqK5OC3BWE")

commando = media.Movie("Commando",
                       "https://upload.wikimedia.org/wikipedia/en/d/d9/Commandoposter.jpg", # NOQA
                       "https://www.youtube.com/watch?v=qAsscHY2ozw")

# Add all our movies to a list
movies = [back_to_the_future, robocop, commando]

# Supply the list to open_movies_page() from fresh_tomatoes
fresh_tomatoes.open_movies_page(movies)
