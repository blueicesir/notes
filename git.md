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
+git add 添加至暂存区
+git add-interactive 交互式添加
+git apply 应用补丁
git am 应用邮件格式补丁
git annotate 是git blame的同义词
git archive 文件归档打包
git bisect 二分查找
git blame 文件逐行追溯
git barnch 分支管理
git cat-file 版本库对象研究工具
git checkout 检出到工作区、切换或创建分支,git checkout -b newbranch检出并创建新的分支
git cherry-pick 提交拣选
git citool 图形化提交，等同于git gui
git clean 清楚工作区未跟踪文件
git clone 克隆版本库
git commit 提交
git config 查询和修改配置（设置全局用户名以及查看配置）
git describe 通过里程碑直观显示提交ID
git diff 差异比较
git difftool 图像化工具比较差异
git fetch 获取远程版本库的提交
git format-patch 创建邮件格式的补丁文件
git grep 文件内容搜索定位工具
git gui 基于Tcl/Tk的图形化工具，侧重提交等操作
git help 帮助
git init 初始化版本库
git init-db* 是git init同义词
git log 显示提交日志
git merge 分支合并
git mergetool 图像化冲突解决
git mv 重命名
git pull 拉回远程版本库的提交
git push 推送至远程版本库
git rebase 分支变基
git rebase-interactive 交互式分支变基
git reflog 分支等引用变更记录管理
git remote 远程版本库管理
git repo-config* git config 同义词
git reset 重置改变分支指向git reset --hard origin/master,把本地master分支重置和origin一样。--hard是硬的不是连接方式，就是复制方式
git rev-parse 将各种引用表示法转换为哈希值等
git revert 反转提交
git rm 删除文件
git show 显示各种类型的对象
git stage* 同义词等同于git add,将文件添加到暂存
git stash 保存和恢复进度
git tag 里程碑管理，也就是标签管理。

### 对象库操作相关命令
git commit-tree 从树对象创建提交
git hash-object 从标准输入或文件计算哈希值或创建对象
git ls-files 显示工作区和暂存区文件
git ls-tree 显示数对象包含的文件
git mktag 从标注输入创建一个标签（里程碑对象）
git mktree 从标注你输入创建一个树对象
git read-tree 读取树对象到暂存区
git update-index 工作区内容注册到暂存区及暂存区管理
git unpack-file 创建临时文件包含指定blob的内容
git write-tree 从暂存区创建一个数对象

### 应用操作相关命令
git check-ref-format 检查引用名称是否符合规范
git for-each-ref 引用迭代器，用于Shell编程
git ls-remote 显示远程版本库的引用
git name-rev 将提交ID显示未友好名称
git peek-remote* 废弃的命令，被git ls-remote替代
git rev-list 显示版本范围
git show-branch 侠士分支列表及拓扑关系
git show-ref 显示本地引用
git symbolic-ref 显示或者设置符号引用
git update-ref 更新引用的指向
git verify-tag 校验GPG签名的Tag

### 版本库管理命令
git count-objects 显示松散对象的数量和磁盘占用
git filter-branch 版本库重构
git fsck 对象库完整性检查
git gc 版本库存储优化
git index-pack 从打包文件创建爱你对应的索引文件
git lost-found* 废弃命令，被git fsck --lost-found替代
git pack-objects 从标注你输入读取对象ID，打包到文件
git pack-redundant 查找多余的pack文件
git pack-refs 将引用打包到.git/packed-refs文件中
git prune 从对象库删除过期的对象
git prune-packed 将已经打包的松散对象删除
git relink 将本地版本库中相同的对象建立硬链接
git repack 将版本库未打包的松散对象打包
git show-index 读取包的索引文件，显示打包文件中的内容
git unpack-objects 从打包文件释放文件
git verify-pack 校验对象库打包文件

### 协议相关命令
git daemon 启动后台守护进程
git http-backend 创建HTTP协议的CGI守护程序
git instaweb 即时启动浏览器通过gitweb浏览当前版本库
git shell 收限制的shell,提供仅执行git命令的ssh访问
git update-server-info 显示协议需要的辅助文件
git http-fetch 通过HTTP协议获取版本库
git http-push 通过HTTP/DAV协议推送


### 合并相关的辅助命令
git merge-base 提供其他脚本调用，找到两个或多个提交最近的共同祖先
git merge-file 针对文件的两个不同版本执行三向文件合并
git merge-index 对index中的冲突文件调用指定的冲突解决工具
git merge-octopus 合并两个以上的分支

### 其它
git var 显示Git环境变量
git diff-tree

