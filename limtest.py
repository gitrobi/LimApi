import os
import time
import configparser
# back_path = "/Users/abc/PycharmProjects/Pythoncoding/projects/"
# back_file ="hello.txt"
# 可以写为读取配置文件
# 第一步：创建conf对象

def write_ini():
    conf = configparser.ConfigParser()
    # 第二步：添加section、options的值
    conf.add_section("path")
    conf.set("path", "back_dir", "/Users/abc/PycharmProjects/Pythoncoding/projects/")  # option
    conf.set("path", "target_dir", "/Users/abc/PycharmProjects/Pythoncoding/")  # option
    conf.add_section("file")
    conf.set("file", "back_file", "apitest")

    # 第三步：写入文件
    with open("path.ini", 'w')as conffile:
        conf.write(conffile)


def read_ini():
    conf = configparser.ConfigParser()
    conf.read('LimConfig.ini')

    print('key')
    for key in conf.keys():
        print(key)

    print('section')
    for section in conf.sections():
        #print(section)
        for option in conf.options(section):
            print('{} = {}'.format(option, conf.get(section, option)))




read_ini()



