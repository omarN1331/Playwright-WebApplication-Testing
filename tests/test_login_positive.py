import re
from playwright.sync_api import Page, expect
import pytest
from conftest import EnvironmentVariables


@pytest.mark.tc(id="TC-LOGIN-POS-001", sheet="Login - Positive")
def test_login_positive_01(page: Page):
    """Corresponds to TC-LOGIN-POS-001: Enter valid username and valid password"""
    page.goto(EnvironmentVariables.BASE_URL)
    page.get_by_role("textbox", name="USERNAME").fill(EnvironmentVariables.USERNAME)
    page.get_by_role("textbox", name="PASSWORD").fill(EnvironmentVariables.PASSWORD)
    page.get_by_role("button", name="LOGIN").click()
    expect(page).to_have_url(re.compile(r".*/superdashboard"))
    


@pytest.mark.tc(id="TC-LOGIN-POS-002", sheet="Login - Positive")
def test_login_positive_02(page: Page):
    """Corresponds to TC-LOGIN-POS-002: Login with 'Remember Me' checked"""
    page.goto(EnvironmentVariables.BASE_URL)
    page.get_by_role("textbox", name="PASSWORD").fill(EnvironmentVariables.PASSWORD)
    page.get_by_role("textbox", name="USERNAME").fill(EnvironmentVariables.USERNAME)
    page.get_by_role("checkbox", name="REMEMBER ME").check()
    page.get_by_role("button", name="LOGIN").click()
    expect(page).to_have_url(re.compile(r".*/superdashboard"))
    

@pytest.mark.xfail(reason="Feature to be Added") # Feature not added yet
@pytest.mark.tc(id="TC-LOGIN-POS-003", sheet="Login - Positive")
def test_login_positive_03(page: Page):
    page.goto(EnvironmentVariables.BASE_URL)
    page.get_by_role("button", name="FORGOT PASSWORD?").click()
    expect(page).to_have_url(re.compile(r".*/forgot-password"))
    


@pytest.mark.tc(id="TC-LOGIN-POS-004", sheet="Login - Positive")
def test_login_positive_04(page: Page):
    """Corresponds to TC-LOGIN-POS-004: Verify 'Remember Me' works after closing tab"""
    page.goto(EnvironmentVariables.BASE_URL)
    page.get_by_role("textbox", name="PASSWORD").fill(EnvironmentVariables.PASSWORD)
    page.get_by_role("textbox", name="USERNAME").fill(EnvironmentVariables.USERNAME)
    page.get_by_role("checkbox", name="REMEMBER ME").check()
    page.get_by_role("button", name="LOGIN").click()
    expect(page).to_have_url(re.compile(r".*/superdashboard"))
    context = page.context
    
    new_page = context.new_page()
    new_page.goto(EnvironmentVariables.DASHBOARD_URL)
    expect(new_page).to_have_url(re.compile(r".*/superdashboard"))

@pytest.mark.xfail(reason="Feature to be Added") # Feature not added yet
@pytest.mark.tc(id="TC-LOGIN-POS-005", sheet="Login - Positive")
def test_login_positive_05(page: Page):
    """Corresponds to TC-LOGIN-POS-005: Verify 'Forgot password?' link"""
    page.goto(EnvironmentVariables.BASE_URL)
    page.get_by_role("button", name="FORGOT PASSWORD?").click()
    expect(page).to_have_url(re.compile(r".*/forgotpassword"))
    


@pytest.mark.tc(id="TC-LOGIN-POS-006", sheet="Login - Positive")
def test_login_positive_06(context):
    """Corresponds to TC-LOGIN-POS-006: Simultaneous logins (using two contexts)"""
    page1 = context.new_page()
    page1.goto(EnvironmentVariables.BASE_URL)
    page1.get_by_role("textbox", name="USERNAME").fill(EnvironmentVariables.USERNAME)
    page1.get_by_role("textbox", name="PASSWORD").fill(EnvironmentVariables.PASSWORD)
    page1.get_by_role("button", name="LOGIN").click()
    expect(page1).to_have_url(re.compile(r".*/superdashboard"))

    context2 = page1.context.browser.new_context()
    page2 = context2.new_page()
    page2.goto(EnvironmentVariables.BASE_URL)
    page2.get_by_role("textbox", name="USERNAME").fill(EnvironmentVariables.USERNAME)
    page2.get_by_role("textbox", name="PASSWORD").fill(EnvironmentVariables.PASSWORD)
    page2.get_by_role("button", name="LOGIN").click()
    expect(page2).to_have_url(re.compile(r".*/superdashboard"))
