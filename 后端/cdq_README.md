## 人脸识别虚拟环境的搭建

### 1.准备

一台修改了国内源的Ubuntu 18.04虚拟机

修改国内源：https://blog.csdn.net/xiangxianghehe/article/details/80112149

### 2.安装python3

一般Ubuntu 18.04都会自带python3，使用以下命令检测python3的版本

```shell
python3 --version
```

### 3.安装venv

从python3.6开始，创建虚拟环境的推荐方法是使用venv。要安装提供venv模块的python3-venv包，运行以下命令

```shell
sudo apt-get update
sudo apt-get install python3-venv
sudo apt-get -y install python-pip python-setuptools python-dev
```

### 4.创建一个虚拟环境

首先，导航到要存储Python 3虚拟环境的目录。它可以是您的主目录，也可以是用户具有读写权限的任何其他目录。为项目创建一个新目录，并cd到其中，运行以下命令创建虚拟环境:

```shell
mkdir my_tensorflow
cd my_tensorflow
python3 -m venv venv
```

上面的命令创建了一个名为venv的目录，其中包含Python二进制文件的副本、Pip包管理器、标准Python库和其他支持文件。您可以为虚拟环境使用任何您想要的名称。

### 5.使用虚拟环境

在开始使用虚拟环境之前，还需要运行activate脚本来激活它：

```shell
source venv/bin/activate
```

一旦激活，虚拟环境的bin目录将被添加到$PATH变量的开头。shell的提示符也会改变，它会显示当前使用的虚拟环境的名称。这里是venv

更新pip

```shell
pip install --upgrade pip
```

