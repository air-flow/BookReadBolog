import os


def MDFileRead(path):
    with open(path, encoding="utf-8") as target:
        md_data = target.readlines()
    return md_data


def cd():
    os.chdir(os.path.dirname(__file__))


def MDMain(data=""):
    cd()
    TEMPLATE_FILE_PATH = "../Doc/template.md"
    ADD_LIST = [
        {
            "headline": "## 発売日",
            "key_name": "date"
        },
        {
            "headline": "## 出版社",
            "key_name": "publisher"
        },
        {
            "headline": "## 単行本",
            "key_name": "price"
        },
        {
            "headline": "## 単行本",
            "key_name": "page"
        },
        {
            "headline": "# 本",
            "key_name": "title"
        },
    ]
    template_data = MDFileRead(TEMPLATE_FILE_PATH)
    test = {
        'date': '2020.7',
        'page': '377p',
        'price': '2800円',
        'publisher': 'テッキーメディア',
        'title': 'AWSではじめるデータレイク = Data Lake starting with AWS : '
        'クラウドによる統合型データリポジトリ構築入門 : クラウドを軸に統合データ基盤を作る'
    }
    for i in ADD_LIST:
        headline, key_name = i.values()
        template_data = add(template_data, headline, test[key_name])
    print(*template_data)
def add(data: list, headline: str, add_data: str):
    add_index = data.index(headline + "\n") + 2
    data.insert(add_index, add_data + "\n \n")
    return data


if __name__ == "__main__":
    MDMain()
