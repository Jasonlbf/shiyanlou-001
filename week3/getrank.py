#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from pymongo import MongoClient
from bson.son import SON

def get_rank(user_id):
    client = MongoClient()
    db = client.shiyanlou
    contests = db.contests
 
    pipline =  [{'$group':{'_id':'$user_id','score':{'$sum':'$score'},
                 'submit_time':{'$sum':'$submit_time'}}},
                 {'$sort':SON([('score',-1),('submit_time',1)])}]

    res = contests.aggregate(pipline)
    li = list(res)

    for i,k in enumerate(li):
        if k['_id'] == user_id:
            return i+1,k['score'],k['submit_time']

if __name__ == '__main__':

    user_id = 0
    try:
        user_id = int(sys.argv[1])
        print(user_id)
    except:
        print("Parameter Error")
    userdata = get_rank(user_id)
    print(userdata)
