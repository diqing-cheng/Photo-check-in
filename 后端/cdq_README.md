## 人脸识别虚拟环境的搭建

### 1.准备

一台修改了国内源的Ubuntu 18.04虚拟机

修改国内源：https://blog.csdn.net/xiangxianghehe/article/details/80112149

### 2.安装python3

一般Ubuntu 18.04都会自带python3，使用以下命令检测python3的版本

```shell
python3 --version
```

安装pip3

```shell
sudo apt-get isntall python3-pip
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

### 6.安装dlib(需要在venv虚拟环境下)

dlib是一个包含机器学习算法的C++开源工具包

在安装dlib之前，确认cmake已经安装：

```shell
cmake --version
```

若没有安装cmake则：

```shell
sudo apt-get install cmake
```

##### 1.使用pip命令安装dlib：

```shell
pip3 install --upgrade pip
pip3 install dlib -i https://pypi.douban.com/simple
```

在 Building wheel for dlib 这个环节可能会花上一段时间，需要耐心等待

pip更改国内原只需要在平时的命令后加上`-i  *国内源*`,如

```shell
pip3 install dlib 
```


##### 2.或者根据下面这篇博客安装dlib

##### https://blog.csdn.net/qq_43006346/article/details/103326514

1) 在官网下载源文件

https://pypi.org/project/dlib/#history

2) 解压，然后运行

```shell
sudo python3 setup.py install
```

注意解压命令 :

```shell
tar -xzvf 文件名.tar.gz
```

### 7.安装face_recognition(需要在venv虚拟环境下)

```shell
pip3 install face_recognition -i https://mirrors.aliyun.com/pypi/simple/
```

## 使用方法

### 命令行界面

当你安装好了本项目，你可以使用两种命令行工具：

- `face_recognition` - 在单张图片或一个图片文件夹中认出是谁的脸。
- `face_detection` - 在单张图片或一个图片文件夹中定位人脸位置。

#### 

#### `face_recognition` 命令行工具

`face_recognition`命令行工具可以在单张图片或一个图片文件夹中认出是谁的脸。

首先，你得有一个你已经知道名字的人脸图片文件夹，一个人一张图，图片的文件名即为对应的人的名字：

[![known](https://cloud.githubusercontent.com/assets/896692/23582466/8324810e-00df-11e7-82cf-41515eba704d.png)](https://cloud.githubusercontent.com/assets/896692/23582466/8324810e-00df-11e7-82cf-41515eba704d.png)

然后，你需要第二个图片文件夹，文件夹里面是你希望识别的图片：

[![unknown](https://cloud.githubusercontent.com/assets/896692/23582465/81f422f8-00df-11e7-8b0d-75364f641f58.png)](https://cloud.githubusercontent.com/assets/896692/23582465/81f422f8-00df-11e7-8b0d-75364f641f58.png)

然后，你在命令行中切换到这两个文件夹所在路径，然后使用`face_recognition`命令行，传入这两个图片文件夹，然后就会输出未知图片中人的名字：

```shell
$ face_recognition ./pictures_of_people_i_know/ ./unknown_pictures/

/unknown_pictures/unknown.jpg,Barack Obama
/face_recognition_test/unknown_pictures/unknown.jpg,unknown_person
```

输出结果的每一行对应着图片中的一张脸，图片名字和对应人脸识别结果用逗号分开。

如果结果输出了`unknown_person`，那么代表这张脸没有对应上已知人脸图片文件夹中的任何一个人。

