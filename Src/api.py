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


def TestIssue1(book_name="エンジニアリングマネージャーのしごと"):
    book_data = APICall(book_name)
    pprint.pprint(book_data)


if __name__ == "__main__":
    TestIssue1()
    # result = APIMain("エンジニアリングマネージャーのしごと")
    # pprint.pprint(result)
    a = {'rss': {
        '@version': '2.0',
        '@xmlns:dc': 'http://purl.org/dc/elements/1.1/',
        '@xmlns:dcmitype': 'http://purl.org/dc/dcmitype/',
        '@xmlns:dcndl': 'http://ndl.go.jp/dcndl/terms/',
        '@xmlns:dcterms': 'http://purl.org/dc/terms/',
        '@xmlns:openSearch': 'http://a9.com/-/spec/opensearchrss/1.0/',
        '@xmlns:rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
        '@xmlns:rdfs': 'http://www.w3.org/2000/01/rdf-schema#',
        '@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
        'channel': {'description': 'Search results for '
                    'title=エンジニアリングマネージャーのしごと cnt=5',
                    'item': [
                        {'author': 'James Stanier 著,吉羽龍太郎, 永瀬美穂, 原田騎郎, '
                          '竹葉美沙 訳,Stanier, James,吉羽, 龍太郎,永瀬, '
                          '美穂,原田, 騎郎,竹葉, 美沙,',
                          'category': '本',
                          'dc:creator': ['Stanier, James',
                                         '吉羽, 龍太郎',
                                         '永瀬, 美穂',
                                         '原田, 騎郎',
                                         '竹葉, 美沙'],
                          'dc:date': '2022.8',
                          'dc:description': ['原タイトル: Become an Effective '
                                             'Software Engineering '
                                             'Manager',
                                             '機器種別 : 機器不用',
                                             'キャリア種別 : 冊子',
                                             '表現種別 : テキスト',
                                             '文献あり 索引あり',
                                             'NDC（9版）はNDC（10版）を自動変換した値である。'],
                          'dc:extent': '350p ; 24cm',
                          'dc:identifier': [{'#text': '9784873119946',
                                             '@xsi:type': 'dcndl:ISBN'},
                                            {'#text': '032321746',
                                             '@xsi:type': 'dcndl:NDLBibID'},
                                            {'#text': '23733738',
                                             '@xsi:type': 'dcndl:JPNO'},
                                            {'#text': '34375248',
                                             '@xsi:type': 'dcndl:TOHANMARCNO'}],
                          'dc:publisher': ['オライリー・ジャパン', 'オーム社 (発売)'],
                          'dc:subject': ['コンピュータ要員',
                                         '管理者',
                                         {'#text': 'DK411',
                                          '@xsi:type': 'dcndl:NDLC'},
                                         {'#text': '007.35',
                                          '@xsi:type': 'dcndl:NDC10'},
                                         {'#text': '007.35',
                                          '@xsi:type': 'dcndl:NDC9'}],
                          'dc:title': 'エンジニアリングマネージャーのしごと : '
                          'チームが必要とするマネージャーになる方法',
                          'dcndl:creatorTranscription': ['ヨシバ, リュウタロウ',
                                                         'ナガセ, ミホ',
                                                         'ハラダ, キロウ',
                                                         'タケバ, ミサ'],
                          'dcndl:price': '3400円',
                          'dcndl:titleTranscription': 'エンジニアリング マネージャー ノ '
                          'シゴト : チーム ガ ヒツヨウ ト '
                          'スル マネージャー ニ ナル '
                          'ホウホウ',
                          'dcterms:issued': {'#text': '2022',
                                             '@xsi:type': 'dcterms:W3CDTF'},
                          'description': '<p>オライリー・ジャパン,9784873119946</p>\n'
                          '<ul><li>タイトル： '
                          'エンジニアリングマネージャーのしごと : '
                          'チームが必要とするマネージャーになる方法</li>\n'
                          '<li>タイトル（読み）： エンジニアリング マネージャー ノ '
                          'シゴト : チーム ガ ヒツヨウ ト スル マネージャー ニ '
                          'ナル ホウホウ</li>\n'
                          '<li>責任表示： James Stanier '
                          '著,吉羽龍太郎, 永瀬美穂, 原田騎郎, 竹葉美沙 '
                          '訳,</li>\n'
                          '<li>NDC(10)： 007.35</li>\n'
                          '<li>NDC(9)： 007.35</li>\n'
                          '</ul>',
                          'guid': {'#text': 'https://iss.ndl.go.jp/books/R100000002-I032321746-00',
                                   '@isPermaLink': 'true'},
                          'link': 'https://iss.ndl.go.jp/books/R100000002-I032321746-00',
                          'pubDate': 'Thu, 22 Sep 2022 09:00:00 +0900',
                          'rdfs:seeAlso': [{'@rdf:resource': 'http://id.ndl.go.jp/bib/032321746'},
                                           {'@rdf:resource': 'https://www.library.pref.osaka.jp/licsxp-opac/WOpacMsgNewListToTifTilDetailAction.do?tilcod=10021401254199'},
                                           {'@rdf:resource': 'http://www.shiga-pref-library.jp/wo/opc_srh/srh_detail/4874877/'},
                                           {'@rdf:resource': 'https://www.lib-sakai.jp/licsxp-opac/WOpacMsgNewListToTifTilDetailAction.do?tilcod=1007001234625'},
                                           {'@rdf:resource': 'https://www.lib.city.saitama.jp/bookdetail?num=3227291&ctg=1'},
                                           {'@rdf:resource': 'https://web.oml.city.osaka.lg.jp/webopac_i_ja/0015249120'},
                                           {'@rdf:resource': 'https://www.apl.pref.akita.jp/licsxp-opac/WOpacMsgNewListToTifTilDetailAction.do?tilcod=1009920958327'},
                                           {'@rdf:resource': 'https://www.library.pref.kyoto.jp/bib/?B12183186'},
                                           {'@rdf:resource': 'https://opac.lib.city.yokohama.lg.jp/opac/OPP1500?SELDATA=TOSHO&SSNO=3-0500990895'},
                                           {'@rdf:resource': 'https://catalog.library.metro.tokyo.lg.jp/winj/opac/switch-detail-iccap.do?bibid=1154057625'},
                                           {'@rdf:resource': 'https://www.library.pref.ishikawa.lg.jp/wo/opc_srh/srh_detail/1000001532586/'}],
                          'title': 'エンジニアリングマネージャーのしごと : '
                          'チームが必要とするマネージャーになる方法'},
                        {'author': 'James Stanier著 ; 吉羽龍太郎 [ほか] '
                         '訳,Stanier, James,吉羽, 龍太郎,',
                         'category': '本',
                         'dc:creator': ['Stanier, James', '吉羽, 龍太郎'],
                         'dc:date': '2022.8',
                         'dc:description': ['その他の訳者: 永瀬美穂, 原田騎郎, 竹葉美沙',
                                            '参考文献: p339-342'],
                         'dc:extent': ['xxiv, 350p', '24cm'],
                         'dc:identifier': [{'#text': '9784873119946',
                                            '@xsi:type': 'dcndl:ISBN'},
                                           {'#text': 'BC16503916',
                                            '@xsi:type': 'dcndl:NIIBibID'}],
                         'dc:publisher': ['オライリー・ジャパン', 'オーム社 (発売)'],
                         'dc:subject': ['情報産業',
                                        '情報処理技術者',
                                        '管理者(経営管理)',
                                        'コンピュータ要員',
                                        '管理者',
                                        {'#text': 'DK411',
                                         '@xsi:type': 'dcndl:NDLC'},
                                        {'#text': '007.35',
                                         '@xsi:type': 'dcndl:NDC10'},
                                        {'#text': '007.35',
                                         '@xsi:type': 'dcndl:NDC9'}],
                         'dc:title': 'エンジニアリングマネージャーのしごと : '
                         'チームが必要とするマネージャーになる方法',
                         'dcndl:creatorTranscription': 'ヨシバ, リュウタロウ',
                         'dcndl:titleTranscription': 'エンジニアリング マネージャー ノ '
                         'シゴト : チーム ガ ヒツヨウ ト '
                         'スル マネージャー ニ ナル '
                         'ホウホウ',
                         'dcterms:issued': {'#text': '2022',
                                            '@xsi:type': 'dcterms:W3CDTF'},
                         'description': '<p>オライリー・ジャパン,9784873119946</p>\n'
                         '<ul><li>タイトル： '
                         'エンジニアリングマネージャーのしごと : '
                         'チームが必要とするマネージャーになる方法</li>\n'
                         '<li>タイトル（読み）： エンジニアリング マネージャー ノ '
                         'シゴト : チーム ガ ヒツヨウ ト スル マネージャー ニ '
                         'ナル ホウホウ</li>\n'
                         '<li>責任表示： James Stanier著 ; '
                         '吉羽龍太郎 [ほか] 訳,</li>\n'
                         '<li>NDC(10)： 007.35</li>\n'
                         '<li>NDC(9)： 007.35</li>\n'
                         '</ul>',
                         'guid': {'#text': 'https://iss.ndl.go.jp/books/R100000096-I012844508-00',
                                   '@isPermaLink': 'true'},
                         'link': 'https://iss.ndl.go.jp/books/R100000096-I012844508-00',
                         'rdfs:seeAlso': {'@rdf:resource': 'https://ci.nii.ac.jp/ncid/BC16503916'},
                         'title': 'エンジニアリングマネージャーのしごと : '
                         'チームが必要とするマネージャーになる方法'}],
                     'language': 'ja',
                     'link': 'https://iss.ndl.go.jp/api/opensearch?cnt=5&title=%E3%82%A8%E3%83%B3%E3%82%B8%E3%83%8B%E3%82%A2%E3%83%AA%E3%83%B3%E3%82%B0%E3%83%9E%E3%83%8D%E3%83%BC%E3%82%B8%E3%83%A3%E3%83%BC%E3%81%AE%E3%81%97%E3%81%94%E3%81%A8',
                     'openSearch:itemsPerPage': '5',
                     'openSearch:startIndex': '1',
                     'openSearch:totalResults': '2',
                     'title': 'エンジニアリングマネージャーのしごと - 国立国会図書館サーチ OpenSearch'}}}
