#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import urllib.request
import json
import sys
import time
from  wechat_conf import CorpID, Agentid, Secret

localtime = time.strftime("[%H:%M:%S]", time.localtime())
dl="\n-------------------------------------\n"
class Tencent(object):
    def __init__(self,user,title,msg):
        # 格式化输出内容：标题+内容
        self.MSG = localtime+title+dl+msg
        self.User = user
        self.url = 'https://qyapi.weixin.qq.com'
        self.send_msg = json.dumps({
            "touser": self.User,
            "msgtype": 'text',
            "agentid": Agentid,
            "text": {'content': self.MSG},
            "safe": 0
        })
    # 获取tokent
    def get_token(self):
        token_url = '%s/cgi-bin/gettoken?corpid=%s&corpsecret=%s' % (self.url, CorpID, Secret)
        token = json.loads(urllib.request.urlopen(token_url).read())['access_token']
        return token

    # 发送信息
    def send_message(self):
        send_url = '%s/cgi-bin/message/send?access_token=%s' % (self.url,self.get_token())
        respone = urllib.request.urlopen(urllib.request.Request(url=send_url, data=self.send_msg)).read()
        x = json.loads(respone.decode())['errcode']
        if x == 0:
            print ('Succesfully')
        else:
            print ('Failed')

# 创建对象
send_obj = Tencent(sys.argv[1],sys.argv[2],sys.argv[3])
# 调用发送函数
send_obj.send_message()