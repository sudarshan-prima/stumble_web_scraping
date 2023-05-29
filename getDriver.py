from seleniumwire import webdriver

def get_driver():
    co = webdriver.ChromeOptions()
    datapath = r"C:\Users\Sudarshan\Desktop\ext"
    co.headless = False
    co.add_argument("log-level=3")
    co.add_argument("--user-data-dir=%s" % datapath)
    co.debugger_address = 'localhost:9222'
    driver = webdriver.Chrome(executable_path='C:/Users/Sudarshan/Downloads/chromedriver_win32/chromedriver.exe',
                              chrome_options=co)
    return driver
