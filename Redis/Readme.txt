Redis官方并不支持在Windows平台下部署Redis服务器，但是微软团队开发出包用于在Windows上部署
详细见地址：https://github.com/MicrosoftArchive/redis/releases（64位包和未编译源码）
而且微软官方并不提供32位的部署，因此需要下载源码用vs编译一个windows32的包
同时加上了安装和卸载服务的bat（也可以不加，不加的话就是用命令行来实现），
直接解压缩到服务器的目录，分配NETWORK SERVICE权限，运行service-install.bat即可完成安装。

将获取的包解压，在cmd窗口，移动到解压包所在目录
运行Redis> redis-server.exe redis.windows.conf

将redis加入环境变量就不需要每次都输入路径了

redis.conf中 默认 bind 127.0.0.1 这样的话，就只能本地访问
要让远程客户端也能访问该redis服务器，改为bind 0.0.0.0或者直接将该行用#注释掉
然后将保护模式关闭，重启服务器就行了，当然这样会有很大的安全漏洞
这时就需要设置密码了，找到redis服务器的redis.conf，找到
# require pass foobared
将#去掉，foobared改成你想设置的密码。
redis-cli -h<host ip default 127.0.0.1> -p<port default 6379> -a<password> -help


redis还可以安装成windows服务，开机自动启动，命令如下：
redis-server --service-install redis.windows.conf
启动命令： redis-server --service-start
停止命令： redis-server --service-stop

还可以安装多个实例：
redis-server --service-install -service-name redisService1 -port 10001
redis-server --service-start -service-name redisService1
redis-server --service-install -service-name redisService2 -port 10002
redis-server --service-start -service-name redisService2

卸载命令
redis-server --service-uninstall