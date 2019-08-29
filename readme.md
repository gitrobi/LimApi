#LimApi for Python

此接口仅为网上lim trade.exe后端服务web接口的python封装,trade.exe并不是我开发的，Please using it at your own risk!

###目录结构
LimApi.py      - Api接口程序 \
LimTest.py     - 测试主程序 \
LimConfig.ini  - service api url 定义文件 \
LimAccount.ini - 用户信息参数配置

###配置
1. 在LimAccount.ini中配置个人的券商账户信息, 请替换成自己的信息. 参考格式如下: \
[券商服务器地址，ip或域名] \
host = 100.100.100.100 \
[券商服务器端口号] \
port = 7708 \
[柜台号] \
id = 148 \
[券商账号] \
account = 111111 \
[券商交易密码] \
jypass = 111111 \
[券商通讯密码] \
txpass =

2. 在LimConfig.ini中,将server修改为自己本地服务运行的ip地址. 参考格式如下: \
server = http://192.168.1.106:80 \
如果端口不是默认的80端口,则需要修改为对应端口号, 参考格式如下: \
server = http://192.168.1.106:8080

###测试
1. 在LimConfig.ini文件中配置好券商账号信息
2. 在命令行下,直接运行主测试程序LimTest.py

###声明
此代码仅限用于个人学习和研究目的；不得将上述内容用于商业或者非法用途，否则一切后果请用户自负!!!\
本人与lim服务提供方没有任何关系, 此接口仅为lim trade.exe后端服务web接口的python封装,本接口不提供任何后端服务.
使用本接口碰到的任何问题,请自行解决.

