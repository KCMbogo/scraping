from playwright.sync_api import sync_playwright
import json

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0.4472.124",
        viewport={"width": 1920, "height": 1080}
    )

    page = context.new_page()

    page.goto("https://www.aliexpress.com/p/calp-plus/index.html?spm=a2g0o.home.allcategoriespc.1.650c76dbvNtRcu&categoryTab=phones_%2526_telecommunications")

    page.wait_for_timeout(3000)

    for _ in range(0):
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")  
        page.wait_for_timeout(3000)

    products = page.query_selector_all("._2FypS")
    scraped_products = []

    for i, product in enumerate(products):
        link_element = product.query_selector('a._3mPKP')
        image_element = product.query_selector('img._2EGeS.product-img')
        title_element = product.query_selector('h3.yB6en')
        price_element = product.query_selector('._3Mpbo')
        rating_element = product.query_selector('._2L2Tc')
        sold_element = product.query_selector('span.DUuR2')
        hint_element = product.query_selector('div.nuPN3 div.FNjFR span._3dc7w')

        link = f"https:{link_element.get_attribute('href')}" if link_element else "N/A"
        image = f"https:{image_element.get_attribute('src')}" if image_element else "N/A"
        title = title_element.inner_text() if title_element else "N/A"
        price = price_element.inner_text() if price_element else "N/A"
        rating = rating_element.inner_text() if rating_element else "N/A"    
        sold = sold_element.inner_text() if sold_element else "N/A"
        hint = hint_element.inner_text() if hint_element else "N/A"

        scraped_products.append({
            "link": link,
            "image": image,
            "title": title,
            "price": price,
            "rating": rating,
            "sold": sold,
            "hint": hint
        })

        # print(f"Product No: {i+1} of {len(products)}\nSite link: {link}\nImage: {image}\nTitle: {title}\nPrice: {price}\nRating: {rating}\nSold: {sold}\nHint: {hint}\n")      

    with open("scraped_products.json", "w", encoding="utf-8") as f:
       json.dump(scraped_products, f, ensure_ascii=False, indent=4)

    print("DONE...!")
    browser.close()