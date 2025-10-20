from playwright.sync_api import Page, expect
import pytest
from conftest import USERNAME, PASSWORD



@pytest.mark.tc(id="TC-LOGIN-POS-001", sheet="Login - Positive")
def test_login_positive_01(page: Page):
    """Corresponds to TC-LOGIN-POS-001: Enter valid username and valid password"""
    page.goto("http://52.19.50.152:40001/login")
    page.get_by_role("textbox", name="USERNAME").fill(USERNAME)
    page.get_by_role("textbox", name="PASSWORD").fill(PASSWORD)
    page.get_by_role("button", name="LOGIN").click(button="left")
    expect(page.get_by_role("complementary")).to_be_visible()


@pytest.mark.tc(id="TC-LOGIN-POS-002", sheet="Login - Positive")
def test_login_positive_02(page: Page):
    """Corresponds to TC-LOGIN-POS-002: Login with 'Remember Me' checked"""
    page.goto("http://52.19.50.152:40001/login")
    page.get_by_role("textbox", name="PASSWORD").fill(PASSWORD)
    page.get_by_role("textbox", name="USERNAME").fill(USERNAME)
    page.get_by_role("checkbox", name="REMEMBER ME").check()
    page.get_by_role("button", name="LOGIN").click(button="left")
    expect(page.get_by_role("complementary")).to_be_visible()

@pytest.mark.xfail(reason="Feature to be Added") # Feature not added yet
@pytest.mark.tc(id="TC-LOGIN-POS-003", sheet="Login - Positive")
def test_login_positive_03(page: Page):
    page.goto("http://52.19.50.152:40001/login")
    page.get_by_role("button", name="FORGOT PASSWORD?").click()
    expect(page.get_by_role("complementary")).to_match_aria_snapshot("- img \"Logo\"\n- text: Connector")
    page.close()


@pytest.mark.tc(id="TC-LOGIN-POS-004", sheet="Login - Positive")
def test_login_positive_04(page: Page):
    """Corresponds to TC-LOGIN-POS-004: Verify 'Remember Me' works after closing tab"""
    page.goto("http://52.19.50.152:40001/login")
    page.get_by_role("textbox", name="PASSWORD").fill(PASSWORD)
    page.get_by_role("textbox", name="USERNAME").fill(USERNAME)
    page.get_by_role("checkbox", name="REMEMBER ME").check()
    page.get_by_role("button", name="LOGIN").click(button="left")
    expect(page.get_by_role("complementary")).to_be_visible()
    context = page.context
    page.close()
    new_page = context.new_page()
    new_page.goto("http://52.19.50.152:40001/superdashboard")
    expect(new_page.get_by_role("complementary")).to_be_visible()

@pytest.mark.xfail(Reason="Feature to be Added") # Feature not added yet
@pytest.mark.tc(id="TC-LOGIN-POS-005", sheet="Login - Positive")
def test_login_positive_05(page: Page):
    """Corresponds to TC-LOGIN-POS-005: Verify 'Forgot password?' link"""
    page.goto("http://52.19.50.152:40001/login")
    page.get_by_role("button", name="FORGOT PASSWORD?").click()
    expect(page.get_by_role("complementary")).to_match_aria_snapshot("- img \"Logo\"\n- text: Connector")
    page.close()


@pytest.mark.tc(id="TC-LOGIN-POS-006", sheet="Login - Positive")
def test_login_positive_06(context):
    """Corresponds to TC-LOGIN-POS-006: Simultaneous logins (using two contexts)"""
    page1 = context.new_page()
    page1.goto("http://52.19.50.152:40001/login")
    page1.get_by_role("textbox", name="USERNAME").fill(USERNAME)
    page1.get_by_role("textbox", name="PASSWORD").fill(PASSWORD)
    page1.get_by_role("button", name="LOGIN").click(button="left")
    expect(page1.get_by_role("complementary")).to_be_visible()

    context2 = page1.context.browser.new_context()
    page2 = context2.new_page()
    page2.goto("http://52.19.50.152:40001/login")
    page2.get_by_role("textbox", name="USERNAME").fill(USERNAME)
    page2.get_by_role("textbox", name="PASSWORD").fill(PASSWORD)
    page2.get_by_role("button", name="LOGIN").click(button="left")
    expect(page2.get_by_role("complementary")).to_be_visible()
