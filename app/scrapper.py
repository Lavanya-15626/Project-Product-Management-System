import requests
from bs4 import BeautifulSoup

# Flask API URL
BASE_URL = "http://127.0.0.1:5000/products"

# Using a simpler static test page (phones)
SCRAPE_URL = "https://webscraper.io/test-sites/e-commerce/static/phones"

def scrape_products():
    print("🔍 Scraping data from:", SCRAPE_URL)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(SCRAPE_URL, headers=headers)
    if response.status_code != 200:
        print("❌ Failed to fetch webpage.")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    items = soup.find_all("div", class_="thumbnail")
    scraped_products = []

    for item in items:
        title_tag = item.find("a", class_="title")
        price_tag = item.find("h4", class_="pull-right price")
        desc_tag = item.find("p", class_="description")

        if not title_tag or not price_tag:
            continue

        title = title_tag.text.strip()
        price = float(price_tag.text.strip().replace("$", ""))
        desc = desc_tag.text.strip() if desc_tag else "No description"

        product = {
            "name": title,
            "description": desc,
            "price": price,
            "quantity": 10
        }
        scraped_products.append(product)

    print(f"✅ Found {len(scraped_products)} products.")
    return scraped_products

def send_to_api(products):
    print(f"📦 Sending {len(products)} products to backend...")
    for p in products:
        res = requests.post(BASE_URL, json=p)
        if res.status_code == 201:
            print(f"✅ Added: {p['name']}")
        else:
            print(f"⚠️ Failed to add {p['name']} — {res.text}")

def main():
    products = scrape_products()
    if products:
        send_to_api(products)
        print("\n🎉 All products scraped and added successfully!")
    else:
        print("❌ No products found to add.")

if __name__ == "__main__":
    main()
