import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time
import json
import os.path
import telegram
import asyncio
bot = telegram.Bot(token='7216096099:AAFN-2lH6-IAjVhdhDk5MXJy75p8KFsXiKg')

async def main(item_id, name, price, description, link):
    async with bot:
        await bot.send_message(text=f'ID: {item_id}\n\nName: {name}\n\nPrice: {price}\n\nDescription: {description}\n\nLink: {link}', chat_id='984091159')

def findElement(typeby, tag, parent):
    try:
        try:
            if typeby == "class":
                child = WebDriverWait(parent, 5).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, tag))
                )
            elif typeby == "css":
                child = WebDriverWait(parent, 5).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, tag))
                )
        except:
            print("NO element found")
        else:
            return child
    except Exception as error: 
        print(f"ERROR: {error}")


def item_scraping(item_id, link, cookiesForLinks):
    driverForLinks.get(link)
    if cookiesForLinks == True:
        removeAlert("class", "x9f619.x1n2onr6.x1ja2u2z.x78zum5.xdt5ytf.x193iq5w.xeuugli.x1iyjqo2.xs83m0k.x150jy0e.x1e558r4.xjkvuk6.x1iorvi4.xdl72j9", driverForLinks, "cookies")
    removeAlert("class", "x92rtbv.x10l6tqk.x1tk7jg1.x1vjfegm", driverForLinks, "location")

    try:
       parent1 = findElement("class", "xckqwgs.x26u7qi.x2j4hbs.x78zum5.xnp8db0.x5yr21d.x1n2onr6.xh8yej3.xzepove.x1stjdt1", driverForLinks)
       parent2 = findElement("class", "xb57i2i.x1q594ok.x5lxg6s.x78zum5.xdt5ytf.x6ikm8r.x1ja2u2z.x1pq812k.x1rohswg.xfk6m8.x1yqm8si.xjx87ck.x1l7klhg.x1iyjqo2.xs83m0k.x2lwn1j.xx8ngbg.xwo3gff.x1oyok0e.x1odjw0f.x1e4zzel.x1n2onr6.xq1qtft.xh8yej3", parent1)
       name = findElement("class", "x193iq5w.xeuugli.x13faqbe.x1vvkbs.x1xmvt09.x1lliihq.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.x14z4hjw.x3x7a5m.xngnso2.x1qb5hxa.x1xlr1w8.xzsf02u", parent2)
       price = findElement("class", "x193iq5w.xeuugli.x13faqbe.x1vvkbs.x1xmvt09.x1lliihq.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.xudqn12.x676frb.x1lkfr7t.x1lbecb7.xk50ysn.xzsf02u", parent2)
       description = findElement("class", "x1n2onr6.x1ja2u2z.x9f619.x78zum5.xdt5ytf.x2lah0s.x193iq5w.xx6bls6.x1jx94hy", driverForLinks)
    except:
        print("cant find any element info")
    else:
        print("----")
        print(name.text)
        print("----")
        print(price.text)
        print("----")
        print(description.text)
        data[str(item_id)] = {"name" : name.text, "price": price.text, "description": description.text, "link": link}
        writeToJSONFile('./','savedData', data)
        asyncio.run(main(item_id, name.text, price.text, description.text, link))
    print("__________%s____________"% i)


def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)


def removeAlert(typeby, tag, driver, message):
    try:
        try:
            if typeby == "class":
                button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, tag))
                )
            elif typeby == "id":
                button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.ID, tag))
                )
        except:
            print(f"NO {message} button popped out")
        else:
            button.click()
    except Exception as error: 
        print(f"ERROR: {error}")



profile_path = r'C:\Users\rroma\AppData\Local\Google\Chrome\User Data\Default'
profile_path_2 = r'C:\Users\rroma\AppData\Local\Google\Chrome\User Data\Profile 2'

options = uc.ChromeOptions() 
# options.add_argument('--headless') = False
# options.add_argument(f"user-data-dir={profile_path}") #optional if thare is chrome problems with default chrome
options.add_argument("--no-first-run")
options.add_argument("--no-default-browser-check")
options.add_argument("--disable-extensions")
options.add_argument("--disable-infobars")
options.add_argument("--disable-features=DefaultBrowserSettingEnabled")
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--search-engine-choice-country")
chrome_options = uc.ChromeOptions() 
# chrome_options.add_argument('--headless') = False
# chrome_options.add_argument(f"user-data-dir={profile_path_2}") #optional if thare is chrome problems with default chrome
chrome_options.add_argument("--no-first-run")
chrome_options.add_argument("--no-default-browser-check")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-features=DefaultBrowserSettingEnabled")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--search-engine-choice-country")

driver = uc.Chrome(options=options) 
driverForLinks = uc.Chrome(options=chrome_options) 

# buttonGoogle = findElement("css",  '[aria-label="Google"]', driver)
# buttonGoogle2 = findElement("css", '[aria-label="Google"]', driverForLinks)
# removeAlert("class", "disc-border", buttonGoogle, "google")
# removeAlert("class", "disc-border", buttonGoogle2, "google")
# child = WebDriverWait(driver, 5).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Google"]'))
# )
# print(child)

item_id = 0
i = 100 
cookies = True
cookiesForLinks = True
registration = False

linksChecked = []
data = {}

if os.path.exists('./savedData.json'):
    with open('./savedData.json', 'r') as file:
        data = json.load(file)
    for item in data:
        linksChecked.append(data[""+item+""]["link"])
        item_id = int(item) + 1

while i!=0:

    with driver:
        driver.get("https://www.facebook.com/marketplace/np/paris/home?maxPrice=0&radius=60&session_id=&exact=false")
    time.sleep(1)

    if cookies == True:
        removeAlert("class", "x9f619.x1n2onr6.x1ja2u2z.x78zum5.xdt5ytf.x193iq5w.xeuugli.x1iyjqo2.xs83m0k.x150jy0e.x1e558r4.xjkvuk6.x1iorvi4.xdl72j9", driver, "cookies")
        cookies = False
     
    if registration == False:
        removeAlert("class", "x92rtbv.x10l6tqk.x1tk7jg1.x1vjfegm", driver, "registration")
    
    removeAlert("class", "x92rtbv.x10l6tqk.x1tk7jg1.x1vjfegm", driver, "location")

    items_recheck = driver.find_elements(By.CSS_SELECTOR, ".x1i10hfl.xjbqb8w.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.x1heor9g.x1sur9pj.xkrqix3.x1lku1pv")
    items = []

    while items_recheck != items:
        items = items_recheck


        try:
            items = items_recheck
            counter = 0
            for item in items:
                try:
                    link = item.get_attribute("href")
                    if link not in linksChecked:
                        linksChecked.append(link)
                        item_scraping(item_id, item.get_attribute("href"), cookiesForLinks)
                        if cookiesForLinks == True:
                            cookiesForLinks = False
                except StaleElementReferenceException:
                    refreshed_items = driver.find_elements(By.CSS_SELECTOR, ".x1i10hfl.xjbqb8w.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.x1heor9g.x1sur9pj.xkrqix3.x1lku1pv")
                    refreshed_item = refreshed_items[counter]
                    link = refreshed_item.get_attribute("href")
                    if link not in linksChecked:
                        linksChecked.append(link)
                        item_scraping(item_id, item.get_attribute("href"), cookiesForLinks)
                        if cookiesForLinks == True:
                            cookiesForLinks = False
                counter += 1
                item_id = item_id+1
        except Exception as e:
            print(f"An error occurred: {str(e)}")
        
        for item in items:
            if item.get_attribute("href") not in linksChecked:
                linksChecked.append(item.get_attribute("href"))
                item_scraping(item_id, item.get_attribute("href"), cookiesForLinks)
                if cookiesForLinks == True:
                    cookiesForLinks = False
                item_id = item_id+1

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        items_recheck = driver.find_elements(By.CSS_SELECTOR, ".x1i10hfl.xjbqb8w.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.x1heor9g.x1sur9pj.xkrqix3.x1lku1pv")
        for item_new in items_recheck:
            print(item_new)
    i = i-1
    cookies = 0
    

# driver.quit()
# driverForLinks.quit()
