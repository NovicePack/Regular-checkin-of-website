# 关于

## 需求

- 服务器上的Python版本为 3.+
- 服务器上安装requests包和apscheduler包

` pip install requests` 

`pip install apscheduler`

## 主要功能

实现Python脚本放置服务器每天早上六点一次签到

## 配置

1.登录[curls转python代码](https://curl.trillworks.com/)网站

2.打开需要签到的网站，F12调出抓包工具，切到Network一栏，单击签到，找到签到的包名右键Copy as cURL，编辑项目脚本代码，替换掉以下代码中

```python
 #替换以下内容
        url = ''
        cookies = {
            'td_cookie': '3760',
            'uid': '47',
            'email': 'ie',
            'key': '1b7a82383c82d8eeb398a1d894',
            'ip': '432e005cb15a43d9dcc',
            'expire_in': '16332',
            'PHPSESSID': 'purdvqpf',
            'crisp-client%2Fcf0e': 'session_90b24fa7-08f9-458ebb',
        }
        headers = {
            'Connection': 'ke,
            'Content-Length': '0',
            'Accept': 'applicatn, */*',
            'User-Agent': 'MozillKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
            'Origin': 'httury',
            'Referer': 'htt/user',
            'Accept-Language': 'zh-=0.9',
        }
        params = (
            ('c', '88157'),
        )
        response = requests.post(url, headers=headers, params=params, cookies=cookies, verify=False)
        # 替换以上内容
```

3.更改签到时间

hour 后面数字更改为自己想要的时间

`cronTrigger = CronTrigger(hour=6)` 

## 运行

1.将脚本上传到服务器中

服务器自行购买，学生可以买阿里云学生机

https://developer.aliyun.com/plan/grow-up

1.安装需求包

3.运行脚本并放置后台中

```shell
nohup python robot.py
```

这时你可以查看进程

```shell
ps -ef | grep python
```

![img](https://img-blog.csdnimg.cn/20190410193901230.png)

代码已经运行起来了，这个就是在后台运行，关闭连接之后一样会运行。

然后就可以愉快的玩耍了。:=)

