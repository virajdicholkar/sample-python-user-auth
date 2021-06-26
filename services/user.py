class UserService:
    __data = [
        {"id": 0, "first_name": "Viraj", "last_name": "Dicholkar"},
    ]

    def get_all(self):
        return self.__data

    def get(self, id: int):
        for user in self.__data:
            if user['id'] == id:
                return user

    def create(self, user):
        user["id"] = self.__data[-1]["id"] + 1 if len(self.__data) > 0 else 0
        self.__data.append(user)


user_service = UserService()
