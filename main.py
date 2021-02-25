# import PIL
import pyautogui # clicks
# import keyboard # for testing
# import urllib3 # for proxy addresses
import os # paths
import random # for random interval entering
import re # regex
import logging # for logs
from selenium import webdriver # web driver for work in browser
# import chromedriver_binary
# from selenium.common import exceptions as ex
from time import sleep # delay

logging.basicConfig(level = logging.DEBUG,
					format = '%(asctime)s : %(levelname)s : %(message)s',
					filename = r'logs.log',
					filemode = 'w')

expansions = ['jpeg', 'jpg', 'png'] # expansions for pictures

# login = None # begin login
# password = None # begin password
# driver = None
# elem = None
# mode = None

def captcha_authorization(driver):
	""" Complete captcha_authorization
	:param driver: web driver
	:return: click on button
	"""
	cpt = re.compile('cpt\w')
	char = re.compile('\d')
	name = re.compile('\w{}10\.\D{3}')
	while True:
		try:
			assert driver.find_element_by_css_selector('div.rc-anchor-content')
			# pic = driver.find_element_by_css_selector('div.rc-anchor-content')
			logging.info('Found element "div.rc-anchor-content"')
			break
		except AssertionError:
			try:
				assert driver.find_elements_by_partial_link_text('https://visit-box.net/images/{}/{}/{}'.format(cpt, char, name))
				# pic = driver.find_elements_by_partial_link_text('https://visit-box.net/images/{}/{}/{}'.format(cpt, char, name))
				logging.info('Found element with partial link text')
				break
			except AssertionError:
				continue
	# solution = server(pic)  # Передача на FTP сервер
	sol = False
	return sol

def authorization(driver, l, p):
	""" Authorization on our site
	:param driver: web driver
	:param l: user login
	:param p: user password
	:return: status code
	"""
	logging.info('Definition "authorization"')
	if 'VisitBox - биржа визитов №1' in driver.title:
		while True:
			try:
				assert driver.find_element_by_class_name('btn upper orange')
				logging.info('Found element "btn upper orange"')
				element = driver.find_element_by_class_name('btn upper orange')
				s = element.size()
				x = random.randint(-s['height'], s['height'])
				y = random.randint(-s['width'], s['width'])
				webdriver.ActionChains(driver).move_to_element_with_offset(element, x, y).click().perform()
				logging.info('Click on this element. Mouse position: {}'.format(pyautogui.position()))
				break
			except AssertionError:
				sleep(5)
	element = driver.find_element_by_name('login')
	s = element.size()
	x = random.randint(-s['height'], s['height'])
	y = random.randint(-s['width'], s['width'])
	webdriver.ActionChains(driver).move_to_element_with_offset(element, x, y).click().perform()
	interval = random.randint(1, 10) / 10
	pyautogui.typewrite(l, interval)
	logging.debug('Login enter in form')
	element = driver.find_element_by_name('password')
	s = element.size()
	x = random.randint(-s['height'], s['height'])
	y = random.randint(-s['width'], s['width'])
	driver.ActionChains(driver).move_to_element_with_offset(element, x, y).click().perform()
	interval = random.randint(1, 10) / 10
	pyautogui.typewrite(p, interval)
	logging.debug('Password enter in form')
	del interval
	sol = captcha_authorization(driver)
	while True:
		try:
			assert driver.find_element_by_name('scpt_code')
			# elem = driver.find_element_by_name('scpt_code')
			break
		except AssertionError:
			sleep(5)
			continue
	pyautogui.typewrite(sol)
	del sol
	element = driver.find_element_by_class_name('btn upper lilac')
	s = element.size()
	x = random.randint(-s['height'], s['height'])
	y = random.randint(-s['width'], s['width'])
	webdriver.ActionChains(driver).move_to_element_with_offset(element, x, y).click().perform()
	print('Authorization success')
	urls_click(driver)

def solutions(driver):
	"""
	:param driver: web driver
	:return: solution of captcha
	"""
	# noinspection PyGlobalUndefined
	logging.debug('Definition "solution"')
	k = 0
	while k <= 3:
		logging.info('Pictures Captcha on start page was found')
		while True:
			try:
				assert driver.find_element_by_css_selector('div.rc-anchor-content')
				# pic = driver.find_element_by_class_name('div.rc-anchor-content')
				logging.info('Google Captcha on start page was found')
				break
			except AssertionError:
				continue
		solution = False # _-_-_-_-_-_-_-_-_-_-_ ПЕРЕДАТЬ В ОБРАБОТЧИК (pic)

		return solution
	k = 0
	while k <= 3:
		try:
			assert driver.find_elements_by_css_selector('div.cpt-image-item')
			# elem = driver.find_elements_by_css_selector('div.cpt-image-item')
			logging.debug('Pictures')
			break
		except AssertionError:
			try:
				assert driver.find_element_by_css_selector('div.rc-inline-block')
				# elem = driver.find_element_by_css_selector('div.rc-inline-block')
				logging.info('Google Captcha')
				break
			except AssertionError:
				k += 1
				sleep(3)
		solution = True # _-_-_-_-_-_-_-_-_-_-_ ПЕРЕДАТЬ В ОБРАБОТЧИК (pic)

		return solution

def captcha(driver):
	""" Complete captcha
	:param driver: web driver
	:return: click on button
	"""
	logging.debug('Definition "captcha"')
	# noinspection PyGlobalUndefined
	pyautogui.press('ctrl + w')
	# pyautogui.click(solutions(elem))
	p = solutions(driver)
	if p is True:
		logging.debug('Returned True')
	else:
		logging.debug('Returned False')

def urls_click(driver):
	""" Start process click of URLs
	:param driver: web driver
	:return: None
	"""
	logging.debug('Definition "urls_click"')
	sleep(1)
	if 'Панель управления - VisitBox' in driver.title:
		while True:
			try:
				assert driver.find_element_by_link_text('Просмотр сайтов')
				logging.info('Found element "Просмотр сайтов"')
				element = driver.find_element_by_link_text('Просмотр сайтов')
				s = element.size()
				x = random.randint(-s['height'], s['height'])
				y = random.randint(-s['width'], s['width'])
				driver.ActionChains(driver).move_to_element_with_offset(element, x, y).click().perform()
				logging.info('Click on this element. Mouse position: {}'.format(pyautogui.position()))
				break
			except AssertionError:
				sleep(5)
		
	while True:
		try:
			assert 'Заработок VS - VisitBox' in driver.title
			assert driver.find_elements_by_css_selector('div.title')
			links = driver.find_elements_by_css_selector('div.title')
			logging.info('Links was found')
			for link in links:
				driver.ActionChains(driver).move_to_element(link).click().perform()
				logging.info('Click on link {}. Mouse position: {}'.format(link, pyautogui.position()))
				captcha(driver)
				pyautogui.hotkey('ctrl + W')
				sleep(10)
			break
		except AssertionError:
			continue
	pyautogui.hotkey('f5')

def main():
	"""
	:return: None
	"""
	global regex
	logging.info('Definition "main"')
	# global login, password
	regex = re.compile('\w{14}\-')
	logging.debug('Regex is enable')
	width, height = pyautogui.size()
	logging.info('Width: {}, Height: {}'.format(width, height))
	# keyboard.wait('ctrl+1')
	try:
		with open('cookies.txt', 'r') as f:
			cookie = f.read()
	except FileNotFoundError:
		cookie = ''
	path = os.path.join(os.getcwd(), 'Web Drivers', 'chromedriver.exe')
	chromeoptions = webdriver.ChromeOptions()
	logging.debug('chromeoptions is enable')
	chromeoptions.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
	# chromeoptions.add_argument("--no-sandbox")
	# chromeoptions.add_argument("--disable-setuid-sandbox")
	chromeoptions.add_argument("--remote-debugging-port=9222")  # don't remote
	chromeoptions.add_argument("--disable-dev-shm-using")
	chromeoptions.add_argument("--disable-extensions")
	chromeoptions.add_argument("--disable-gpu")
	chromeoptions.add_argument("start-maximized")
	chromeoptions.add_argument("disable-infobars")
	# chromeoptions.add_argument("--headless")
	# chromeoptions.add_argument('--disable-blink-features')
	logging.debug('Options was appended')
	# logging.debug('BinaryLocation={}'.format(chromeoptions.BinaryLocation))
	# try:
	if cookie != '':
		driver = webdriver.Chrome(executable_path=path, options = chromeoptions).add_cookie(cookie)
		driver.get('https://visit-box.net/visits/')
		urls_click(driver)
	else:
		driver = webdriver.Chrome(executable_path=path, options = chromeoptions)
		cookie = driver.get_cookies()
		with open('cookies.txt', 'w') as f:
			f.write(cookie)
		driver.get('https://visit-box.net/login/')  # .open_new_tab()
		logging.debug('Login page was got')
		while True:
			if os.path.exists('login_password.txt'):
				logging.info('File was found')
				with open('login_password.txt', 'r') as f:
					content = f.read()
				content = content.split('\n')
				login = content[0].strip()
				login = login.strip('\n')
				password = content[1].strip()
				password = password.strip('\n')
				# noinspection PyTypeChecker
				authorization(driver, login, password)
				break
			else:
				logging.info('File not found')
				continue
	logging.debug('Not errors in start browser')
	# except ex.WebDriverException as e:
	# 	print('See logs')
	# 	logging.warning('Crash browser: {}'.format(e))
	# 	sleep(5)


if __name__ == '__main__':
	main()
