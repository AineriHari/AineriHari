import requests
import time

start_time = round(time.time())
end_time = round(time.time()) + 60
taken_time = 0

while round(time.time()) <= end_time:
    try:
        get_request = requests.get('https://xkcd.com/353/', timeout=1)
        get_request.raise_for_status()
    except requests.exceptions.Timeout:
        pass
    except requests.exceptions.ConnectionError:
        pass
    else:
        if get_request.ok is True:
            print(True)
            break
