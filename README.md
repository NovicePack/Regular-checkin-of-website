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
        url = 'http://a.luxury/user/checkin'
        cookies = {
            'td_cookie': '3753938660',
            'uid': '1602747',
            'email': 'novice',
            'key': '1b7a89fbcd8cd74553c5a68b2383c82d8eeb398a1d894',
            'ip': '432e00a605f95d7747c5cb15a43d9dcc',
            'expire_in': '1633018232',
            'PHPSESSID': 'puhjurmdrl6hpa68kevprdvqpf',
            'crisp-client%2Fsession%2F57fad162-9de4-4d4b-94ba-c5c2f345cf0e': 'session_90b24fa7-08f9-4cd9-ac90-7f8cbc758ebb',
        }
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '0',
            'Accept': 'application/json, text/plain, */*',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
            'Origin': 'http://a.luxury',
            'Referer': 'http://a.luxury/user',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        params = (
            ('c', '0.6313279893588157'),
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
