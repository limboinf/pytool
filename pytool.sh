#!/bin/bash
echo "Git仓库准备中……"
git pull origin master;
git add -A;
echo "填写日志："
read log
git ci -m "$log";
git push origin master;
echo "PUSH完成!"

