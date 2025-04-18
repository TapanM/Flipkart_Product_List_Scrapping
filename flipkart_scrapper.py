from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Generating URL
def generate_url(search_term):
    base_template = "https://www.flipkart.com/search?q={}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
    return base_template.format(search_term)

# Creating Chrome Driver
def create_driver()-> webdriver.Chrome:
    options = Options()
    options.add_argument("--headless") #No GUI, run on background
    driver = webdriver.Chrome(options=options)
    return driver

# # Generate File Name
# def generate_filename(search_item):
#     filename = '_'.join(search_item.split(' '))
#     return filename +'.csv'

# Collecting Product List from current page
def collect_products_list(driver):
    products = driver.find_elements(By.CLASS_NAME, "tUxRFH")
    return products

# Collect info from Specific Products
def extract_product_data(product):
    title = product.find_element(By.CLASS_NAME, "KzDlHZ").text
        
    # EXTRACTING PRICE
    price = product.find_element(By.XPATH, ".//div[@class='Nx9bqj _4b5DiR']").text
        
    # EXTRACTING REVIEW
    try:
        review = product.find_element(By.CLASS_NAME, "XQDdHH").text
    except:
        review="NULL"
        
    # EXTRACTING LINK
    link = product.find_element(By.CLASS_NAME, "CGtC98").get_attribute('href')

    return title, price, review, link

# # Import data into CSV
# def save_data_to_csv(record, filename, new_file=False):
#     header = ['Title', 'Price', 'Review', 'Link']
#     if new_file:
#         with open(filename, 'w', newline='', encoding='utf-8') as f:
#             writer = csv.writer(f)
#             writer.writerow(header)
#     else:
#         with open(filename, 'a+', newline='', encoding='utf-8') as f:
#             writer = csv.writer(f)
#             writer.writerow(record)

def run(search_item):
    products_data = []
    driver = create_driver()
    for page in range(1,2):
        url = generate_url(search_item)
        driver.get(url)

        # Extract the products info
        products = collect_products_list(driver)
        for product in products:
            record = extract_product_data(product)
            products_data.append({
                'title' : record[0],
                'price' : record[1],
                'review' : record[2],
                'link' : record[3]
            })
    driver.quit()
    return products_data