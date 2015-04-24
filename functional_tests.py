from selenium import webdriver

# browser = webdriver.Chrome(executable_path="C:/ChromeDriver/chromedriver.exe")
browser = webdriver.Firefox()
browser.get("http://localhost:8000")

assert "Django" in browser.title
