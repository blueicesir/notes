###Sublime Text 2插件安装方法

## 安装Package Control组件
Ctrl+`调出console
## 粘贴如下代码并回车
import urllib2,os;pf='Package Control.sublime-package';ipp=sublime.installed_packages_path();os.makedirs(ipp) if not os.path.exists(ipp) else None;open(os.path.join(ipp,pf),'wb').write(urllib2.urlopen('http://sublime.wbond.net/'+pf.replace(' ','%20')).read())

## 重启Sublime Text 2编辑器
##  OS X 系统的Perferences菜单在Sublime Text 2菜单下。
## 确认安装是否成功Perferences->package settings->package control

### Package Control安装插件的方法
Ctrl+Shift+P调出命令面板(OS X平台按shift+command+p)
输入install调出Install Package选项并回车。

## 输入markdown Pre安装md文件预览插件

OS X
~/Library/Application Support/Sublime Text 2


### Markdown Preview插件使用
shift+command+p
install
markdown preview
使用方法
shift+command+p
输入mp，调用markdown previewer，选择在浏览器中显示即可。


