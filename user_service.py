from data_service import DataService

class UserService(DataService):
    def __init__(self, data_service):
        self.data_service = data_service

    def get_users_with_popular_posts(self, commentThreshold):
        return []
