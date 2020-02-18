# 单词本的服务器



## Http 请求表

---

### 添加新单词

* **方法**

    post

* **表单**

    user = "用户名"

    words  =  "如下`json` 数组"

    ```json
    [
        {
            "word":"good",
        	"soundMark":"/good/",
            "mean":"好的",
            "sentence":"I am very good.",
            "time":12345678
        },
        ......
    ]
    ```

    

* **返回**

    `json` 数据，如下:

    ```json
    {
        "failNum":2,
        "words":
        [
            {
                "word":"good",
                "reason":"已存在"
            },
            {
                "word":"nice",
                "reason":"已存在"
            }
        ]
    }
    ```



### 获取更新

* **方法**

    `GET`

* **URL**

    ?user=用户名

* **返回**

    ```json
    [
        {
            单词数据
        },
        ...
    ]
    ```

    



## 服务器逻辑

---

### 添加新单词

* 先查找单词是否已存在

* 每个单词添加下面这两个属性

    ```json
    {
        "user" : "xxx",
        "modifyTime" : 1234567
    }
    ```

* 将单词插入数据库



### 获取更新

* 根据用户标识，查找用户上次更新时间
* 查找数据库中，更改时间在更新时间之后，且添加者不是该用户的所有单词
* 将单词以 `json` 格式发给客户端



### 更新单词数据

一定要把该单词的用户也更新，不然获取更新的逻辑会出错



## 数据库

---

mongodb 数据库，共两个集合

### users 集合

用来存储用户的相关数据

```json
{
    "user":"pc-1",
    "updateTime":12345678	// 用户上一次更新的时间
}
```



### words 集合

用来存储单词数据

```json
{
    "word":"good",
    "soundMark":"/good/",
    "mean":"好的",
    "sentence":"I am very good.",
    "time":12345678,					// 单词的记录时间
    "user" : "xxx",						// 添加或修改该单词的用户
    "modifyTime":12345678,				// 单词加入（修改）数据库的时间
    
}
```



​    