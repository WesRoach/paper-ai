import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(
    executable_path='/Users/admin/Projects/repos/paper-io/chromedriver')
url = "http://paper-io.com/"
browser.get(url)

# first login - set username
name = 'Anna'
input_name_text = browser.find_element_by_id("paperio_p1")
input_name_text.send_keys(name)

# first play - click play
input_name_button = browser.find_element_by_css_selector("div.button.play")
input_name_button.click()

# If died - hit play button
play_again_button = browser.find_element_by_css_selector(
    "#game_over > div.button.play")
play_again_button.click()

# If Ad - click Skip
skip_add_button = browser.find_element_by_css_selector(
    '#body > div.videoAdUiSkipButtonExperimentalText'
    '.videoAdUiFixedPaddingSkipButtonText'
)
skip_add_button.click()

browser.close()



i = 0
while i < 100:
    ActionChains(browser).send_keys(Keys.ARROW_LEFT).perform()
    time.sleep(.5)
    print("Turned Left - Sleeping")

    ActionChains(browser).send_keys(Keys.ARROW_DOWN).perform()
    time.sleep(.5)
    print("Turned Down - Sleeping")

    ActionChains(browser).send_keys(Keys.ARROW_RIGHT).perform()
    time.sleep(.5)
    print("Turned Right - Sleeping")

    ActionChains(browser).send_keys(Keys.ARROW_UP).perform()
    time.sleep(.5)
    print("Turned Up - Sleeping")
    i += 4
print("exited loop")

in_value = input()
print(in_value)

the_game = browser.find_element_by_id("the_game")
the_game.send_keys("w")
the_game.send_keys("a")
the_game.send_keys("s")
the_game.send_keys("d")

screen = curses.initscr()