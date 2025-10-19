from playwright.sync_api import Page, expect
import pytest
import pytest_playwright

@pytest.mark.tc(id="TC-LOGIN-POS-001", sheet="Login - Positive")
def test_login_positive_01(page: Page):
    """Corresponds to TC-LOGIN-POS-001: Enter valid username and valid password"""
    page.goto("http://52.19.50.152:40001/login")
    page.get_by_role("textbox", name="USERNAME").fill("supervisor")
    page.get_by_role("textbox", name="PASSWORD").fill("P@ssw0rd")
    page.get_by_role("button", name="LOGIN").click(button="left")
    expect(page.get_by_role("complementary")).to_be_visible()
    # Removed page.close() as pytest handles cleanup

@pytest.mark.tc(id="TC-LOGIN-POS-002", sheet="Login - Positive")
def test_login_positive_02(page: Page):
    """Corresponds to TC-LOGIN-POS-002: Login with 'Remember Me' checked"""
    page.goto("http://52.19.50.152:40001/login")
    page.get_by_role("textbox", name="PASSWORD").fill("P@ssw0rd")
    page.get_by_role("textbox", name="USERNAME").fill("supervisor")
    # **FIXED**: Check the box *before* clicking login
    page.get_by_role("checkbox", name="REMEMBER ME").check()
    page.get_by_role("button", name="LOGIN").click(button="left")
    expect(page.get_by_role("complementary")).to_be_visible()

@pytest.mark.tc(id="TC-LOGIN-POS-003", sheet="Login - Positive")
def test_login_positive_03(page: Page):
    page.goto("http://52.19.50.152:40001/login")
    page.get_by_role("button", name="FORGOT PASSWORD?").click()
    # For now we will assume that the page to be shown should be the complementary page
    expect(page.get_by_role("complementary")).to_match_aria_snapshot("- img \"Logo\"\n- text: Connector")
    page.close()

@pytest.mark.tc(id="TC-LOGIN-POS-004", sheet="Login - Positive")
def test_login_positive_04(page: Page):
    """Corresponds to TC-LOGIN-POS-004: Verify 'Remember Me' works after closing tab"""
    page.goto("http://52.19.50.152:40001/login")
    page.get_by_role("textbox", name="PASSWORD").fill("P@ssw0rd")
    page.get_by_role("textbox", name="USERNAME").fill("supervisor")
    page.get_by_role("checkbox", name="REMEMBER ME").check()
    page.get_by_role("button", name="LOGIN").click(button="left")
    expect(page.get_by_role("complementary")).to_be_visible()

    context = page.context
    page.close()

    new_page = context.new_page()
    new_page.goto("http://52.19.50.152:40001/login")
    expect(new_page.get_by_role("complementary")).to_be_visible()

@pytest.mark.tc(id="TC-LOGIN-POS-005", sheet="Login - Positive")
def test_login_positive_05(page: Page):
    """Corresponds to TC-LOGIN-POS-005: Verify 'Forgot password?' link"""
    page.goto("http://52.19.50.152:40001/login")
    page.get_by_role("button", name="FORGOT PASSWORD?").click()
    # For now we will assume that the page to be shown should be the complementary page
    expect(page.get_by_role("complementary")).to_match_aria_snapshot("- img \"Logo\"\n- text: Connector")
    page.close()

@pytest.mark.tc(id="TC-LOGIN-POS-006", sheet="Login - Positive")
def test_login_positive_06(context):
    """Corresponds to TC-LOGIN-POS-006: Simultaneous logins (using two contexts)"""
    # User 1 logs in
    page1 = context.new_page()
    page1.goto("http://52.19.50.152:40001/login")
    page1.get_by_role("textbox", name="USERNAME").fill("supervisor")
    page1.get_by_role("textbox", name="PASSWORD").fill("P@ssw0rd")
    page1.get_by_role("button", name="LOGIN").click(button="left")
    expect(page1.get_by_role("complementary")).to_be_visible()

    # User 2 logs in (in a separate context to be independent)
    context2 = page1.context.browser.new_context()
    page2 = context2.new_page()
    page2.goto("http://52.19.50.152:40001/login")
    page2.get_by_role("textbox", name="USERNAME").fill("supervisor") # Assuming another user, change if needed
    page2.get_by_role("textbox", name="PASSWORD").fill("P@ssw0rd")
    page2.get_by_role("button", name="LOGIN").click(button="left")
    expect(page2.get_by_role("complementary")).to_be_visible()
