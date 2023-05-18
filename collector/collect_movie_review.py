import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

######################################
# 1.Install ChrmeDriver for selenium #
######################################
# Selenium -> 개인 웹 브라우저 사용!(우리는 웹 브라우저 중 Chrom 사용)
driver = webdriver.Chrome()

########################
# 2. Open ChromeDriver #
########################
# selenium -> webdriver(chrome)
# 1.최신 버전 사용해서 code로 다운로드(최신버전)
# 2.chrome driver 다운로드 후 주입(구버전)
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


movie_id = 160244
url = f"https://movie.daum.net/moviedb/grade?movieId={movie_id}"
