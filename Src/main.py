import os
import api
import pprint
import markdown
import env
def cd():
    os.chdir(os.path.dirname(__file__))


if __name__ == "__main__":
    cd()
    SEARCH_BOOK_NAME = "システム運用アンチパターン"
    # OUTPUT_FILE_PAHT = "output file path"
    data = api.APIMain(SEARCH_BOOK_NAME)
    if data["status"]:
        print(markdown.MDMain(data["data"],
              env.OUTPUT_FILE_PAHT + SEARCH_BOOK_NAME))
    else:
        print(data["status"], "Book Data Error")
    # pprint.pprint(api.APIMain("awsではじめるデータレイク"))
    
