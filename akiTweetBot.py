# -*- coding: utf-8 -*-

# akiTweetBot.py
# Created by Akihiro Yamada on 2018/10/27.
# Copyright (c) 2018. All Rights Reserved.

import twitter

configFileName = '../.ApiConfig'
confingFile = open(configFileName)

lines = confingFile.read()

keys = lines.split(",")

consumerKey = str(keys[0])
consumerSecret = str(keys[1])
token = str(keys[2])
tokenSecret = str(keys[3])


# keyとtokenを設定。
api = twitter.api.Api(consumer_key=consumerKey, 
                     consumer_secret=consumerSecret, 
                     access_token_key=token, 
                     access_token_secret=tokenSecret)

api.PostUpdates("テスト投稿!")