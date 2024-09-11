import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Send a request to the e-commerce website (replace URL with the actual one you want to scrape)
url = "https://example.com/products"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}
response = requests.get(url, headers=headers)

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Step 3: Extract product information (names, prices, ratings) 
# Adapt the selectors based on the website’s structure
products = []
for product in soup.find_all('div', class_='product-item'):
    name = product.find('h2', class_='product-title').text.strip()  # Extract product name
    price = product.find('span', class_='price').text.strip()  # Extract product price
    rating = product.find('span', class_='rating').text.strip()  # Extract product rating

    products.append({
        'Name': name,
        'Price': price,
        'Rating': rating
    })

# Step 4: Save the extracted data to a CSV file using pandas
df = pd.DataFrame(products)
df.to_csv('products.csv', index=False)

print("Scraping completed! Data saved to products.csv.")
