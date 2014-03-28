#!/bin/bash
cd ~/桌面/pytool/;
git pull origin master;
git add .;
git ci -m "自动生成";
git push origin master;


