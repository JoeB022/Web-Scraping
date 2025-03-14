## E-commerce Web Scraper
This is a Python program that extracts product information (name, price, and rating) from an e-commerce website (e.g., Amazon) and stores the data in a structured CSV file. The program uses the requests and BeautifulSoup libraries for web scraping and the csv module for saving the data.

## Features
Web Scraping: Extracts product information (name, price, and rating) from an e-commerce website.

CSV Export: Saves the extracted data to a CSV file for easy analysis.

Customizable: Can be adapted to scrape different e-commerce websites or search queries.

## How to Use
# Clone the Repository (if applicable):

git clone https://github.com/JoeB022/Web-Scraping.git
cd Web-Scraping

# Install Dependencies:
Ensure you have Python installed on your system. Then, install the required libraries using the following command:

pip install requests beautifulsoup4

# Run the Program:
Run the program using the following command:

python3 scraper.py

# View the Output:

The program will scrape the website and save the extracted data to a CSV file (products.csv).

Open the CSV file to view the product information.

## Example Output (CSV File)
Product Name,Price,Rating
"ASUS VivoBook 15 Laptop",799,4.5
"HP Pavilion 15 Laptop",899,4.3
"Dell Inspiron 15 3000 Laptop",699,4.2
...

## Customization
Change the URL: Update the URL variable in the program to target a different e-commerce website or search query.

Add More Fields: Modify the extract_product_info function to extract additional product details (e.g., reviews, availability).

## Requirements
Python 3.x

Libraries: requests, beautifulsoup4

## Notes
Respect Website Policies: Always check the website's robots.txt file and terms of service before scraping.

Dynamic Content: Some websites use JavaScript to load content dynamically. In such cases, consider using a tool like Selenium.

Error Handling: Add error handling for network issues or changes in the website's HTML structure.

## License
This project is open-source and available under the MIT License.

Contributing
Contributions are welcome! If you find any issues or want to improve the program, feel free to open an issue or submit a pull request.

## Author
Joe Brian

https://github.com/JoeB022

joebrian.dev@gmail.com
