import pkgutil

from creart import create
from graia.ariadne.app import Ariadne
from graia.ariadne.connection.config import (
    HttpClientConfig,
    WebsocketClientConfig,
    config,
)
from graia.saya import Saya

import os

saya = create(Saya)
app = Ariadne(
    connection=config(
        3512942073,  # 你的机器人的 qq 号
        "114514",  # 填入你的 mirai-api-http 配置中的 verifyKey
        # 以下两行（不含注释）里的 host 参数的地址
        # 是你的 mirai-api-http 地址中的地址与端口
        # 他们默认为 "http://localhost:8080"
        # 如果你 mirai-api-http 的地址与端口也是 localhost:8080
        # 就可以删掉这两行，否则需要修改为 mirai-api-http 的地址与端口
        HttpClientConfig(host="http://127.0.0.1:8080"),
        WebsocketClientConfig(host="ws://127.0.0.1:8080"),
    ),
)

with saya.module_context():
    saya.require("modules.ch")

app.launch_blocking()