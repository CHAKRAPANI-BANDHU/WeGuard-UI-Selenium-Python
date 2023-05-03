import os
from WeGuardlogger import rotate_log_file
import time
from datetime import datetime

now_datetime = datetime.now()
start_of_day_datetime = now_datetime.replace(hour=00, minute=00, second=00)
end_of_day_datetime = now_datetime.replace(hour=23, minute=59, second=59)
start_timestamp = int(round(start_of_day_datetime.timestamp() * 1000))
end_timestamp = int(round(end_of_day_datetime.timestamp() * 1000))


# global username
username = 'chakrapani.bandhu@weguard.com'
global password
password = ''
global BaseURL
BaseURL= ''
global loglevel
loglevel = 4

wait = 60

# Urls
LoginUrl = "https://qa-cloud.weguard.io/#/login"

# if os.environ.get('WEGUARD_USER') is not None:
#     username = os.getenv('WEGUARD_USER')

if os.environ.get('WEGUARD_PASS') is not None:
    password = os.getenv('WEGUARD_PASS')

if os.environ.get('QA_BASEURL') is not None:
    BaseURL = os.getenv('QA_BASEURL')

if os.environ.get('LOG_LEVEL') is not None:
    loglevel = int(os.environ['LOG_LEVEL'])

log_file = "WeGuard" + format(time.strftime("%Y%m%d_%H%M%S")) + ".log"
rotate_log_file(log_file, loglevel)

chrome_driver_path= "chromedriver"

timeout= 300


