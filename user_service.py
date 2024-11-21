from data_service import DataService

class UserService(DataService):
    def __init__(self, data_service):
        self.data_service = data_service


    ####################################################################################
    # IMPLEMENT THE NAIVE SOLUTION HERE Big O(n^3)
    ####################################################################################
    #
    # get all users
    # get all posts
    # get all comments
    #
    #        for each post:
    #            count the number of comments
    #            store the comment count with the post
    #
    #        if the comment count of comments >= 10:
    #            get a list of all posts for the user
    #            append user with the the list of the posts for the user 
    ####################################################################################    
    def get_users_with_popular_posts(self, commentThreshold):
        debug = False
        users_with_popular_posts = []
        all_users = self.data_service.get_users()
        all_posts = self.data_service.get_posts()
        all_comments = self.data_service.get_comments()
        temp_user = {}
        list_of_user_ids_with_popular_posts = []
        user_posts = []

        for post in all_posts:
            temp_post_count = 0
            post["comment_count"] = 0
            post_id = post["id"]
            for comment in all_comments:
                postId_of_comment = comment["postId"]
                if (postId_of_comment == post_id):
                    post["comment_count"] = post["comment_count"] + 1


        for post in all_posts:
            post["post_is_popular"] = False
            if (post["comment_count"] >= commentThreshold):
                post["post_is_popular"] = True
                if (debug):
                    print("popular_post: ", post)
                    print("post[\"comment_count\"]: ", post["comment_count"])
                popular_post_user_id = post["userId"]
                list_of_user_ids_with_popular_posts.append(popular_post_user_id)
            

        # For all users, if they have a popular post save the user. 
        # Then add the all posts for that user to the user object
        for user in all_users:
            if (user["id"] in list_of_user_ids_with_popular_posts):
                for post in all_posts:
                    if(post['userId'] == user["id"]):
                        user_posts.append(post)
                temp_user = user
                temp_user["posts"] = user_posts
                users_with_popular_posts.append(temp_user)


        return users_with_popular_posts









    ####################################################################################
    # IMPLEMENT THE OPTIMIZED SOLUTION HERE O(n) or O(1)
    ####################################################################################
    #
    # get all users
    # get all posts
    # get all comments
    #
    #        Find popular comments:
    #            count the number of comments per postId using a dictionary where:
    #               comment_count_dictionary[comment["postId"]] = comment_count_dictionary.get(comment["postId"], 0) + 1

    #            store the comment count with the postId
    #
    #        if the comment count of comments >= 10:
    #            get a list of all posts for the user
    #            append user with the the list of the posts for the user 
    ####################################################################################    

    ####################################################################################    
    def get_users_with_popular_posts_optimized(self, commentThreshold):
        debug = False
        users_with_popular_posts = []  # List of users with popular posts
        all_users = self.data_service.get_users()
        all_posts = self.data_service.get_posts()
        all_comments = self.data_service.get_comments()

        comment_count_dictionary = {}  # Map postId -> comment count
        list_of_popular_postIds = []  # List of postIds with comment count >= commentThreshold

        # Count comments for each postId
        for comment in all_comments:
            comment_count_dictionary[comment["postId"]] = comment_count_dictionary.get(comment["postId"], 0) + 1

        if debug:
            print("comment_count_dictionary:", comment_count_dictionary)

        # Find postIds with comment count >= commentThreshold
        for postId, count in comment_count_dictionary.items():
            if count >= commentThreshold:
                list_of_popular_postIds.append(postId)

        if debug:
            print("list_of_popular_postIds:", list_of_popular_postIds)

        # Create a mapping of userId -> posts for efficient lookup
        user_posts_map = {}
        for post in all_posts:
            userId = post["userId"]
            if userId not in user_posts_map:
                user_posts_map[userId] = []
            user_posts_map[userId].append(post)

        if debug:
            print("user_posts_map:", user_posts_map)

        # Identify users with popular posts
        for postId in list_of_popular_postIds:
            # Find the post with the matching postId
            popular_post = next((post for post in all_posts if post["id"] == postId), None)
            if popular_post:
                userId = popular_post["userId"]
                # Find the user and ensure they're only added once
                user = next((user for user in all_users if user["id"] == userId), None)
                if user and user not in users_with_popular_posts:
                    # Add the user's posts to their object
                    user["posts"] = user_posts_map.get(userId, [])
                    users_with_popular_posts.append(user)

        if debug:
            print("users_with_popular_posts:", users_with_popular_posts)

        return users_with_popular_posts







    ####################################################################################
    # IMPLEMENT THE AI OPTIMIZED SOLUTION HERE 
    ####################################################################################    
    #
    # Here's a Python function optimized to retrieve users with popular posts 
    #     based on a comment threshold, utilizing data services for users, posts, and comments. 
    #     This function is designed for optimal performance:
    #
    # Explanation of Optimizations:
    # Precompute Comment Counts:
    #
    # Counts comments per postId in a single pass (O(n)).
    # Identify Popular Posts:
    #
    # Filters postIds with a comment count above the threshold (O(n)).
    # Map Posts to Users:
    #
    # Groups posts by userId to avoid repetitive loops (O(n)).
    # Single Pass for Result Assembly:
    #
    # Combines data efficiently into a final list of users with their popular posts (O(m), where m is the number of users).
    # Complexity:
    # Time Complexity: O(n + m), where n is the total number of comments/posts and m is the total number of users.
    # Space Complexity: O(n + m), for dictionaries and result storage.
    # This approach ensures the function is both time-efficient and scalable for large datasets.
    ####################################################################################    
    ####################################################################################    
    def get_users_with_popular_posts_ai_optimized(self, commentThreshold):
        debug = False

        # Fetch all data
        all_users = self.data_service.get_users()
        all_posts = self.data_service.get_posts()
        all_comments = self.data_service.get_comments()

        # Dictionary to count comments by postId
        comment_count_by_post = {}

        # Count comments for each postId
        for comment in all_comments:
            post_id = comment["postId"]
            comment_count_by_post[post_id] = comment_count_by_post.get(post_id, 0) + 1

        if debug:
            print("comment_count_by_post:", comment_count_by_post)

        # Identify popular postIds
        popular_post_ids = {
            post_id for post_id, count in comment_count_by_post.items() if count >= commentThreshold
        }

        if debug:
            print("popular_post_ids:", popular_post_ids)

        # Map users to their posts
        user_posts_map = {user["id"]: [] for user in all_users}
        for post in all_posts:
            if post["id"] in popular_post_ids:
                user_posts_map[post["userId"]].append(post)

        if debug:
            print("user_posts_map:", user_posts_map)

        # Create list of users with popular posts
        users_with_popular_posts = []
        for user in all_users:
            user_id = user["id"]
            if user_posts_map[user_id]:  # If user has popular posts
                user_copy = user.copy()
                user_copy["posts"] = user_posts_map[user_id]
                users_with_popular_posts.append(user_copy)

        if debug:
            print("users_with_popular_posts:", users_with_popular_posts)

        return users_with_popular_posts










