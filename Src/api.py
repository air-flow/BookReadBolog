import requests
import json
import pprint
import urllib.parse
import xml.etree.ElementTree as ET
import xmltodict
import json


def APICall(book_name, cnt=5) -> dict:
    result = ""
    URL = "https://iss.ndl.go.jp/api/opensearch"
    params = {
        'title': book_name,
        "cnt": cnt}
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
    if int(data["rss"]["channel"]["openSearch:totalResults"]) <= 1:
        print(ERROR_MESSAGE)
        return False
    return True


def APIShaping(book_data) -> dict:
    item = book_data["rss"]["channel"]["item"][1]
    response = {
        "price": item['dcndl:price'],
        "title": item['title'],
        "publisher": item['dc:publisher'],
        "date": item['dc:date'],
        "page": TakeOutPageData(item["dc:extent"]),
        "language": "日本語"
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

if __name__ == "__main__":
    result = APIMain("awsではじめるデータレイク")
    pprint.pprint(result)
