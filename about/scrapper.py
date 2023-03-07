import urllib.request
import urllib.request
import instaloader
from .models import InstagramPost
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager


def web_scraping():

    driver = webdriver.Chrome(ChromeDriverManager().install())
    INSTA_USER_NAME = "temur_11932"
    INSTA_PASSWORD = "q2%m-Y7j!MVWyXm"
    driver.get('https://www.instagram.com/accounts/login/')
    time.sleep(5)
    enter_username = driver.find_element(By.NAME, 'username')
    enter_password = driver.find_element(By.NAME, 'password')

    enter_username.send_keys(INSTA_USER_NAME)
    enter_password.send_keys(INSTA_PASSWORD)
    login_btn = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div')
    login_btn.click()
    time.sleep(5)
    driver.get("https://www.instagram.com/wayu.uz/")
    time.sleep(5)
    n_scrolls = 1
    for _ in range(n_scrolls):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
    anchors = driver.find_elements(By.TAG_NAME, 'a')
    anchors = [a.get_attribute('href') for a in anchors]
    parent_dir = r"C:\Users\User\Desktop\uic_internship\wayu_uz\images\instagram_images"

    for i, a in enumerate(anchors):
        if str(a).startswith("https://www.instagram.com/p/"):
            L = instaloader.Instaloader()
            post = instaloader.Post.from_shortcode(L.context, a.split("/")[-2])
            if not post.is_video:
                img = urllib.request.urlretrieve(str(post.url), f"{parent_dir}\{i}.jpg")
                obj = InstagramPost.objects.create(image_url=a, post_image=img)
                obj.save()
    driver.quit()
