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
            "headline": "## 言語",
            "key_name": "language"
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
    print(template_data)


def add(data: list, headline: str, add_data: str):
    add_index = data.index(headline) + 2
    data.insert(add_index, add_data)
    return data


if __name__ == "__main__":
    MDMain()
