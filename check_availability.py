from availability import get_availability
# from store import get_bj_stores_number
from store import get_sz_stores_number


def check_availability(checkStores, strWantedModel):
    avai = get_availability()
    yoho = []
    res = {}
    for store_num, store_name in checkStores:
        model_avai = avai['stores'][store_num][strWantedModel]['availability']
        res[store_name] = model_avai
        if model_avai['contract'] or model_avai['unlocked']:
            yoho.append(store_name)
            print('有货：store_num[%s] store_name[%s] model[%s]' % (store_num, store_name, model_avai))
    return res, yoho


if __name__ == '__main__':
    check_stores = get_sz_stores_number()
    res, yoho = check_availability(check_stores,'MGLD3CH/A')
    print(res)
    print(yoho)
