#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_cookie_dict():
    cookie_str = r'cookie: geo=CN; ccl=9bo94Mc4iaYZcfj3hRdRUA==; xp_ci=3z3PZw1XzGhwz51hzCaGzX01MVGWY; s_fid=3E8BCF5163FF2C60-22662FEFBFC7307C; s_cc=true; s_vi=[CS]v1|2FB0760A8515FC57-400006E5C5BDA072[CE]; dssid2=d1474493-71da-46b4-9b1a-7888839e3d4a; dssf=1; pxro=1; dslang=CN-ZH; site=CHN; XID=6b24337e6d7e7acdb42531960e285cd7; s_ppvl=%5B%5BB%5D%5D; s_orientation=%5B%5BB%5D%5D; as_pcts=Np:VRO3Hh7ruX0CiI34LqSjjxOP5v0vmWyLi1A5uP3NWe4xoC70sZWAoeMRE-Ed:p5DUVj; check=true; mbox=session#04127c49d8344ac8b77ae9088d311022#1603578860|PC#04127c49d8344ac8b77ae9088d311022.38_0#1666821800; mk_epub=%7B%22btuid%22%3A%221tloi73%22%2C%22eVar1%22%3A%22iphone%2012%20pro%20-%20overview%20(us)%20%7C%20locale%20switcher%20%7C%20continue%20button%22%2C%22prop57%22%3A%22www.us.iphone12pro%22%2C%22prop25%22%3A%22locale%20switcher%22%7D; reserve-prime-2=b5cd888bd927e1ee0008a523aa227b8b; JSESSIONID=21A9B17082E09212329CAE1525E559D9; CKAFFINITY=17.179.240.2; s_ria=Flash%20Not%20Detected%7C; s_invisit_n2_us=21; myacinfo=DAWTKNV2df17613dca1f1304f073768208dfd499400beff612ae6c0730dc4b5d2f281cd04442a8f82721f6edfbd26b5b398293130e7975af56b28b3655507020f50c82a9a91d399cdbd532e305fbf522d7adfc58ac74af94a26855a4661997cf75b55cc2d2689a62ff2d95d9602225e490cfa6d072987adb3cf4829cb3e91e1df05fc36ad8f22fe98f94f3c53bddb88f1712c0509401b70dac5f9c077840200323b88672fb3b18ec96c2834adde6ff87de1860ae182778105e392b92f48c2f5f1f26805312e331b10fb9369da57c9e105075a4dacbdc502facc74e068bdae5e09d4e5e5ed886d565f6d0a939ffa018a169388b455c18983fcf0ea5b33e772e6ffdff89c99b1d880ad35b316e9fca8d46fac0d3566ac99074400e0ae1de328eb683026087c707d2aeb46c81ac74700376a02ea1ace1d857b518b8b63f4eb0c09f735581c6806867c27d3a36f04fde7dc7f2c42bf645c06a2dd6bb282c6dba1686cd62712a19530a5157e5e3ea3abf9295afa9061285923db2c555351d1c1384707e7158027ecd335a3354eabceb397086b1efae0bcef9723b6e0935ccf90217c3c91959e6501226a90a458f69415f65f194c7090518f9b0ad48b4a80fc9574c788d089c684f949a131b9d7a7f6c230b8912c76252273da14014a55772b3517b76e90b6b77da4c59d9aa8dcd1bac8420b75b4a2bb8c2594e4f4d6a09874ac12afe1e62cd6d0683639b717ea9976b551368d3f78dd732313361346338346436613633613765643262333636316532313761356136653933623363303039MVRYV2; s_vnum_n2_us=4%7C1%2C21%7C1; s_sq=%5B%5BB%5D%5D; s_ppv=concierge%2520-%2520my%2520reservations%2520-%25201%2520-%2520summary%2C100%2C87%2C858%2C100%3A%3E%7C200%3A%3E%7C300%3A%3E%7C400%3A%3E%7C500%3A%3E%7C600%3A%3E%7C700%3A%3E%7C800%3A%3E; s_orientationHeight=749; s_pathLength=prs%3D21%2Cretail.concierge%3D3%2C; dims=kWa44j1e3NlY5BSo9z4ofjb75PaK4Vpjt.gEngMQEjZr_WhXTA2s.XTVV26y8GGEDd5ihORoVyFGh8cmvSuCKzIlnY6xljQlpRDuVhtWJ55n9MqgXK_Pmtd0SHp815LyjaY2.rINj.rIN4WzcjftckcKyAd65hz74WySXvOxwawgCgIlNU.3Io3.Nzl998tp7ppfAaZ6m1CdC5MQjGejuTDRNziCvTDfWrJ4jB9VkqOHypZHgfLMC7Afyz.sUAuyPBAU5TCpjB44_etb_GGEOpBSKxUC56MnGWpwoNSUC53ZXnN87gq1VWH15L6hqB0KyhpAI6.D_yg1wWF9kmFxTnx9MsFr931QxXa5DsQs.xLB.Tf1cKFb4WDJQukAm4.f282pJzJ4yQhSFQ_10CygdfgFY5BNlrJNNlY5QB4bVNjMk.8UW; s_ptc=%5B%5BB%5D%5D'
    cookie_dict = {i.split("=")[0]: i.split("=")[-1] for i in cookie_str.split("; ")}
    return cookie_dict


def get_headers():
    headers = {'if-modified-since': 'Wed, 02 Oct 2019 03:49:00 GMT',
               'if-none-match': "4c0028-fbec-593e55962e300",
               'referer': 'https://reserve-prime.apple.com/CN/zh_CN/reserve/A/availability?store=R484&iUP=N&appleCare=N&rv=0&partNumber=MGLD3CH/A',
               'sec-fetch-mode': 'cors',
               'sec-fetch-site': 'same-origin',
               'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
               'accept': '*/*',
               'accept-encoding': 'gzip, deflate, br',
               'accept-language': 'zh-CN,zh;q=0.9'}
    return headers


def get_store_url():
    url = r'https://reserve-prime.apple.com/CN/zh_CN/reserve/A/stores.json'
    return url


def get_availability_model_url():
    url = r'https://reserve-prime.apple.com/CN/zh_CN/reserve/A/availability.json'
    return url
