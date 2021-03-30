### Flask 几种获取json data的方式

Ajax 请求不来源于 form 提交，flask 的 request.form 是拿不到数据的，只能通过以下几种方式拿到数据：

1. #### 获取未经处理过的原始数据而不管内容类型,如果数据格式是json的，则取得的是json字符串，排序和请求参数一致

```python
request.get_data()
```

以 get_data() 拿到的数据，将会变成 bytes 对象，如：

```python
b'{'name': 'alma'}'
```

此时需引入 json 模块，再次重新将其以 json 形式转为 dict（如果 data 是 json）：

```python
json.loads(request.get_data())
```

#### 2.将请求参数做了处理，得到的是字典格式的，因此排序会打乱依据字典排序规则

```python
request.get_json()
```

#### 3.可以获取未经处理过的原始数据，如果数据格式是json的，则取得的是json字符串，排序和请求参数一致

```python
request.data
```

#### 4.将请求参数做了处理，得到的是字典格式的，因此排序会打乱依据字典排序规则

```python
data = request.json
print(data['key'])
```

————————————————
版权声明：本文为CSDN博主「cloudhand」的原创文章转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/cloudhand/article/details/102055296