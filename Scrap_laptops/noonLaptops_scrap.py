import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Set up the WebDriver using WebDriver Manager
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu') 
driver = webdriver.Chrome(service=service, options=options)

laptops_title=[]
laptops_price=[]

for i in range(1,17):
    pages=f'https://www.noon.com/saudi-en/electronics-and-mobiles/computers-and-accessories/laptops/?limit=50&page={i}&sort%5Bby%5D=popularity&sort%5Bdir%5D=desc'
    driver.get(pages)

    time.sleep(5)

    for _ in range(10):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    driver_content=driver.page_source
    soup=BeautifulSoup(driver.page_source,'html.parser')

  

    laptops_titles = soup.find_all('div', {'data-qa': 'product-name'})
    laptops_prices=soup.find_all('div',{'class':'sc-8df39a2e-1 hCDaLm'})
   
    print(f'laptop title len:{len(laptops_titles)}')
    print(f'laptop prices len:{len(laptops_prices)}')

    for laptop in laptops_titles:
        title = laptop.get('title')
        if title:
            #title=title_tag.text.strip()
            laptops_title.append(title)
            print(f"Title found: {title}")

    for laptop in laptops_prices:        
        price_tag=laptop.find('strong')
        if price_tag:
           price = price_tag.text.strip()
           laptops_price.append(price) 
           print(f"Price found: {price}")   
driver.quit()            

#create csv file 
data={
    'Laptop_name':laptops_title,
    'price':laptops_price
}

for title,price in zip(laptops_title,laptops_price):
    print(f'title:{title},Price :{price}')  

df=pd.DataFrame(data=data)
df.to_csv('Laptops.csv',index=False)
     

