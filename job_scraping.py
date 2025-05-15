from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    user_data_dir = "/home/kadilana/.config/google-chrome/Profile 4"
    browser = p.chromium.launch_persistent_context(user_data_dir=user_data_dir, headless=False)
    context = browser.new_context()