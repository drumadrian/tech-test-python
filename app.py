from data_service import DataService
from user_service import UserService
import datetime

# ENABLE DEBUGING and TESTING FOR EASY TROUBLESHOOTING
debug = False
testing = True

def run():
    data_service = DataService()
    user_service = UserService(data_service)
    users = user_service.get_users_with_popular_posts(10)
    res = str(len(users))
    print("\n\n There are " + res + " users with popular posts")
    if (debug): 
        print("\n users: ", users)
        print("")


def run_optimized():
    data_service = DataService()
    user_service = UserService(data_service)
    users = user_service.get_users_with_popular_posts_optimized(10)
    res = str(len(users))
    print("\n\n There are " + res + " users with popular posts(Adrian Optimized)")
    if (debug): 
        print("\n users: ", users)
        print("")


def run_ai_optimized():
    data_service = DataService()
    user_service = UserService(data_service)
    users = user_service.get_users_with_popular_posts_ai_optimized(10)
    res = str(len(users))
    print("\n\n There are " + res + " users with popular posts(AI optimized)")
    if (debug): 
        print("\n users: ", users)
        print("")







####################################################################################
# THIS WILL START THE APPLICATION AND PRINT THE TIME ELAPSED FOR COMPARISON
####################################################################################
start = datetime.datetime.now()
if (debug):
    # Print the current date and time in a specific format
    print("current date and time: ",str(start.strftime("%Y-%m-%d %H:%M:%S")))
run()
end = datetime.datetime.now()
time_difference = end - start
print("elapsed_seconds: ", time_difference.total_seconds() )
print("\n\n\n")





####################################################################################
# THIS WILL START THE **OPTIMIZED** APPLICATION AND PRINT THE TIME ELAPSED FOR COMPARISON
####################################################################################
start = datetime.datetime.now()
if (debug):
    # Print the current date and time in a specific format
    print("\ncurrent date and time: ",str(start.strftime("%Y-%m-%d %H:%M:%S")))
run_optimized()
end = datetime.datetime.now()
time_difference_optimized = end - start
print("elapsed_seconds(optimized): ", time_difference_optimized.total_seconds() )
print("\n\n\n\n")





####################################################################################
# THIS WILL START THE **AI OPTIMIZED** APPLICATION AND PRINT THE TIME ELAPSED FOR COMPARISON
####################################################################################
start = datetime.datetime.now()
if (debug):
    # Print the current date and time in a specific format
    print("\ncurrent date and time: ",str(start.strftime("%Y-%m-%d %H:%M:%S")))
run_ai_optimized()
end = datetime.datetime.now()
time_difference_ai_optimized = end - start
print("elapsed_seconds(ai_optimized): ", time_difference_ai_optimized.total_seconds() )
print("\n\n\n\n")




####################################################################################
# THIS WILL PRINT ALL THE TIME ELAPSED FOR COMPARISON
####################################################################################
print("####################################################################################")
print("elapsed_seconds: ", time_difference.total_seconds() )
print("elapsed_seconds(ai_optimized): ", time_difference_optimized.total_seconds() )
print("elapsed_seconds(ai_optimized): ", time_difference_ai_optimized.total_seconds() )
print("####################################################################################\n\n")




####################################################################################
# BONUS
# THIS WILL TEST THE APPLICATION
####################################################################################
if (testing == True):

    try:
        data_service = DataService()
        testing_UserService = UserService(data_service)
        test_result_1 = testing_UserService.get_users_with_popular_posts(-1)
        test_result_2 = testing_UserService.get_users_with_popular_posts_optimized(1)
        test_result_3 = testing_UserService.get_users_with_popular_posts_ai_optimized(-1)
        
        test_result_4 = testing_UserService.get_users_with_popular_posts(0)
        test_result_5 = testing_UserService.get_users_with_popular_posts_optimized(0)
        test_result_6 = testing_UserService.get_users_with_popular_posts_ai_optimized(0)
        
        # test_result_7 = testing_UserService.get_users_with_popular_posts(".")
        # test_result_8 = testing_UserService.get_users_with_popular_posts_optimized(".")
        # test_result_9 = testing_UserService.get_users_with_popular_posts_ai_optimized(".")

    except:
        print("BONUS Test Results: ")
        print("test_result_1", test_result_1)
        print("test_result_2", test_result_2)
        print("test_result_3", test_result_3)

        print("test_result_4", test_result_4)
        print("test_result_5", test_result_5)
        print("test_result_6", test_result_6)

        # print("test_result_7", test_result_7)
        # print("test_result_8", test_result_8)
        # print("test_result_9", test_result_9)



