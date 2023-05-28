from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

URL = "https://www.speedtest.net/"

service = Service(r"C:\\Users\\janns\\PycharmProjects\\chromedriver.exe")
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

driver.get(URL)

total_test = 0
test_count = 5

download = []
upload = []


def average(to_ave):
    return sum(to_ave) / len(to_ave)


for n in range(test_count):
    total_test += 1
    driver.find_element(By.CLASS_NAME, "start-text").click()
    sleep(45)

    download_speed = driver.find_element(By.CLASS_NAME, "download-speed").text
    upload_speed = driver.find_element(By.CLASS_NAME, "upload-speed").text
    download.append(float(download_speed))
    upload.append(float(upload_speed))

    with open("Internet speed result.txt", "a") as file:
        file.write(f"Test {total_test}\n")
        file.write(f"Download Speed: {download_speed}\n")
        file.write(f"Upload Speed: {upload_speed}\n")
        file.write("\n----------------------------------------------------------------------------\n")

    sleep(5)

with open("Internet speed result.txt", "r+") as f:
    lines = f.readlines()
    lines.insert(0, "TEST RESULT\n")
    lines.insert(1, f"Total Test: {total_test}\n")
    lines.insert(2, f"Average Download Speed: {average(download)}\n")
    lines.insert(3, f"Average Upload Speed: {average(upload)}\n")
    lines.insert(4, "----------------------------------------------------------------------------")
    lines.insert(5, "\n----------------------------------------------------------------------------\n")
    f.seek(0)
    f.writelines(lines)

print("Test Complete")

driver.quit()
