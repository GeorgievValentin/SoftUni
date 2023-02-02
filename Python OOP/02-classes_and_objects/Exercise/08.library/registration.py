from oop.oop_exams.retake_exam_22_august_2022.project import User
from oop.oop_exams.retake_exam_22_august_2022.project import Library


class Registration:
    def add_user(self, user: User, library: Library):
        if user in library.user_records:
            return f"User with id = {user.user_id} already registered in the library!"

        library.user_records.append(user)

    def remove_user(self, user: User, library: Library):
        if user in library.user_records:
            library.user_records.remove(user)

        return f"We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str, library: Library):
        for user in library.user_records:
            if user.user_id == user_id:
                if not user.username == new_username:
                    user.username = new_username

                    if user.username in library.rented_books:
                        library.rented_books[new_username] = library.rented_books[user.username]
                        del library.rented_books[user.username]

                    return f"Username successfully changed to: {new_username} for user id: {user_id}"

                return f"Please check again the provided username - it should be different than the username used so far!"

            return f"There is no user with id = {user_id}!"



