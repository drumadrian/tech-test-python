from data_service import DataService
from user_service import UserService
def run():
    data_service = DataService()
    user_service = UserService(data_service)
    users = user_service.get_users_with_popular_posts(10)
    res = str(len(users))
    print("There are " + res + " users with popular posts")
run()