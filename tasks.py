import os
from pathlib import Path

from robocorp import browser, log
from robocorp.tasks import task


@task
def coolblue_voorbeeld():
    """
    Voorbeeld robot: open coolblue, zoek de iphone 17 en maak een screenshot!
    """
    browser.configure(
        browser_engine="chromium",
        screenshot="only-on-failure",
        headless=False,
    )
    try:
        page = browser.page()
        page.goto("https://www.coolblue.nl")

        # (Optional) handle cookie banner if it appears
        try:
            cookie_button = page.locator("button[name='accept_cookie']").first
            cookie_button.wait_for(state="visible", timeout=3000)
            cookie_button.click(timeout=3000)
        except Exception as e:
            log.info (e)

        # Locate the first input inside div.aap (your example used a different selector;
        # for Coolblue search, use their search input)
        search = page.locator("input[name='query']")

        log.info(search)

        search.wait_for(state="visible", timeout=3000)

        # Type text and press Enter
        search.fill("iphone 17")
        search.press("Enter")

        first_hit = page.locator(".product-card").first

        first_hit.screenshot( path="eerste_iphone.png")

    finally:
        # A place for teardown and cleanups. (Playwright handles browser closing)
        print("Automation finished!")



