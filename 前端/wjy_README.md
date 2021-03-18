<i>2021.3.16</i>

## VUE安装

https://blog.csdn.net/Smile_Sunny521/article/details/89714388?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522161589924816780255248521%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=161589924816780255248521&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_click~default-1-89714388.pc_search_result_cache&utm_term=vue%E5%AE%89%E8%A3%85

node.js环境 

npm 资源下载工具(安装好node.js后查看)

vue-cli vue脚手架

webpack 资源管理

yarn   facebook发布的一款取代npm的包管理工具。



## VUE新建项目

### 使用vue-cli 2.0

安装 npm i -g vue-cli

新建 <b>vue init webpack 项目名</b>

![image-20210316210029840](C:\Users\12876\AppData\Roaming\Typora\typora-user-images\image-20210316210029840.png)

运行 npm run dev

目录结构分析：

https://blog.csdn.net/bbsyi/article/details/77897278?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522161591196116780262514851%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=161591196116780262514851&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-1-77897278.pc_search_result_cache&utm_term=vue-cli2.0%E7%9B%AE%E5%BD%95%E7%BB%93%E6%9E%84

![image-20210317002943073](C:\Users\12876\AppData\Roaming\Typora\typora-user-images\image-20210317002943073.png)

### 使用vue-cli 3.0

安装 npm install -g @vue/cli

新建 <b>vue create 项目名</b>

运行 npm run server

![在这里插入图片描述](https://img-blog.csdnimg.cn/20191016130616116.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2FwamN1aQ==,size_16,color_FFFFFF,t_70)

目录结构分析：

https://www.cnblogs.com/coober/p/10875647.html

![image-20210317004712709](C:\Users\12876\AppData\Roaming\Typora\typora-user-images\image-20210317004712709.png)

ps: vue-cli3.0的目录比2.0的精简很多：

- public文件夹相当于2.0的static文件夹
- 默认目录没有build和config这两个文件夹
- <b>需要配置webpack则需要在项目的根目录下新建 vue.config.js 文件</b>（是根目录，不是src目录）
- /src/views 新建我们的页面组件



<i>2021.3.17</i>

vue-cli3.0全面配置 有对vue.config.js配置的说明

https://segmentfault.com/a/1190000017008697

<b>代码格式化 Eslint：</b>

- ESLint 

   一个开源的 JavaScript 代码检查工具，它是用来进行代码的校验，检测代码中潜在的问题，比如某个变量定义了未使用、函数定义的参数重复、变量名没有按规范命名等等。
  ESLint 的初衷是为了让程序员可以创建自己的检测规则。ESLint 的所有规则都被设计成可插入的。ESLint 的默认规则与其他的插件并没有什么区别，规则本身和测试可以依赖于同样的模式。为了便于人们使用，ESLint 内置了一些规则，当然，你可以在使用过程中自定义规则。
  ESLint 使用 Node.js 编写，这样既可以有一个快速的运行环境的同时也便于安装。 (重点，使用eslint必须有package.json文件)

- Prettier
  它是代码格式化工具，用来做代码格式化，有了Prettier之后，它能去掉原始的代码风格，确保团队的代码使用统一相同的格式，修复规则可自定义。

​	配置setting.json:

```javascript
{

  // vscode默认启用了根据文件类型自动设置tabsize的选项

  "editor.detectIndentation": false,

  // 重新设定tabsize

  "editor.tabSize": 2,

  // #每次保存的时候自动格式化 

  "editor.formatOnSave": true,

  // #每次保存的时候将代码按eslint格式进行修复

  "eslint.autoFixOnSave": true,

  // 添加 vue 支持

  "eslint.validate": [

   "javascript",

   "javascriptreact",

   {

​    "language": "vue",

​    "autoFix": true

   }

  ],

  // #让prettier使用eslint的代码格式进行校验 

  "prettier.eslintIntegration": true,

  // #去掉代码结尾的分号 

  "prettier.semi": false,

  // #使用带引号替代双引号 

  "prettier.singleQuote": true,

  // #让函数(名)和后面的括号之间加个空格

  "javascript.format.insertSpaceBeforeFunctionParenthesis": true,

  // #这个按用户自身习惯选择 

  "vetur.format.defaultFormatter.html": "js-beautify-html",

  // #让vue中的js按编辑器自带的ts格式进行格式化 

  "vetur.format.defaultFormatter.js": "vscode-typescript",

  "vetur.format.defaultFormatterOptions": {

   "js-beautify-html": {

​    "wrap_attributes": "force-aligned"

​    // #vue组件中html代码格式化样式

   }

  },

  // 格式化stylus, 需安装Manta's Stylus Supremacy插件

  "stylusSupremacy.insertColons": false, // 是否插入冒号

  "stylusSupremacy.insertSemicolons": false, // 是否插入分好

  "stylusSupremacy.insertBraces": false, // 是否插入大括号

  "stylusSupremacy.insertNewLineAroundImports": false, // import之后是否换行

  "stylusSupremacy.insertNewLineAroundBlocks": false,

  "editor.suggestSelection": "first",

  "vsintellicode.modify.editor.suggestSelection": "automaticallyOverrodeDefaultValue",

  "editor.codeActionsOnSave": {

   "source.fixAll.eslint": true

  } // 两个选择器中是否换行

 }

```



<i>2021.3.18</i>

## VUE Router 路由

官方文档 https://router.vuejs.org/zh/installation.html

### 1 编写 ./src/router/index.js

- routes 为一数组，每个路由都是一个对象，用大括号包裹，其主要参数如下：
- path ：跳转的路径，相当于 Spring MVC 中 Controller 中 return 的路径
- name ：自定义的组件名称
- component ：引入的 Vue 组件名称

```js
import Vue from 'vue'
import VueRouter from 'vue-router'

// 组件通过export暴露接口，路由中导入组件
import Login from '../components/Login'
import Main from '../components/Main'
import Register from '../components/Register'

// 导入 vue-router 依赖
Vue.use(VueRouter);

export default new VueRouter({
    routes: [
        {
            path: '/login',   // 跳转路径
            name: 'login',    // 名称
            component: Login  // 组件
        },
        {
            path: '/main',
            name: 'main',
            component: Main
        },
        {
            path: '/register',
            name: 'register',
            component: Register
        }
    ]
});
```



### 2 在主文件main.js 中引入路由

import router from './router'

### 3 添加 router-link 以及 router-view

router-link 相当于 a 标签， to 属性相当于 href 属性，用于配置路由中声明的路径，即对应 index.js 中路由的 path，匹配成功则进行跳转切换
router-view 用于展示视图，要通过它才能将跳转的视图展示出来

```javascript
<template>
  <div id="app">
      <router-link to="/main">Main</router-link>
      <router-link to="/login">Login</router-link>
      <router-link to="/register">Register</router-link>
      <router-view></router-view>
  </div>
</template>
```



### 4 传递参数

#### route-link 中 to

```js
//修改 App.vue 中 route-link 的 to 属性，让其携带参数：

<router-link :to="{name:'login', params:{id:1}}">Login</router-link>

// 修改 index.js 中的路由的 path 属性

{
    path: '/login/:id',   // 跳转路径
    name: 'login',    // 名称
    component: Login  // 组件
},
```



#### 路由配置增加props

```js
// 在 index.js 的路由配置中增加 “props: true” 属性

{
     path: '/login/:id',   // 跳转路径
     name: 'login',    // 名称
     component: Login,  // 组件
     props: true
 },

// 在 Login.vue 中通过 props 接受 id 参数

<script>
export default {
    props: ['id'],
    name: 'Main'
}
</script>

```



### 5 重定向

添加 redirect 属性即可

```javascript
// 修改路由中 register 的配置，删掉 Component，用 redirect 取代，路径为 “/Main”，即重定向至 Main
{
    path: '/register',
    redirect: '/main'
}
```



### 6 404跳转处理

新建组件notFound.vue

然后在index.js多添加一个路由：

```js
{
    path: '*',//匹配所有请求
    component: NotFound 
}
```



## Axios

官方文档：http://www.axios-js.com/zh-cn/

### 1 简介

基于`promise`，用于浏览器和`node.js`的http客户端，本质上也是对原生XHR的封装，只不过它是Promise的实现版本，符合最新的ES规范，有以下特点：

- 从浏览器中创建 XMLHttpRequests
- 从 node.js 创建 http 请求
- 支持 Promise API
- 拦截请求和响应
- 转换请求数据和响应数据
- 取消请求
- 自动转换 JSON 数据
- 客户端支持防御 XSRF

与Ajax区别：http://www.axios-js.com/zh-cn/blogs/

axios是通过promise实现对ajax技术的一种封装，就像jQuery实现ajax封装一样。
简单来说： ajax技术实现了网页的局部数据刷新，axios实现了对ajax的封装。axios是ajax，但ajax不止axios。

代码比较：

```js
//axios：
axios({
            url: '/getUsers',
            method: 'get',
            responseType: 'json', // 默认的
            data: {
                //'a': 1,
                //'b': 2,
            }
        }).then(function (response) {
            console.log(response);
            console.log(response.data);
        }).catch(function (error) {
            console.log(error);
            }）

// ajax：
$.ajax({
            url: '/getUsers',
            type: 'get',
            dataType: 'json',
            data: {
                //'a': 1,
                //'b': 2,
            },
            success: function (response) {
                console.log(response)；
            }
        })
```



### 2 安装

npm install axios --save

在main.js中引入：

```js
import axios from 'axios'
Vue.prototype.$axios = axios
```



### 3 请求方法

- get：获取数据，请求指定的信息，返回实体对象
- post：向指定资源提交数据（例如表单提交或文件上传）
- put：更新数据，从客户端向服务器传送的数据取代指定的文档的内容
- patch：更新数据，是对put方法的补充，用来对已知资源进行局部更新
- delete：请求服务器删除指定的数据



### 4 并发请求

同时进行多个请求，并统一处理返回值

```js
this.$axios.all([
	this.$axios.get('/goods.json'),
	this.$axios.get('/classify.json')
]).then(
	this.$axios.spread((goodsRes,classifyRes)=>{
		console.log(goodsRes.data);
		console.log(classifyRes.data);
	})
)
```

