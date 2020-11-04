import requests
import json
from retrying import retry
import userInfo


@retry(stop_max_attempt_number=10)
def get_store():
    url = userInfo.get_store_url()
    cookie_dict = userInfo.get_cookie_dict()
    headers = userInfo.get_headers()
    res = requests.get(url, cookies=cookie_dict, headers=headers).content
    j_res = json.loads(res)
    return j_res


def get_bj_stores_number():
    res = get_store()
    stores = res['stores']
    bj_stores = []
    for store in stores:
        if store['city'] == '北京':
            bj_stores.append((store['storeNumber'], store['city']+store['storeName']))
    return bj_stores


def get_sz_stores_number():
    res = get_store()
    stores = res['stores']
    sz_stores = []
    for store in stores:
        if store['city'] == '深圳':
            sz_stores.append((store['storeNumber'], store['city']+store['storeName']))
    return sz_stores


def get_all_stores_number():
    res = get_store()
    stores = res['stores']
    all_stores = []
    for store in stores:
        all_stores.append((store['storeNumber'], store['city']+store['storeName']))
    return all_stores


if __name__ == '__main__':
    bj_stores = get_bj_stores_number()
    sz_stores = get_sz_stores_number()
    all_stores = get_all_stores_number()
    print(bj_stores)
    print(len(bj_stores))
    print(all_stores)
    print(len(all_stores))
