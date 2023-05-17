# -*- coding:utf-8-*-
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage, FriendMessage
from graia.ariadne.message.chain import MessageChain, Source, At
from graia.ariadne.model import Member, Friend, Group
from collections import Counter

from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
import os
with open("badwords/fls.txt", "r", encoding="UTF-8") as f: #这里填写你的词库
    fls = f.read().splitlines()
with open("badwords/sex.txt", "r", encoding="UTF-8") as f:
    sex = f.read().splitlines()
with open("badwords/politic.txt", "r", encoding="UTF-8") as f:
    plt = f.read().splitlines()
channel = Channel.current()
@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def getup(app: Ariadne,
                message: MessageChain,
                source: Source,
                member: Member,
                group: Group):
    md = message.display
    if any(fl in md for fl in fls):
        if not os.path.exists("chlist"):
            os.mkdir("chlist")
        with open("chlist/{0}.txt".format(member.id), "a", encoding="UTF-8") as f: #做一个简易数据库，powerd by txt
            f.write("\n")
        with open("chlist/{0}.txt".format(member.id), "r", encoding="UTF-8") as f:
            r = f.readlines()
            wns = len(r) #计算群员违规的次数
            if wns <= 3:
                await app.recall_message(source.id)
                await app.send_group_message(group.id,
                MessageChain(At(member.id),
                " 你发送的内容包含粗口，警告第",
                str(wns),
                "次"))
                f.close() #这个必填，不然会内存溢出
            else:
                await app.recall_message(source.id)
                await app.send_group_message(group.id,
                    MessageChain(At(member.id),
                    " 你已经发送多次粗口,已举报给管理员\ncc", At(2581144729), At(1634967892), At(3412515002), At(3564646312))) #因为无法获取并私聊管理员,请在这里填写管理员
    if any(fl in md for fl in sex):
        if not os.path.exists("chlist"):
            os.mkdir("sexlist")
        with open("sexlist/{0}.txt".format(member.id), "a", encoding="UTF-8") as f: #做一个简易数据库，powerd by txt
            f.write("\n")
        with open("sexlist/{0}.txt".format(member.id), "r", encoding="UTF-8") as f:
            r = f.readlines()
            wns = len(r) #计算群员违规的次数
            if wns <= 3:
                await app.recall_message(source.id)
                await app.send_group_message(group.id,
                MessageChain(At(member.id),
                " 你发送的内容包含色情词汇，警告第",
                str(wns),
                "次"))
                f.close() #这个必填，不然会内存溢出
            else:
                await app.recall_message(source.id)
                await app.send_group_message(group.id,
                    MessageChain(At(member.id),
                    " 你已经发送多次色情词汇,已举报给管理员\ncc", At(2581144729), At(1634967892), At(3412515002), At(3564646312))) #因为无法获取并私聊管理员,请在这里填写管理员
    if any(fl in md for fl in plt):
        await app.recall_message(source.id)
        await app.send_group_message(group.id,
            MessageChain(At(member.id),
            " 你发送了政治敏感词汇，已向管理员举报\ncc", At(2581144729), At(1634967892), At(3412515002), At(3564646312))) #因为无法获取并私聊管理员,请在这里填写管理员