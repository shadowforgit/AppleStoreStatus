import requests
import json
from retrying import retry


@retry(stop_max_attempt_number=10)
def get_availability():
    url = r'https://reserve-prime.apple.com/CN/zh_CN/reserve/A/availability.json'
    cookie_str = r'xp_ci=3z3jhG67zDTNz59pz9TdzeRVpYbyw; dssid2=fe373e97-bc4b-48bf-a5a3-ef1832e42960; dssf=1; s_fid=7E2F9E594F02B56B-0797C2457F688562; pxro=1; s_vi=[CS]v1|2EC06E5B852E444F-60000C53E001B629[CE]; as_cn=~76hTp59vCaZ8F20sOOkgc19RUr2ly-EoKQkLzYBb03Y=; as_affl=p238%7C%7Cmtid%3A%3A18707vxu38484%26mnid%3A%3A9YDjuZgc_mtid_18707vxu38484%26cid%3A%3Aaos-cn-kwba-brand-bz%26%7C%7C20190917_061955; as_loc=b92208ff0fdcb7caad0fe5607a300a8c8f5a2097f45f27148c2616f9693ee3ef706d21342ae50e5af9835508eb74bb6cf7c9457b764284c23f996422bfbc5ce96e94ea94fbff69a1f622c181961ae5328f18ea37f43b83f2815c45d45d2e41d4f69f68d1e992dbab89cd728a3d0c1957ae858db109afb49dae3b8834c42eb800d3f5c02b2f39644ffe21e3d43feb0899; dslang=CN-ZH; acn01=NWZtU1g4ex/BQSeuVJ4UeH5j9h8dpsm91gATiu2X7wQc; as_disa=AAAjAAABAA0YaY7RuYQyRGu_uzpPSuo8ZFC07z3hdz6wMntE9HBx0Fzjz6zk2v3toxOsn1IuAAIBB5qhdyp8_5GARbNJNA6BgSuLWh1ohvK0Yq6dpB_Odjo=; as_rec=e6eab5fce107044fe6aabd96e574a8cfe433e4136def69ea64ff772ec2d83ac9c8584b335fa7b816d3daaf372e653f62c85bc2d62cf547feb097a9bd0416087420fd0752e5561311213af5dd785a683d; POD=cn~zh; s_vnum_n2_us=4%7C1; geo=CN; ccl=wcJJ0gxvJdFEUhO2fU8LQQ==; check=true; s_cc=true; mbox=session#323a9d03523149f0aea1b3d830cb1b83#1569989440|PC#323a9d03523149f0aea1b3d830cb1b83.22_17#1633232380; as_pcts=tKUqW2yNVzy-9GpOEHOfmBm+MOrwxh7QDm_Azoc5LvU1Lncy48d5qpYUwwSw:FZhIsqht1; as_sfa=Mnxjbnxjbnx8emhfQ058Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE=; s_sq=%5B%5BB%5D%5D; s_ptc=%5B%5BB%5D%5D; dims=VWa44j1e3NlY5BSo9z4ofjb75PaK4Vpjt.gEngMQEjZr_WhXTA2s.XTVV26y8GGEDd5ihORoVyFGh8cmvSuCKzIlnY6xljQlpRD__htduVCbqWxf7_OLgiPFMJhHFW_jftckkCoqAkCoq0NUuAuyPB94UXuGlfUm0NUbNiqUU8jA2Q3wL6k03x0.5EwHXXTSHCSPmtd0wVYPIG_qvoPfybYb5EvYTrYesSAAQnIp.QEh2vLG9mhORoVijvw2WwjftckhwOsrLwkJLLfaTK43xbJlpMpwoNSUC56MnGWpwoNHHACVZXnN9N6QhpvHav91azLu_dYV6HzL0TFc4NO7TjOy_Aw7Q_v9NA2pW5Dtfs.xLB.Tf1X6Nsg8mjf.j7J1gBZEJebtIEnSfe2RjOI0NFgBFY5BNlrJNNlY5QB4bVNjMk.EyM'
    cookie_dict = {i.split("=")[0]: i.split("=")[-1] for i in cookie_str.split("; ")}
    headers = {'if-modified-since': 'Wed, 02 Oct 2019 03:49:00 GMT',
              'if-none-match': "4c0028-fbec-593e55962e300",
              'referer': 'https://reserve-prime.apple.com/CN/zh_CN/reserve/A/availability?&iUP=N&appleCare=N&rv=1&path=/cn/shop/buy-iphone/iphone-11-pro/MWDH2CH/A&partNumber=MWDH2CH/A',
              'sec-fetch-mode': 'cors',
              'sec-fetch-site': 'same-origin',
              'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
               'accept': '*/*',
               'accept-encoding': 'gzip, deflate, br',
               'accept-language': 'zh-CN,zh;q=0.9'}
    res = requests.get(url, cookies=cookie_dict, headers=headers).content
    j_res = json.loads(res)
    return j_res


if __name__ == '__main__':
    res = get_availability()
    print(res)
