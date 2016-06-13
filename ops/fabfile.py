# coding=utf-8
"""
fabric自动化部署

    :copyright: (c) 2016 by fangpeng(@beginman.cn).
    :license: MIT, see LICENSE for more details.
"""
from fabric.api import local, env, cd, run
from fabric.context_managers import prefix


def production():
    """设置生成环境"""
    env.hosts = ["production@123.123.123.123:2500"]
    env.password = "12345"


def test():
    """设置测试环境"""
    env.hosts = ["root@192.168.1.120:22"]
    env.password="!qaz2wsx"


def prepare():
    """ 本地提交代码，准备部署 """
    local("git pull")           # local 用于执行本地命令
    local("pip freeze > requirements.txt")
    local("git add -p && git commit")   # 交互输入 commit message
    local("git push")

def update():
    """ 服务器上更新代码、依赖和迁移 """
    # cd 用于在服务器上执行 cd 命令，本地环境对应的 api 是 lcd (local cd)
    with cd("/path/to/project"), prefix("workon project"):  # workon project 进入virtualenv环境
        run("git pull")     # run 用于服务器上执行命令
        run("pip install -r requirements.txt")
        run("python manage.py db migrate")
        run("supervisorctl restart project")


def deploy():
    prepare()
    update()


"""
# 部署到 production 环境
$ fab production deploy

# 部署到 test 环境
$ fab test deploy
"""
