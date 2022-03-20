import requests
import time


def Prefix_function(prefix):
    def Decorator_function(func):

        def wrapper_function(*args, **kwargs):
            func(*args, **kwargs)
            start_time = round(time.time())
            end_time = round(time.time()) + 60
            taken_time = 0

            while round(time.time()) <= end_time:
                try:
                    get_request = requests.get(
                        prefix, timeout=1)
                    get_request.raise_for_status()
                except requests.exceptions.Timeout:
                    pass
                except requests.exceptions.ConnectionError:
                    pass
                except requests.exceptions.HTTPError:
                    pass
                except requests.exceptions.RequestException:
                    pass
                else:
                    if get_request.ok is True:
                        print(True)
                        break
        return wrapper_function
    return Decorator_function


@Prefix_function('https://xkcd.com/353/')
def start():
    print("Tuning Wizard server application startup complete.")


start()
