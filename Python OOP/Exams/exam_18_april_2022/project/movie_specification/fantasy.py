from project_10_april.movie_specification.movie import Movie


class Fantasy(Movie):
    AGE_RESTRICT = 6

    def __init__(self, title: str, year: int, owner: object, age_restriction: int = AGE_RESTRICT):
        super().__init__(title, year, owner, age_restriction)

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if value < self.AGE_RESTRICT:
            raise ValueError("Fantasy movies must be restricted for audience under 6 years!")

        self.__age_restriction = value

    def details(self):
        return f"Fantasy - Title:{self.title}, Year:{self.year}, Age restriction:{self.age_restriction}, " \
               f"Likes:{self.likes}, Owned by:{self.owner.username}"
