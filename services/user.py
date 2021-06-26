class UserService:
    __data = [
        {"id": "viraj_dicholkar", "first_name": "Viraj", "last_name": "Dicholkar", "password": "ABC123"},
    ]

    def get_all(self):
        return self.__data

    def get(self, _id):
        for user in self.__data:
            if user['id'] == _id:
                return user

    def create(self, user):
        user["id"] = self.__data[-1]["id"] + 1 if len(self.__data) > 0 else 0
        self.__data.append(user)

    def validate_user(self, user):
        user_result = self.get(user['id'])
        if not user_result:
            raise RuntimeError('User not found')
        if user["password"] != user_result["password"]:
            raise RuntimeError('Invalid password')
        return {
            "id": user_result["id"],
            "first_name": user_result["first_name"],
            "last_name": user_result["last_name"]
        }


user_service = UserService()
