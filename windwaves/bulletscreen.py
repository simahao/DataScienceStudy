import json
import time

import numpy as np
import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


def get_windwaves_bullet_screen(browser: WebDriver, url_month, url_day, url_var1, url_var2):
    one_episode_bs = pd.DataFrame()
    step = 0
    print("getting bullet screen from {}-{}".format(url_month, url_day))
    time.sleep(2)
    try:
        while True:
            # construct bullet screen url address
            bullet_screen_url = "https://bullet-ws.hitv.com/bullet/2020/{}/{}/{}/{}/{}.json".format(url_month, url_day, url_var1, url_var2, step)
            browser.get(bullet_screen_url)
            data = browser.page_source
            data = data.replace('<html><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">', '')
            data = data.replace('</pre></body></html>', '')
            json_data = json.loads(data)
            rows = json_data['data']['items']
            contents = [row.get('content') for row in rows]
            thumb_up = [row.get('v2_up_count') for row in rows]
            fill = {'thumbUp': 0}
            df = pd.DataFrame({
                "date": url_month + url_day,
                "content": contents,
                "thumbUp": thumb_up
            }).fillna(value=fill).astype({'thumbUp': 'int32'})
            one_episode_bs = one_episode_bs.append(df, ignore_index=True)
            print("getting the {} page bullet screen:OK".format(step + 1))
            step += 1
    except Exception as e:
        print(e)
        print("getting the {} page bullet screen:FAILED".format(step + 1))
        print("get bullet screen data finished")
    return one_episode_bs

if __name__ == "__main__":
    url_info = np.array(\
        [["06", "21", "104556", "8337559"], \
        ["06", "25", "151545", "8398205"]])
    # construct browser object according to browser driver
    browser = webdriver.Chrome()
    for i in range(url_info.shape[0]):
        ds = get_windwaves_bullet_screen(browser=browser, url_month=url_info[i][0], \
            url_day=url_info[i][1], url_var1=url_info[i][2], url_var2=url_info[i][3])
        if i == 0:
            # new file at first time
            ds.to_csv('./windwaves/data/bullet.csv', index=False)
        else:
            # append mode
            ds.to_csv('./windwaves/data/bullet.csv', mode='a', index=False)
    browser.close()
