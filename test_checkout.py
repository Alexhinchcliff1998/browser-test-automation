import os
from pathlib import Path
import pytest
from playwright.sync_api import sync_playwright,expect
P=Path(__file__).parent
@pytest.fixture
def page(request):
    with sync_playwright() as pw:
        options={'headless':True}
        if os.getenv('CHROMIUM_PATH'):options['executable_path']=os.getenv('CHROMIUM_PATH')
        browser=pw.chromium.launch(**options);page=browser.new_page();page.set_content((P/'checkout.html').read_text())
        yield page
        if getattr(request.node,'rep_call',None) and request.node.rep_call.failed:
            folder=P/'artifacts';folder.mkdir(exist_ok=True);page.screenshot(path=str(folder/(request.node.name+'.png')))
        browser.close()
def test_quantity_and_total(page):
    page.locator('#add').click(click_count=2);expect(page.locator('#qty')).to_have_text('2');expect(page.locator('#total')).to_have_text('$24.00')
    page.locator('#remove').click();expect(page.locator('#total')).to_have_text('$12.00')
def test_empty_cart(page):
    page.locator('#email').fill('demo@example.test');page.locator('#terms').check();page.get_by_role('button',name='Place order').click()
    expect(page.get_by_role('status')).to_have_text('Your cart is empty.')
def test_email_validation(page):
    page.locator('#add').click();page.locator('#email').fill('bad');page.locator('#terms').check();page.get_by_role('button',name='Place order').click()
    assert not page.locator('#email').evaluate('(e)=>e.validity.valid')
def test_terms_required(page):
    page.locator('#add').click();page.locator('#email').fill('demo@example.test');page.get_by_role('button',name='Place order').click()
    assert not page.locator('#terms').evaluate('(e)=>e.validity.valid')
def test_success(page):
    page.locator('#add').click();page.locator('#email').fill('demo@example.test');page.locator('#terms').check();page.get_by_role('button',name='Place order').click()
    expect(page.get_by_role('status')).to_have_text('Demo order confirmed.');expect(page.locator('#qty')).to_have_text('0')
def test_keyboard_and_lower_bound(page):
    page.locator('#add').focus();page.keyboard.press('Enter');expect(page.locator('#qty')).to_have_text('1');page.locator('#remove').click(click_count=2);expect(page.locator('#qty')).to_have_text('0')
