from script import Facebook
import pandas as pd
import numpy as np
import random
from option import details


def main(userInfo, folder):
    postCodeList = list()
    count = 16
    df = pd.read_csv(details['postCodePath'])

    for user in userInfo:
        for count in range(0, count):
            num = random.randint(0, len(df)-1)
            postCodeList.append(df.iloc[num, 0])
        print(postCodeList)
        facebookObj = Facebook(user, postCodeList, folder, count)
        facebookObj.publistListings()
        postCodeList.clear()
