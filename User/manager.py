from Uber.User.db.config import user_service
class UserManager():
    def __init__(self,user_id=None):
        self.user_id =  user_id

    def get_users(self):
        return user_service.get()

    def create_user(self, name, email, mobile):
        res = user_service.create(user_name=name, email=email, mobile=mobile)
        return res
