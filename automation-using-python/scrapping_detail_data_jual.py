from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=50)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://jual-dev.praktis.co/")
    page.get_by_role("button", name="Log In").click()
    page.get_by_placeholder("e g. John_123").click()
    page.get_by_placeholder("e g. John_123").press("CapsLock")
    page.get_by_placeholder("e g. John_123").fill("Nizar")
    page.get_by_placeholder("e g. John_123").press("Tab")
    page.get_by_placeholder("Input password").press("CapsLock")
    page.get_by_placeholder("Input password").fill("Login1234@")
    page.get_by_role("button", name="Sign In").click()
    page.get_by_role("button", name="Inbound").click()
    page.get_by_role("link", name="Purchase Order").click()
    page.fill("input[name=\"vendor\"]", "elvan")
