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

Git命令速查表
---
* git add 添加至暂存区  
* git add-interactive 交互式添加  
* git apply 应用补丁
* git am 应用邮件格式补丁
* git annotate 是git blame的同义词
* git archive 文件归档打包
* git bisect 二分查找
* git blame 文件逐行追溯
* git barnch 分支管理
* git cat-file 版本库对象研究工具
* git checkout 检出到工作区、切换或创建分支,git checkout -b newbranch检出并创建新的分支
* git cherry-pick 提交拣选
* git citool 图形化提交，等同于git gui
* git clean 清楚工作区未跟踪文件
* git clone 克隆版本库
* git commit 提交
* git config 查询和修改配置（设置全局用户名以及查看配置）
* git describe 通过里程碑直观显示提交ID
* git diff 差异比较
* git difftool 图像化工具比较差异
* git fetch 获取远程版本库的提交
* git format-patch 创建邮件格式的补丁文件
* git grep 文件内容搜索定位工具
* git gui 基于Tcl/Tk的图形化工具，侧重提交等操作
* git help 帮助
* git init 初始化版本库
* git init-db* 是git init同义词
* git log 显示提交日志
* git merge 分支合并
* git mergetool 图像化冲突解决
* git mv 重命名
* git pull 拉回远程版本库的提交
* git push 推送至远程版本库
* git rebase 分支变基
* git rebase-interactive 交互式分支变基
* git reflog 分支等引用变更记录管理
* git remote 远程版本库管理
* git repo-config* git config 同义词
* git reset 重置改变分支指向git reset --hard origin/master,把本地master分支重置和origin一样。--hard是硬的不是连接方式，就是复制方式
* git rev-parse 将各种引用表示法转换为哈希值等
* git revert 反转提交
* git rm 删除文件
* git show 显示各种类型的对象
* git stage* 同义词等同于git add,将文件添加到暂存
* git stash 保存和恢复进度
* git tag 里程碑管理，也就是标签管理。

### 对象库操作相关命令
* git commit-tree 从树对象创建提交
* git hash-object 从标准输入或文件计算哈希值或创建对象
* git ls-files 显示工作区和暂存区文件
* git ls-tree 显示数对象包含的文件
* git mktag 从标注输入创建一个标签（里程碑对象）
* git mktree 从标注你输入创建一个树对象
* git read-tree 读取树对象到暂存区
* git update-index 工作区内容注册到暂存区及暂存区管理
* git unpack-file 创建临时文件包含指定blob的内容
* git write-tree 从暂存区创建一个数对象

### 应用操作相关命令
* git check-ref-format 检查引用名称是否符合规范
* git for-each-ref 引用迭代器，用于Shell编程
* git ls-remote 显示远程版本库的引用
* git name-rev 将提交ID显示未友好名称
* git peek-remote* 废弃的命令，被git ls-remote替代
* git rev-list 显示版本范围
* git show-branch 侠士分支列表及拓扑关系
* git show-ref 显示本地引用
* git symbolic-ref 显示或者设置符号引用
* git update-ref 更新引用的指向
* git verify-tag 校验GPG签名的Tag

### 版本库管理命令
* git count-objects 显示松散对象的数量和磁盘占用
* git filter-branch 版本库重构
* git fsck 对象库完整性检查
* git gc 版本库存储优化
* git index-pack 从打包文件创建爱你对应的索引文件
* git lost-found* 废弃命令，被git fsck --lost-found替代
* git pack-objects 从标注你输入读取对象ID，打包到文件
* git pack-redundant 查找多余的pack文件
* git pack-refs 将引用打包到.git/packed-refs文件中
* git prune 从对象库删除过期的对象
* git prune-packed 将已经打包的松散对象删除
* git relink 将本地版本库中相同的对象建立硬链接
* git repack 将版本库未打包的松散对象打包
* git show-index 读取包的索引文件，显示打包文件中的内容
* git unpack-objects 从打包文件释放文件
* git verify-pack 校验对象库打包文件

### 协议相关命令
* git daemon 启动后台守护进程
* git http-backend 创建HTTP协议的CGI守护程序
* git instaweb 即时启动浏览器通过gitweb浏览当前版本库
* git shell 收限制的shell,提供仅执行git命令的ssh访问
* git update-server-info 显示协议需要的辅助文件
* git http-fetch 通过HTTP协议获取版本库
* git http-push 通过HTTP/DAV协议推送


### 合并相关的辅助命令
* git merge-base 提供其他脚本调用，找到两个或多个提交最近的共同祖先
* git merge-file 针对文件的两个不同版本执行三向文件合并
* git merge-index 对index中的冲突文件调用指定的冲突解决工具
* git merge-octopus 合并两个以上的分支

### 其它
* git var 显示Git环境变量
* git diff-tree



# 设置Git用户
git config --global user.email "you@example.com"
git config --global user.name "Your Name"

git commit -a -m 'init project2'
git remote add origin git@xxx:project2.git
git push origin master

git pull




# Gitosis安装
sudo apt-get install -y gitcore
git clone git://github.com/res0nat0r/gitosis.git
cd gitosis
sudo python setup.py install

## 创建git用户，所有的仓库都存放在git用户名下
sudo adduser --shell /bin/bash --home /home/git git
### 在git用户下生成密钥，不输入密码
ssh-keygen -t rsa
初始化gitosis套件
sudo -H -u gitosis gitosis-init < id_dsa.pub

### 修改gitosis设置
git clone git@gitserver:/home/git/repositories/gitosis-admin.git
克隆系统设置

### 也可以使用其它主机上行的账号进行此操作，但需要设置用户名
git config --global user.name git
## 复制客户机的id_rsa.pub到git服务器的git用户下的~/.ssh/authorized_keys中，这样可以免密码登陆
## 测试免密码登陆使用ssh git@gitserver测试即可。

## Gitosis会在系统root账户下创建一个gitosis-admin目录其中存放keydir登陆

## Gitosis真实的项目文件存放地点
/home/git/repositories/
如果需要新增项目，则
cd /home/git/repositories
mkdir ent-sms.git
cd ent-sms.git
git init
touch readme.md
git add .
git commit -a -m "Initialize Repo..."


## 然后到客户机
git clone git@gitserver:/home/git/repositories/ent-sms.git
就克隆到本地了，
然后你可以把已经存在的项目拷贝过来然后
git add .
即可


## 新增项目
### 新增仓库需要在服务器操作，并设置gitosis-admin中设置
# Gitosis用户必须使用完整路径否则会提示找不到仓库
* 在blueice用户下，而仓库在git@raspberrypi的真实路径下,配置这个用户名必须是git主机的有效用户名
* git config --global user.name blueice
* git config --global user.email "blueicesir@gmail.com"



* git clone git@raspberrypi:/home/git/repositories/gitosis-admin.git
* 把远程配置同步到本地之后，把你需要增加的id_rsa.pub文件复制到keydir目录中，重名名为git主机上的用户名例如pi@raspberrypi.pub
* git add .
* git commit -a -m "add pi@raspberrypi.pub"
* git push
* 这样gitosis后台会自动增加你新增的公钥到git用户目录~/.ssh/authorized_keys中，格式是特定的！
* 如果要授权某个用户访问特定的项目需要修改gitosis-admin目录下的gitosis.conf配置文件
* 新增仓库
[group newrepo]
writable = 你的项目名称，在/home/git/repositories/目录下，目录需要有.git后缀，而项目名称这里不需要.git后缀
members = 这里就是你的keydir目录中的除去.pub的文件名，例如如果存在pi@raspberrypi.pub目录，这里就写pi@raspberrypi，多个用户使用空格分隔


* 例如我的仓库名称是 ent-sms，相关命令如下：
mkdir /home/git/repositories/ent-sms.git
cd /home/git/repositories/ent-sms.git
git init
touch readme.md
echo "Hello" > raedme.md
git add .
git commit -a -m "initialize"

* 在客户机上
git clone git@raspberrypi:/home/git/repositories/ent-sms.git

gitosis-admin.git配置参考如下：
[group ent-sms]
writable = ent-sms
writable = pi@raspberrypi blueice@raspberrypi



##如果是自己的项目之前采用的只读方式clone的，想切换到非只读模式修改配置即可
### 查看配置
#### 默认git config -e会调用nano编辑器，如果需指定编辑器需呀设置环境变量，这个设置对crontab -e也生效
* export EDITOR=vim
* git config --list
* 修改[remote]中的remote.origin.url条目
* 只读模式是
* remote.origin.url=git://github.com/blueicesir/utils.git
* 修改为
* remote.origin.url=git@github.com:blueicesir/utils.git
* 之后就可以使用git push进行更新了。
* 只读模式需要写完整的
* git push git@github.com:blueicesir/utils.git


---
Git命令手札
* git reset --hard 重置当前branch
* git checkout 只会改变HEAD，不会改变影响当前branch

* 对特定文件忽略不添加和提交到版本库中
* .gitignore 这个文件会push到服务器上
* .git/info/exclude 这个完全工作在本地，不会被push到服务器上

* git config --global core.autocrlf true 版本库中使用LF，检出时使用CRLF
* git config --global core.autocrlf input 检出时使用LF

* git revert 不会改变历史，而是生成一个新的commit来反转指定的commit中的change
* git reset -- filename 用于使用HEAD中的filename覆盖index中的新版本
* git branch -D master 无法删除当前所在分支
* git ls-files -s 显示当前staged的object的状态


## 忽略版本库中的文件，且不被版本库提交的内容显示.gitignore这个无法满足
* 在版本库目录中存在一个.git/info/exclude文件，把需要不添加到版本库的文件加入到这个文件即可，这样git push不会有任何信息提交到版本库中。

## 对于已经git add添加之后的文件需要忽略，则使用
* git update-index --assume-unchanged -- path/to/file 启用忽略
* git update-index --no-assume-unchanged -- path/to/file 停用忽略


## 不想提交直接checkout到其它branch
* git stash save [message] 保存当前工作进度
* git stash list 查看已经保存的工作进度
* git stash apply [--index] [stash] 恢复指定的工作进度
* git stash pop [--index] [stash] 恢复指定的工作进度，并从进度列表中删除
* git stash drop [stash] 删除一个存储的工作
* git stash clear 删除所有存储的进度

## git filter-branch命令
* git filter-branch --tree-filter 'rm filename' HEAD 把filename指定的文件从历史中永久删除
* git filter-branch --index-filter 'git rm --cached --ignore-unmatch filename' HEAD


