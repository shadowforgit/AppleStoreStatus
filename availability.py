import requests
import json
from retrying import retry
import userInfo


@retry(stop_max_attempt_number=10)
def get_availability():
    url = userInfo.get_availability_model_url()
    cookie_dict = userInfo.get_cookie_dict()
    headers = userInfo.get_headers()
    res = requests.get(url, cookies=cookie_dict, headers=headers).content
    j_res = json.loads(res)
    return j_res


if __name__ == '__main__':
    res = get_availability()
    print(res)
