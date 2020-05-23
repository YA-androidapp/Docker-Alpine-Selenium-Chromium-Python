#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2020 YA-androidapp(https://github.com/YA-androidapp) All rights reserved.

# $ cd ＜Dockerfileがあるディレクトリ＞
# $ docker-compose up -d
# $ docker container exec -it selenium python get_source.py


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


o = Options()
o.binary_location = '/usr/bin/chromium-browser'
o.add_argument('--headless')
o.add_argument('--disable-gpu')
o.add_argument('--no-sandbox')
o.add_argument('--window-size=1200x600')


s = Service(executable_path='/usr/lib/chromium/chromedriver')
s.start()
d = webdriver.Remote(
    s.service_url,
    desired_capabilities=o.to_capabilities()
)


d.get('https://www.google.com')
print(d.title)
print(d.page_source)

print(dir(d))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_file_detector', '_is_remote', '_mobile', '_switch_to', '_unwrap_value', '_web_element_cls', '_wrap_value', 'add_cookie', 'application_cache', 'back', 'capabilities', 'close', 'command_executor', 'create_web_element', 'current_url', 'current_window_handle', 'delete_all_cookies', 'delete_cookie', 'desired_capabilities', 'error_handler', 'execute', 'execute_async_script', 'execute_script', 'file_detector', 'file_detector_context', 'find_element', 'find_element_by_class_name', 'find_element_by_css_selector', 'find_element_by_id', 'find_element_by_link_text', 'find_element_by_name', 'find_element_by_partial_link_text', 'find_element_by_tag_name', 'find_element_by_xpath', 'find_elements', 'find_elements_by_class_name', 'find_elements_by_css_selector', 'find_elements_by_id', 'find_elements_by_link_text', 'find_elements_by_name', 'find_elements_by_partial_link_text', 'find_elements_by_tag_name', 'find_elements_by_xpath', 'forward', 'fullscreen_window', 'get', 'get_cookie', 'get_cookies', 'get_log', 'get_screenshot_as_base64', 'get_screenshot_as_file', 'get_screenshot_as_png', 'get_window_position', 'get_window_rect', 'get_window_size', 'implicitly_wait', 'log_types', 'maximize_window', 'minimize_window', 'mobile', 'name', 'orientation', 'page_source', 'quit', 'refresh', 'save_screenshot', 'session_id', 'set_page_load_timeout', 'set_script_timeout', 'set_window_position', 'set_window_rect', 'set_window_size', 'start_client', 'start_session', 'stop_client', 'switch_to', 'switch_to_active_element', 'switch_to_alert', 'switch_to_default_content', 'switch_to_frame', 'switch_to_window', 'title', 'w3c', 'window_handles']

d.quit()
