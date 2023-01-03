def get_func_name(func, *args):
    modified_function_name = func.__name__.title().replace('_', ' ')
    print(modified_function_name, end=" ")
    print(*args)


def open_browser(browser_name):
    get_func_name(open_browser, browser_name)

def go_to_companyname_homepage(page_url):
    get_func_name(go_to_companyname_homepage, page_url)

def find_registration_button_on_login_page(page_url, button_text):
    get_func_name(find_registration_button_on_login_page, page_url, button_text)

open_browser("Chrome")
go_to_companyname_homepage("https://qa.guru")
find_registration_button_on_login_page("https://qa.guru/", "authorization")