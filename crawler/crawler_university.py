import requests

base_url = 'https://shanghairanking.cn/api/pub/v1/bcur?bcur_type=11&year=2022'

headers = {

    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "cookie": "Hm_lvt_af1fda4748dacbd3ee2e3a69c3496570=1672467774;Hm_lpvt_af1fda4748dacbd3ee2e3a69c3496570=1672469192",
    "referer": "https://shanghairanking.cn/rankings/bcur/2022",
    # "user-agent": "Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36"
}
response = requests.get(base_url, headers=headers)
print(response.json())
