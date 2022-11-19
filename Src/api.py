import requests
import json
import pprint
import urllib.parse
import xml.etree.ElementTree as ET
import xmltodict
import json


def APICall(book_name, cnt=1) -> dict:
    result = ""
    URL = "https://iss.ndl.go.jp/api/opensearch"
    params = {
        'title': book_name,
        "cnt": cnt,
        "dpid": "iss-ndl-opac"}
    res = requests.get(URL, params=params)
    if res.status_code != 200:
        print("ERROR HTTP GET")
        return result
    result = xmltodict.parse(res.text)
    # result = res_json["rss"]["channel"]["item"][1]
    return result


def APIValidationCheck(data) -> bool:
    ERROR_MESSAGE = "ERROR Not Result"
    if len(data) == 0:
        print(ERROR_MESSAGE)
        return False
    if int(data["rss"]["channel"]["openSearch:totalResults"]) <= 0:
        print(ERROR_MESSAGE)
        return False
    return True


def APIShaping(book_data) -> dict:
    item = book_data["rss"]["channel"]["item"]
    response = {
        "price": item['dcndl:price'],
        "title": item['title'],
        "publisher": item['dc:publisher'],
        "date": item['dc:date'],
        "page": TakeOutPageData(item["dc:extent"])
    }
    return response


def TakeOutPageData(data):
    return data.split(";")[0].strip()


def APIMain(book_name) -> dict:
    result = {"status": False}
    book_data = APICall(book_name)
    if not APIValidationCheck(book_data):
        return result
    result["data"] = APIShaping(book_data)
    result["status"] = True
    return result


def TestIssue1(book_name="事業をエンジニアリングする技術者たち ― フルサイクル開発者がつくるCARTAの現場"):
    book_data = APICall(book_name)
    # book_data = book_data["rss"]["channel"]["item"]
    pprint.pprint(book_data)


if __name__ == "__main__":
    TestIssue1()
    # result = APIMain("エンジニアリングマネージャーのしごと")
    # pprint.pprint(result)
#     {'data': {'date': '2022.8',
#           'page': '350p',
#           'price': '3400円',
#           'publisher': ['オライリー・ジャパン', 'オーム社 (発売)'],
#           'title': 'エンジニアリングマネージャーのしごと : チームが必要とするマネージャーになる方法'},
#  'status': True}
