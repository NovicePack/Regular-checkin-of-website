import requests
import time
from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
def main():
    try:
        #以下内容复制粘贴
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
        # 以上内容复制粘贴
    except Exception:
        a = time.ctime()[4:].replace(' ', '-')
        with open('signIn_logs.txt', mode='a', encoding='utf-8') as f:
            f.write(str(a) + ' 失败' + '\n')
            f.close()
        print('签到失败！等待下一天早上六点签到')
    else:
        a = time.ctime()[4:].replace(' ', '-')
        with open('signIn_logs.txt', mode='a', encoding='utf-8') as f:
            f.write(str(a) + ' 成功' + '\n')
            f.close()
        print('签到成功！等待下一天早上六点签到')
if __name__ == '__main__':
    print('等待早上六点签到中')
    scheduler = BlockingScheduler()
    cronTrigger = CronTrigger(hour=6)
    scheduler.add_job(main, cronTrigger, id='每天一签到')
    scheduler.start()
