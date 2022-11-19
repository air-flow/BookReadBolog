import api
import pprint


def NormalAPITest(book_name):
    # main.MainCall(book_name)
    pprint.pprint(api.APIMain(book_name))


if __name__ == "__main__":
    test_data = [
        "システム運用アンチパターン",
        "エンジニアリングマネージャーのしごと",
        "ネットワークがよくわかる教科書",
        "プロダクトマネジメントのすべて",
        "事業をエンジニアリングする技術者たち",
    ]
    for i in test_data:
        print("-" * 5 + " " + i + " " + "-" * 5)
        NormalAPITest(i)
