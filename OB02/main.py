class User():
    def __init__(self, id_number, name, level='user'):
        self._id = id_number
        self._name = name
        self._level = level

class Admin(User):
    def __init__(self, id_number=0, name="Admin", level='user', admin=True):
        super().__init__(id_number, name, level)
        self.__admin = admin
        self.__list_users = {} #по-хорошему список нужно делать отдельным классом, а лучше базой, но в рамках задания нет условия

    def add_user(self, user):
        self.__list_users[user._id] = user

    def remove_user(self,user):
        del self.__list_users[user._id]

    def get_list_users(self):
        print(f"Список пользователей {self.__list_users}")

    def set_level_admin(self, admin=True):
        self.__admin = admin

admin = Admin()

#будем считать, что имя уникальное

vasilii = User(1,"vasilii")
masha = User(2,"masha")
vlad = User(3,"vlad")
dasha = User(4,"dasha")

admin.add_user(vasilii)
admin.add_user(masha)
admin.add_user(vlad)
admin.add_user(dasha)

admin.get_list_users()

admin.remove_user(vasilii)

admin.get_list_users()

misha = Admin()
print(misha._Admin__admin)
misha.set_level_admin(False)
print(misha._Admin__admin)




