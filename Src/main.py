import os
import api
import pprint
import markdown
import env
def cd():
    os.chdir(os.path.dirname(__file__))


def Main(SEARCH_BOOK_NAME):
    cd()
    # SEARCH_BOOK_NAME = "システム運用アンチパターン"
    # OUTPUT_FILE_PAHT = "output file path"
    data = api.APIMain(SEARCH_BOOK_NAME)
    if data["status"]:
        print(markdown.MDMain(
            data["data"],
            env.OUTPUT_FILE_PAHT + SEARCH_BOOK_NAME
        ))
    else:
        print(data["status"], "Book Data Error")


def MainCreateBooksList(books_list: list):
    for i in books_list:
        Main(i)


if __name__ == "__main__":
    books_list = [
        "システム運用アンチパターン",
        # "エンジニアリングマネージャーのしごと",
        # "ネットワークがよくわかる教科書",
        # "プロダクトマネジメントのすべて",
        # "事業をエンジニアリングする技術者たち",
    ]
    # Main("システム運用アンチパターン")
    MainCreateBooksList(books_list)
    
