ubuntu搭建python开发环境

(1)安装IDE，安装的是VScode
1、从官网下载压缩包
访问Visual Studio Code官网 https://code.visualstudio.com/docs?dv=linux64

2.解压 ,如果文件名不对,可能解压不出来的(扩展名:tar.gz)

    1 tar xzvf + 要解压的包

3.然后移动到 /usr/local/ 目录

    1 mv VSCode-linux-x64 /usr/local/

4.可能还需要给可执行的权限, 然后就已经可以运行了

    1 chmod +x /usr/local/VSCode-linux-x64/code

5.复制一个VScode图标文件到 /usr/share/icons/ 目录(后面会有用)

    1 cp /usr/local/VSCode-linux-x64/resources/app/resources/linux/code.png /usr/share/icons/

6.创建启动器, 在/usr/share/applications/ 目录, 也可以将它复制到桌面目录
直接在终端使用命令:

    1 vim /usr/share/applications/VSCode.desktop

然后输入以下文本:

    1 [Desktop Entry]
    2 Name=Visual Studio Code
    3 Comment=Multi-platform code editor for Linux
    4 Exec=/usr/local/VSCode-linux-x64/code
    5 Icon=/usr/share/icons/code.png
    6 Type=Application
    7 StartupNotify=true
    8 Categories=TextEditor;Development;Utility;
    9 MimeType=text/plain;

执行授予执行权限：

    1 sudo chmod +x  /usr/local/VSCode-linux-x64/code

再把图标复制到桌面

    1 cp /usr/share/applications/VSCode.desktop ~/桌面/

之后 就会发现 桌面和 应用程序菜单都有了 VSCode的快捷方式了












