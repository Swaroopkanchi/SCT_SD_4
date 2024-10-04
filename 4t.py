import requests
from bs4 import BeautifulSoup
import csv

def extract_product_info(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    products = []
    for product in soup.find_all('div', class_='product-item'):
        name = product.find('h2', class_='product-title').text.strip()
        price = product.find('span', class_='price').text.strip()
        rating = product.find('span', class_='rating').text.strip() if product.find('span', class_='rating') else 'No rating'
        products.append([name, price, rating])

    return products

def save_to_csv(products, filename='products.csv'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Price', 'Rating'])
        writer.writerows(products)