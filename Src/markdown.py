import os
import api


def MDFileRead(path: str):
    with open(path, encoding="utf-8") as target:
        md_data = target.readlines()
    return md_data


def MDFileWrite(write_data: list, path: str):
    try:
        with open(path, encoding="utf-8", mode="w") as target:
            target.writelines(write_data)
    except Exception as identifier:
        print(identifier)
        return False
    return True
def cd():
    os.chdir(os.path.dirname(__file__))


def MDMain(data, output_path):
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
    CHANGE_LIST = [
        {"BulletPoints": ["price", "page"]},
        {"ConvertPage": ["page"]},
    ]
    template_data = MDFileRead(TEMPLATE_FILE_PATH)
    data = MDChangeMarkdownData(data, CHANGE_LIST)
    template_data = MDAddMarkdownData(template_data, ADD_LIST,data)
    return MDFileWrite(template_data, output_path)


def MDChangeMarkdownData(data: list, change_list: list):
    for i in change_list:
        func_name = list(i.keys())[0]
        data_list = list(i.values())[0]
        if func_name == "BulletPoints":
            for j in data_list:
                data[j] = MDBulletPoints(data[j])
        if func_name == "ConvertPage":
            for j in data_list:
                data[j] = MDConvertPage(data[j])
    return data


def MDAddMarkdownData(template_data: list, add_list: list,data:list):
    for i in add_list:
        headline, key_name = i.values()
        template_data = MDHeadlineAddData(
            template_data, headline, data[key_name])
    return template_data


def MDHeadlineAddData(data: list, headline: str, add_data: str):
    add_index = data.index(headline + "\n") + 2
    new_line = "\n \n"
    if add_data[0] == "-":
        new_line = "\n"
    data.insert(add_index, add_data + new_line)
    return data


def MDConvertPage(data):
    return data.replace("p", "ページ")


def MDBulletPoints(data):
    return "- " + data


if __name__ == "__main__":
    data = api.APIMain("awsではじめるデータレイク")
    # print(data["data"])
    print(MDMain(data["data"]))
