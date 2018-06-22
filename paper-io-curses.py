import curses

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(
    executable_path='/Users/admin/Projects/repos/paper-io/chromedriver')
url = "http://paper-io.com/"
browser.get(url)

name = 'r4gz'
input_name_text = browser.find_element_by_id("paperio_p1")
input_name_text.send_keys(name)

input_name_button = browser.find_element_by_css_selector("div.button.play")
input_name_button.click()

actions = ActionChains(browser)

screen = curses.initscr()

curses.noecho()
curses.cbreak()
screen.keypad(True)

try:
    while True:
        char = screen.getch()
        if char == ord('q'):
            break
        elif char == curses.KEY_RIGHT:
            # actions.send_keys(Keys.ARROW_RIGHT)
            # actions.perform()
            ActionChains(browser).send_keys(Keys.ARROW_RIGHT).perform()
        elif char == curses.KEY_LEFT:
            # actions.send_keys(Keys.ARROW_LEFT)
            # actions.perform()
            ActionChains(browser).send_keys(Keys.ARROW_LEFT).perform()
        elif char == curses.KEY_UP:
            # actions.send_keys(Keys.ARROW_UP)
            # actions.perform()
            ActionChains(browser).send_keys(Keys.ARROW_UP).perform()
        elif char == curses.KEY_DOWN:
            # actions.send_keys(Keys.ARROW_DOWN)
            # actions.perform()
            ActionChains(browser).send_keys(Keys.ARROW_DOWN).perform()

finally:
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
