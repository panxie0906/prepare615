Redis�ٷ�����֧����Windowsƽ̨�²���Redis������������΢���Ŷӿ�������������Windows�ϲ���
��ϸ����ַ��https://github.com/MicrosoftArchive/redis/releases��64λ����δ����Դ�룩
����΢��ٷ������ṩ32λ�Ĳ��������Ҫ����Դ����vs����һ��windows32�İ�
ͬʱ�����˰�װ��ж�ط����bat��Ҳ���Բ��ӣ����ӵĻ���������������ʵ�֣���
ֱ�ӽ�ѹ������������Ŀ¼������NETWORK SERVICEȨ�ޣ�����service-install.bat������ɰ�װ��

����ȡ�İ���ѹ����cmd���ڣ��ƶ�����ѹ������Ŀ¼
����Redis> redis-server.exe redis.windows.conf

��redis���뻷�������Ͳ���Ҫÿ�ζ�����·����

redis.conf�� Ĭ�� bind 127.0.0.1 �����Ļ�����ֻ�ܱ��ط���
Ҫ��Զ�̿ͻ���Ҳ�ܷ��ʸ�redis����������Ϊbind 0.0.0.0����ֱ�ӽ�������#ע�͵�
Ȼ�󽫱���ģʽ�رգ����������������ˣ���Ȼ�������кܴ�İ�ȫ©��
��ʱ����Ҫ���������ˣ��ҵ�redis��������redis.conf���ҵ�
# require pass foobared
��#ȥ����foobared�ĳ��������õ����롣
redis-cli -h<host ip default 127.0.0.1> -p<port default 6379> -a<password> -help


redis�����԰�װ��windows���񣬿����Զ��������������£�
redis-server --service-install redis.windows.conf
������� redis-server --service-start
ֹͣ��� redis-server --service-stop

�����԰�װ���ʵ����
redis-server --service-install -service-name redisService1 -port 10001
redis-server --service-start -service-name redisService1
redis-server --service-install -service-name redisService2 -port 10002
redis-server --service-start -service-name redisService2

ж������
redis-server --service-uninstall