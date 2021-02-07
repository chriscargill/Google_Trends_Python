import pyautogui as auto
import random
import time

google_urls = []
typing_speed = 0.01

seconds_wait_for_website = 3
seconds_normal_wait = 1
seconds_open_program = 2

download_button_x = 1420
download_button_y = 470

browser_close_x = 1905
browser_close_y = 42
move_mouse_speed = 1

terminal_close_x = 1302
terminal_close_y = 390

downloads_folder = "~/Downloads/multiTimeline.csv"
file_folder = "/home/username/GoogleTrends/data/"

def getRandomInterval():
    """ Get a random decimal number from 0 to 1 """
    return round((random.randrange(0,100) * .01),2)

def grabData(google_url):
    """ Grab the data from Google Trends and save it as a CSV """
    # open terminal
    time.sleep(seconds_normal_wait)
    auto.hotkey('ctrl', 'alt', 't')
    time.sleep(seconds_open_program)
    # open firefox
    auto.typewrite("firefox", interval=typing_speed)
    auto.hotkey("enter")
    time.sleep(seconds_wait_for_website)
    # go to google trends website
    auto.typewrite(google_url, interval=typing_speed)
    auto.hotkey("enter")
    time.sleep(seconds_wait_for_website)
    auto.moveTo(download_button_x,download_button_y,move_mouse_speed)
    random_interval = getRandomInterval()
    auto.leftClick(interval=random_interval)
    time.sleep(seconds_wait_for_website)
    # Download the data
    auto.hotkey('alt','s')
    time.sleep(seconds_normal_wait)
    auto.hotkey('enter')
    time.sleep(seconds_normal_wait)
    # close firefox
    auto.moveTo(browser_close_x,browser_close_y,move_mouse_speed)
    auto.leftClick()
    # open terminal
    auto.hotkey('ctrl', 'alt', 't')
    time.sleep(seconds_open_program)
    #move csv file from downloads folder
    data_date = time.time()
    auto.typewrite(f"mv {downloads_folder} {file_folder}data_{data_date}", interval=typing_speed)
    auto.hotkey('enter')
    time.sleep(seconds_normal_wait)
    # exit terminal
    auto.hotkey('shift', 'ctrl', 'q')
    # exit firefox terminal
    time.sleep(seconds_normal_wait)
    auto.moveTo(terminal_close_x,terminal_close_y)
    random_interval = getRandomInterval()
    auto.leftClick(interval=random_interval)

def userKeyWords():
    """ Store all of the keywords you want to search for"""
    store_keywords = {}
    keywords = {"1":["data", "engineer","software", "developer"]}
    for i, keyword in keywords.items():
        try temp = store_keywords[i]:
            goahead = false
        except:
            goahead = true
        if goahead:
            if " " in keyword:
                keyword = keyword.replace(" ", "%20")
            store_keywords[i].append(keyword)
    all_keywords = ",".join(store_keywords[i])
    return all_keywords

def createURLS(all_keywords):
    """ Go through the last 10 years, month by month and store the associated data as a list of URLs """
    years = 10
    months = 12
    times = years * months
    start_year = "2011"
    start_month = "01"
    start_day = "01"
    end_year = start_year
    end_month = "0" + str(int(start_month) + 1)
    end_day = start_day
    for each_month in range(0,times):
        google_urls.append(f"https://trends.google.com/trends/explore?date={start_year}-{start_month}-{start_day}%20{end_year}-{end_month}-{end_day}&geo=US&q={all_keywords}")
        
        # Start month is set to the end_month
        start_month = "0" + str(int(end_month))

        # Trim leading 0 in double digit numbers greater than 9
        if int(start_month) > 9:
            start_month = start_month[1:]

        if int(start_month) > 12:
            print("THIS SHOULD NEVER HAPPEN!")
        # If the new start month is december, the new end month should be january
        elif int(start_month) == 12:
            end_month = "01"
            end_year = str(int(end_year) + 1)
        elif int(start_month) == 1:
            end_month = "0" + str(int(start_month) + 1)
            start_year = str(int(start_year) + 1)
        else:
            end_month = "0" + str(int(start_month) + 1)

        # Trim leading 0 in double digit numbers greater than 9
        if int(end_month) > 9:
            end_month = end_month[1:]

def main():
    all_keywords = userKeyWords()
    createURLS(all_keywords)
    for google_url in google_urls:
        grabData(google_url)
        print(f"Grabbed data from {google_url}")
    
main()
