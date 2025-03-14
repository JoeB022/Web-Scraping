import requests
from bs4 import BeautifulSoup
import csv

# Define the URL of the e-commerce website (e.g., Amazon search results for "laptops")
URL = "https://www.amazon.com/s?k=laptops"

# Headers to mimic a real browser request
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

def extract_product_info(product):
    """Extract product name, price, and rating from a product block."""
    name = product.find("span", class_="a-text-normal")
    price = product.find("span", class_="a-price-whole")
    rating = product.find("span", class_="a-icon-alt")

    # Clean and format the data
    name = name.text.strip() if name else "N/A"
    price = price.text.strip() if price else "N/A"
    rating = rating.text.strip().split()[0] if rating else "N/A"

    return name, price, rating

def scrape_website(url):
    """Scrape the website and extract product information."""
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")

    products = soup.find_all("div", {"data-component-type": "s-search-result"})
    product_data = []

    for product in products:
        name, price, rating = extract_product_info(product)
        product_data.append([name, price, rating])

    return product_data

def save_to_csv(data, filename="products.csv"):
    """Save the extracted data to a CSV file."""
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Product Name", "Price", "Rating"])
        writer.writerows(data)

def main():
    """Main function to run the web scraper."""
    print("Scraping product information...")
    product_data = scrape_website(URL)

    if product_data:
        save_to_csv(product_data)
        print(f"Data saved to 'products.csv'")
    else:
        print("No products found.")

if __name__ == "__main__":
    main()