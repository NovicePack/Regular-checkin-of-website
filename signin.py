import requests
import time
from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
def main():
    try:
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
