import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
import os.path
import telegram
import asyncio
bot = telegram.Bot(token='7216096099:AAFN-2lH6-IAjVhdhDk5MXJy75p8KFsXiKg')

async def main(item_id, name, price, description, link):
    async with bot:
        await bot.send_message(text=f'ID: {item_id}\n\nName: {name}\n\nPrice: {price}\n\nDescription: {description}\n\nLink: {link}', chat_id='984091159')


def item_scraping(item_id, link):
    driverForLinks.get(link)
    clickButton("x9f619.x1n2onr6.x1ja2u2z.x78zum5.xdt5ytf.x193iq5w.xeuugli.x1iyjqo2.xs83m0k.x150jy0e.x1e558r4.xjkvuk6.x1iorvi4.xdl72j9", driverForLinks)
    time.sleep(1)
    clickButton("x92rtbv.x10l6tqk.x1tk7jg1.x1vjfegm", driverForLinks)
    time.sleep(5)   
    name = driverForLinks.find_elements(By.CLASS_NAME,  "x193iq5w.xeuugli.x13faqbe.x1vvkbs.x1xmvt09.x1lliihq.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.x14z4hjw.x3x7a5m.xngnso2.x1qb5hxa.x1xlr1w8.xzsf02u")
    price = driverForLinks.find_elements(By.CLASS_NAME,  "x193iq5w.xeuugli.x13faqbe.x1vvkbs.x1xmvt09.x1lliihq.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.xudqn12.x676frb.x1lkfr7t.x1lbecb7.xk50ysn.xzsf02u")
    description = driverForLinks.find_element(By.CLASS_NAME,  "x1n2onr6.x1ja2u2z.x9f619.x78zum5.xdt5ytf.x2lah0s.x193iq5w.xx6bls6.x1jx94hy")

    # name = WebDriverWait(driverForLinks, 5).until(
    #     EC.element_to_be_clickable((By.CLASS_NAME, "x1i10hfl.xjbqb8w.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.x1heor9g.x1sur9pj.xkrqix3.x1lku1pv.x193iq5w.xeuugli.x13faqbe.x1vvkbs.x1xmvt09.x1lliihq.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.xudqn12.x676frb.x1lkfr7t.x1lbecb7.xk50ysn.xzsf02u.x14z4hjw.x3x7a5m.xngnso2.x1qb5hxa.x1xlr1w8.xzsf02u"))
    # )
    # price = WebDriverWait(driverForLinks, 5).until(
    #     EC.element_to_be_clickable((By.CLASS_NAME, "x1i10hfl.xjbqb8w.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.x1heor9g.x1sur9pj.xkrqix3.x1lku1pv.x193iq5w.xeuugli.x13faqbe.x1vvkbs.x1xmvt09.x1lliihq.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.xudqn12.x676frb.x1lkfr7t.x1lbecb7.xk50ysn.xzsf02u"))
    # )
    # description = WebDriverWait(driverForLinks, 5).until(
    #     EC.element_to_be_clickable((By.CLASS_NAME, "x1i10hfl.xjbqb8w.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.x1heor9g.x1sur9pj.xkrqix3.x1lku1pv.x193iq5w.xeuugli.x13faqbe.x1vvkbs.x1xmvt09.x1lliihq.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.xudqn12.x676frb.x1lkfr7t.x1lbecb7.xk50ysn.xzsf02u.x3x7a5m.x6prxxf.xvq8zen.xo1l8bm.xzsf02u"))
    # )
    
    # print(name.text, price.text)
    print(name[1].text)
    print("----")
    print(price[1].text)
    print("----")
    print(description.text)
    data[str(item_id)] = {"name" : name[1].text, "price": price[1].text, "description": description.text, "link": link}
    writeToJSONFile('./','savedData', data)
    asyncio.run(main(item_id, name[1].text, price[1].text, description.text, link))
    print("__________%s____________"% i)


def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)


def clickButton(buttonClass, driver):
    try:
        try:
            button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CLASS_NAME, buttonClass))
            )
        except:
            print("NO cookies button popped out")
        else:
            button.click()
    except Exception as error: 
        print(f"ERROR: {error}")


profile_path = r'C:\Users\nickkendz\AppData\Local\Google\Chrome\User Data\Guest Profile'
profile_path_2 = r'C:\Users\nickkendz\AppData\Local\Google\Chrome\User Data\Profile 6'

options = uc.ChromeOptions() 
options.headless = False
# options.add_argument(f"user-data-dir={profile_path}")
crome_options = uc.ChromeOptions() 
crome_options.headless = False
# crome_options.add_argument(f"user-data-dir={profile_path_2}")

driver = uc.Chrome(options=options) 
driverForLinks = uc.Chrome(options=crome_options) 

item_id = 0
i = 100 
cookies = 1

linksChecked = []
data = {}

if os.path.exists('./savedData.json'):
    with open('./savedData.json', 'r') as file:
        data = json.load(file)
    for item in data:
        linksChecked.append(data[""+item+""]["link"])
        item_id = int(item)

while i!=0:
    pages = 0

    with driver:
        driver.get("https://www.facebook.com/marketplace/category/computers")
        clickButton("disc-wrapper", driver)
    time.sleep(2)

    while pages!=1 and driver.find_elements(By.CSS_SELECTOR, "[role='link']"):
        if cookies == 1:
            clickButton("x9f619.x1n2onr6.x1ja2u2z.x78zum5.xdt5ytf.x193iq5w.xeuugli.x1iyjqo2.xs83m0k.x150jy0e.x1e558r4.xjkvuk6.x1iorvi4.xdl72j9", driver)
            time.sleep(1)
            clickButton("x92rtbv.x10l6tqk.x1tk7jg1.x1vjfegm", driver)
            time.sleep(1)
            clickButton("x92rtbv.x10l6tqk.x1tk7jg1.x1vjfegm", driver)
            cookies = 0
        for item in driver.find_elements(By.CSS_SELECTOR, ".x1i10hfl.xjbqb8w.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.x1heor9g.x1sur9pj.xkrqix3.x1lku1pv"):
            if item.get_attribute("href") not in linksChecked:
                linksChecked.append(item.get_attribute("href"))
                item_scraping(item_id, item.get_attribute("href"))
                item_id = item_id+1
        pages=pages+1
        # driver.find_element(By.CSS_SELECTOR, "[data-q='pagination-forward-page']").click()
        time.sleep(2)
    i = i-1

# driver.quit()
# driverForLinks.quit()
