#创建用户

###添加用户git
adduser --system --shell /bin/bash --group git
adduser git ssh

git clone git://github.com/ossxp-com/gitolite.git


sudo adduser --system --shell /bin/bash --gecos 'git version control' --group --disabled-password --home /home/git git

sudo ssh-keygen rsa 
sudo -H -u git gitosis-init < id_rsa.pub
