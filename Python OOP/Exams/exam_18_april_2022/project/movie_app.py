from project_10_april.movie_specification.movie import Movie
from project_10_april.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def __user_is_registered(self, username: str):
        if username in [user.username for user in self.users_collection]:
            return True

    def __movie_is_uploaded(self, movie: Movie):
        if movie in self.movies_collection:
            return True

    def __get_user(self, username: str):
        return [u for u in self.users_collection if u.username == username][0]

    @staticmethod
    def __user_is_owner(username: str, movie: Movie):
        if movie.owner.username == username:
            return True

    def register_user(self, username: str, age: int):
        if self.__user_is_registered(username):
            raise Exception("User already exists!")

        self.users_collection.append(User(username, age))

        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        if self.__movie_is_uploaded(movie):
            raise Exception("Movie already added to the collection!")

        if not self.__user_is_registered(username):
            raise Exception("This user does not exist!")

        if not self.__user_is_owner(username, movie):
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        user = self.__get_user(username)
        self.movies_collection.append(movie)
        user.movies_owned.append(movie)

        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        if not self.__movie_is_uploaded(movie):
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if not self.__user_is_owner(username, movie):
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for attribute, new_attribute in kwargs.items():
            if attribute == "title":
                movie.title = new_attribute
            elif attribute == "year":
                movie.year = new_attribute
            elif attribute == "age_restriction":
                movie.age_restriction = new_attribute

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        if not self.__movie_is_uploaded(movie):
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if not self.__user_is_owner(username, movie):
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        user = self.__get_user(username)
        user.movies_owned.remove(movie)
        self.movies_collection.remove(movie)

        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = self.__get_user(username)
        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        if self.__user_is_owner(username, movie):
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)

        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = self.__get_user(username)
        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)

        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if self.movies_collection:
            movies = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))

            return "\n".join([movie.details() for movie in movies])

        return "No movies found."

    def __str__(self):
        result = []
        if not self.users_collection:
            result.append("All users: No users.")
        else:
            result.append(f"All users: {', '.join([user.username for user in self.users_collection])}")

        if not self.movies_collection:
            result.append("All movies: No movies.")
        else:
            result.append(f"All movies: {', '.join([movie.title for movie in self.movies_collection])}")

        return "\n".join(el for el in result)
