from selenium import webdriver # or any custom webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

def before_all(context):
    context.web = webdriver.Chrome(ChromeDriverManager().install())
    #context.web = webdriver.Firefox()

def after_step(context, step):
    print()

def after_all(context):
    context.web.close()