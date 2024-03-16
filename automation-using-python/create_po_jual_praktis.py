from playwright.sync_api import Playwright, sync_playwright, expect
import time


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
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
    page.goto("https://jual-dev.praktis.co/inbound/purchase-order/create")
    page.get_by_role("button", name="Vendor").click()
    page.locator("label").filter(has_text="elvan").click()
    page.get_by_placeholder("Input Vendor Address").click()
    page.get_by_placeholder("Input Vendor Address").fill(
        "apa aja test vendor playwright")
    page.get_by_role("button", name="Warehouse").click()
    page.locator("label").filter(has_text="Apa Aja HQ33").click()
    page.get_by_role("button", name="Expected Delivery Date").click()
    page.get_by_role("button", name="10th February (Saturday)").click()
    page.get_by_placeholder("Input Notes Here").click()
    page.get_by_placeholder("Input Notes Here").fill("test euy")
    page.get_by_role("button", name="+ Add Items").click()
    page.get_by_placeholder("Search Item Name or Item SKU").click()
    page.get_by_placeholder("Search Item Name or Item SKU").press("CapsLock")
    page.get_by_placeholder("Search Item Name or Item SKU").fill("GGS-001")
    page.get_by_placeholder("Search Item Name or Item SKU").press("Enter")
    page.get_by_role(
        "row", name="GGS-001 Ganteng Ganteng").get_by_role("img").click()
    page.get_by_role("button", name="Add 1 Item").click()
    page.get_by_placeholder("0").first.click()
    page.get_by_role("button", name="Save as Draft").click()
    time.sleep(5)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
