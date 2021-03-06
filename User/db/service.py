from Uber.User.db.models import User

class UserService(object):

    users = [User('user-1','a','a', False), User('user-2','a','a', False),
             User('driver-1','a','a', False), User('driver-2','a','a', False)]

    def get(self):
        return [self.embed(user) for user in self.users]

    def update(self, user_id):
        pass

    def create(self, user_name, email, mobile):
        user = User(user_name, email, mobile)
        self.users.append(user)
        return self.embed(user)

    def delete(self):
        pass

    def embed(self,user):
        return user.__dict__
