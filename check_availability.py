from availability import get_availability
from store import get_bj_stores_number


WANTED_MODEL = 'MWDH2CH/A'


def check_availability():
    bj_stores = get_bj_stores_number()
    avai = get_availability()
    yoho = []
    res = {}
    for store_num, store_name in bj_stores:
        model_avai = avai['stores'][store_num][WANTED_MODEL]['availability']
        # print(store_name, model_avai)
        res[store_name] = model_avai
        if model_avai['contract'] or model_avai['unlocked']:
            yoho.append(store_name)
    return res, yoho


if __name__ == '__main__':
    res, yoho = check_availability()
    print(res)
    print(yoho)
