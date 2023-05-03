# If you turn this off, login will not be executed and subsequent test cases should be skipped.
must_run = 1


# Run only selected tests that I need to execute. Usually this should be normally set to 0
my_cases = 0

# Turn it to 1 for sanity tests only, 0 to execute other tests.
sanitytest = 0

# Turn it to 1 for regression tests only, 0 to execute other tests.
regressiontest = 0

# Turn it to 1 for regression tests only, 0 to execute other tests.
usualtest = 0

# Turn it to 1 for regression tests only, 0 to execute other tests.
regression_tests = 0

# Turn it to 1 for avoid tests only, 0 to execute other tests.
avoid_test_cases = 0

negative_tests = 1
positive_tests = 1



# Run all positive and negative cases
test_tc_001_User_login = 1
test_tc_002_User_dashboard = 1
test_tc_013_User_Profile = 1


def run_positive_tests():
    print( "Inside run_positive_tests" )
    global test_tc_001_User_login
    test_tc_001_User_login = 1

    global test_tc_002_User_dashboard
    test_tc_002_User_dashboard = 1

def run_negative_tests():
    print( "Inside run_positive_tests" )
    global test_tc_000001_AccountAdmin_Invalid_Credentials
    test_tc_000001_AccountAdmin_Invalid_Credentials = 1

    global test_tc_000001_AccountAdmin_Invalid_Email
    test_tc_000001_AccountAdmin_Invalid_Email = 1

    global test_tc_000001_AccountAdmin_Invalid_Password
    test_tc_000001_AccountAdmin_Invalid_Password = 1

    global test_tc_000001_AccountAdmin_Credentials_With_Spaces
    test_tc_000001_AccountAdmin_Credentials_With_Spaces = 1

    global test_tc_000001_AccountAdmin_WithOut_Password
    test_tc_000001_AccountAdmin_WithOut_Password = 1

    global test_tc_000001_AccountAdmin_WithOut_UserName
    test_tc_000001_AccountAdmin_WithOut_UserName = 1

    global test_tc_000001_AccountAdmin_WithOut_UserName_Password
    test_tc_000001_AccountAdmin_WithOut_UserName_Password = 1


# # Turn it to 1 for smoke tests only, 0 to execute other tests.
# smoke_test = 0
#
# my_cases = 1
#
# run_test_tc_101_Login = 0
# run_test_tc_201_DashboardPage = 0
# run_test_tc_301_DevicesPage = 0
# run_test_tc_401_DeviceDetailsViewPage = 0
# run_test_tc_501_PolicyGroups = 0
# run_test_tc_601_Reports = 0
# run_test_tc_701_WeTrackPage = 0
# run_test_tc_801_WeBoxPage = 0
# run_test_tc_901_BroadcastPage = 0
# run_test_tc_1001_AuditLogsPage = 0
# run_test_tc_1001_WeTalkPage = 0
# run_test_tc_2001_AlertsPage = 0
# run_test_tc_3001_BulkActionsPage = 0
# run_test_tc_4001_Roles_PermissionsPage = 0
#
# def run_smoke_test():
#     global run_test_tc_101_Login
#     run_test_tc_101_Login = 1
#
#     global run_test_tc_201_Dashboard
#     run_test_tc_201_Dashboard = 1
#
#
# def run_regression_test():
#     global run_test_tc_101_Login
#     run_test_tc_101_Login = 1
#
#     global run_test_tc_201_Dashboard
#     run_test_tc_201_Dashboard = 1
#
#     global run_test_tc_301_DeviceDetailsView
#     run_test_tc_301_DeviceDetailsView = 1
#
#
# def run_my_cases():
#     global run_test_tc_420_DeviceDetailsView
#     run_test_tc_420_DeviceDetailsView = 1
#
#
# if my_cases == 1:
#     run_my_cases()
#
# if smoke_test == 1:
#     run_smoke_test()















