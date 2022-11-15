import os
import api
import pprint

def cd():
    os.chdir(os.path.dirname(__file__))


if __name__ == "__main__":
    cd()
    pprint.pprint(api.APIMain("awsではじめるデータレイク"))
    
