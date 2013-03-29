# Git常用命令
---
### 创建Git仓库
git init

### 添加远端仓库
git remote add origin git@github.com:blueicesir/utils.git

### 查看远端分支
git branch -r

### 查看所有分支
git branch -a


### 确保在本地master分支，并提交修改到HEAD中
git checkout master
git commit -a -m "注释信息"

### 提交本地分支master到远端仓库
git push git@github.com:blueicesir/utils.git master

### 从远端仓库获取最新版本,如果省略origin默认是远端仓库
git fetch origin
git reset --hard origin/master 使用远端origin分支作为本地的master分支

### 本地仓库分支与远端同步
git pull


### 显示配置
git config --list

---
