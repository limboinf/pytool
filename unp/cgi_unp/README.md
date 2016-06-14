# Python CGI编程

所有的HTTP服务器执行CGI程序都保存在一个预先配置的目录。这个目录被称为CGI目录，并按照惯例，它被命名为/var/www/cgi-bin目录。
CGI文件的扩展名为.cgi，python也可以使用.py扩展名。

且该目录下文件赋予可执行权限

    chmod -R 755 cgi-bin/*

其注意该目录下py格式:

    #!/usr/bin/env python
    # -*- coding: UTF-8 -*-
    ...


参考: http://www.runoob.com/python/python-cgi.html