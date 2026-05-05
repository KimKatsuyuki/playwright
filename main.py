import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.gov.br/cdtn/pt-br/centrais-de-conteudo/noticias?form.submitted=1&texto=&dt_inicio=&dt_fim=&categoria=")
    
    # ---------------------
    page.pause()
    # context.close()
    # browser.close()


with sync_playwright() as playwright:
    run(playwright)
