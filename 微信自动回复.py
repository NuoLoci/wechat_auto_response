import random
import re

from wxpy import *

#将缓存功能启动，避免频繁扫码登陆
bot = Bot(cache_path = True)

'''
    获取所有的好友列表，如果只要单一的选定好友，请将代码改写成下列形式:
        name = bot.friends.search('好友名字')
        found = ensure_one(name)
    之后需要将reply函数前的函数装饰器(@bot.register()函数)替换为下列形式：
        @bot.register([found,bot.self],except_self = False)
    此时就可以指定对某一些人使用自动回复功能了
'''
found = bot.friends(update=False)

#使用字典形式设置自动回复规则，利用了正则表达式，可以自行添加规则
rules = {
    r'[.+]?干啥呢':'[自动回复]要么在吃，要么在玩',
    r'[.+]?在吗':'[自动回复]现在忙的要死，可能得晚一点才能回复你！',
    r'.+[怎么|如何]安排':'[自动回复]怎么都行，你说了算',
    r'作业写完了吗':'[自动回复]你再问就该绝交了'
}

'''
    此函数中采取了文字匹配返回发送文字的方法，
    你也可以使用表情包（图片）来自动回复，
    具体方式如下：
        1：将想要回复的图片放置在picture文件夹中
        2：先执行一次picture.py(该函数能帮你自动将图片文件名写出为txt文件)
        3：接下来在reply函数前插入以下代码：
            with open('picture.txt') as pic:
                picread = pic.read()
            pic.close()
            P = picread.split('\n')
        4：此时P即为文件名列表，可以直接调用
        5：如果想随机回复一个表情包，只需要添加一行代码：
            msg.sender.send_image(random.choice(P))
'''

@bot.register(found)
def reply(msg):
    sign = True
    for rule in rules:
        if re.match(rule,msg.text):
            try:
                msg.sender.send_msg(rules[rule])
                sign = False
                break
            except:
                pass
    if sign:
        msg.sender.send_msg('[自动回复]你好，该微信主人暂时比较忙，请稍等一会再找他')
        
            
#此函数起到阻塞线程，不会执行一次就中断程序的效果
embed()
