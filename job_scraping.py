import os, json
from playwright.sync_api import sync_playwright

user_data_dir = os.path.expanduser("~/.playwright_profile/chrome")

with sync_playwright() as p:
    browser = p.chromium.launch_persistent_context(user_data_dir=user_data_dir, headless=True, viewport={"width": 1920, "height": 1080})
    page = browser.new_page()
    page.goto(
        "https://www.linkedin.com/jobs",
        wait_until="domcontentloaded"
    )
    page.wait_for_timeout(2000)

    search_prompt = input("Enter Title, Skill or Company:\t")
    location_prompt = input("Enter the area to search:\t")
    page.wait_for_timeout(1000)

    search_input = page.locator("input[aria-label='Search by title, skill, or company']:not([disabled])")
    search_input.wait_for(state="visible")
    search_input.fill(search_prompt)
    search_input.press("Enter")
    page.wait_for_timeout(1000)

    location_input = page.locator("input[aria-label='City, state, or zip code']:not([disabled])")
    location_input.wait_for(state="visible")
    location_input.fill(location_prompt)
    location_input.press("Enter")

    page.wait_for_selector("ul.EyBJWAsJeZqdckibssVhhKWmJliNWZofyFG li[data-occludable-job-id]")
    job_list_selector = "ul.EyBJWAsJeZqdckibssVhhKWmJliNWZofyFG"

    previous_count = 0
    scroll_attempts = 0
    max_attempts = 10

    while scroll_attempts < max_attempts:
        page.evaluate(f''' document.querySelector("{job_list_selector}").scrollBy(0, 1000) ''')
        page.wait_for_timeout(1500)
        current_count = page.locator(f"{job_list_selector} li[data-occludable-job-id]").count()
        print(f"Attempt {scroll_attempts+1}: Found {current_count} jobs")

        if current_count == previous_count:
            break  
        previous_count = current_count
        scroll_attempts += 1

    print(f"Found: {current_count} Jobs")

    jobs = page.locator("ul.EyBJWAsJeZqdckibssVhhKWmJliNWZofyFG li[data-occludable-job-id]")

    scrapped_jobs = []

    for i in range(current_count):
        print(f"Scraping {i+1}/{current_count} jobs")
        job = jobs.nth(i)
        job.scroll_into_view_if_needed()
        page.wait_for_timeout(500)
        title = job.locator(".artdeco-entity-lockup__title").inner_text()
        company = job.locator(".artdeco-entity-lockup__subtitle").inner_text()
        location = job.locator(".artdeco-entity-lockup__caption").inner_text()
        image = job.locator(".job-card-list__logo img").get_attribute('src')
        link_element = job.locator(".artdeco-entity-lockup__title a")

        raw_link_id = link_element.get_attribute('href').split("/")[3]
        link = f"https://www.linkedin.com/jobs/view/{raw_link_id}"

        link_element.click()
        details = page.locator("div[id='job-details']").inner_text()

        scrapped_jobs.append({
            "title": title,
            "company": company,
            "location": location,
            "link": link,
            "image": image,
            "details": details
        })

    with open("scraped/jobs.json", "w", encoding="utf-8") as f:
        json.dump(scrapped_jobs, f, ensure_ascii=False, indent=4)
    print("Done..!")
    browser.close()

