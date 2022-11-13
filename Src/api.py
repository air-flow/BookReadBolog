import requests
import json
import pprint
import urllib.parse
import xml.etree.ElementTree as ET
import xmltodict
import json


def CallApi(book_name):
    result = ""
    URL = "https://iss.ndl.go.jp/api/sru"
    return result


if __name__ == "__main__":
    url = 'https://iss.ndl.go.jp/api/opensearch'
    params = {'title': 'AWSではじめるデータレイク',
              "cnt": 5}
    res = requests.get(url, params=params)
    # print(params)
    # pprint.pprint(res.text)
    # xml_str = res.text
    # element = ET.fromstring(xml_str)
    # ET.dump(element)
    element = xmltodict.parse(res.text)
    pprint.pprint(element["rss"]["channel"]["item"][1])
