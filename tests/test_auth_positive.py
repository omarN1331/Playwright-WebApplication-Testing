import re
from playwright.sync_api import Page, expect, Browser
import pytest
from conftest import EnvironmentVariables



@pytest.mark.tc(id="TC-LOGIN-POS-001", sheet="Authentication - Positive")
def test_authentication_positive_01(page: Page):
    """Corresponds to TC-LOGIN-POS-001: Enter valid username and valid password"""
    page.goto(EnvironmentVariables.BASE_URL)
    page.get_by_role("textbox", name="USERNAME").fill(EnvironmentVariables.USERNAME)
    page.get_by_role("textbox", name="PASSWORD").fill(EnvironmentVariables.PASSWORD)
    page.get_by_role("button", name="LOGIN").click()
    expect(page).to_have_url(re.compile(r".*/superdashboard"))

@pytest.mark.tc(id="TC-LOGIN-POS-002", sheet="Authentication - Positive")
def test_authentication_positive_02(page: Page):
    """Corresponds to TC-LOGIN-POS-002: Login with 'Remember Me' checked"""
    page.goto(EnvironmentVariables.BASE_URL)
    page.get_by_role("textbox", name="PASSWORD").fill(EnvironmentVariables.PASSWORD)
    page.get_by_role("textbox", name="USERNAME").fill(EnvironmentVariables.USERNAME)
    page.get_by_role("checkbox", name="REMEMBER ME").check()
    page.get_by_role("button", name="LOGIN").click()
    expect(page).to_have_url(re.compile(r".*/superdashboard"))

@pytest.mark.xfail(reason="Feature to be Added") # Feature not added yet
@pytest.mark.tc(id="TC-LOGIN-POS-003", sheet="Authentication - Positive")
def test_authentication_positive_03(page: Page):
    page.goto(EnvironmentVariables.BASE_URL)
    page.get_by_role("button", name="FORGOT PASSWORD?").click()
    expect(page).to_have_url(re.compile(r".*/forgot-password"))

@pytest.mark.tc(id="TC-LOGIN-POS-004", sheet="Authentication - Positive")
def test_authentication_positive_04(browser: Browser):
    """Corresponds to TC-LOGIN-POS-004: Verify 'Remember Me' works after closing browser"""
    storage_state_path = "user_session_state.json"
    context = browser.new_context()
    page = context.new_page()
    page.goto(EnvironmentVariables.BASE_URL)
    page.get_by_role("textbox", name="PASSWORD").fill(EnvironmentVariables.PASSWORD)
    page.get_by_role("textbox", name="USERNAME").fill(EnvironmentVariables.USERNAME)
    page.get_by_role("checkbox", name="REMEMBER ME").check()
    page.get_by_role("button", name="LOGIN").click()
    expect(page).to_have_url(re.compile(r".*/superdashboard"))
    context.storage_state(path=storage_state_path)
    context.close()
    new_context = browser.new_context(storage_state=storage_state_path)
    new_page = new_context.new_page()
    new_page.goto(EnvironmentVariables.DASHBOARD_URL)
    expect(new_page).to_have_url(re.compile(r".*/superdashboard"))
    new_context.close()

@pytest.mark.xfail(reason="Feature to be Added") # Feature not added yet
@pytest.mark.tc(id="TC-LOGIN-POS-005", sheet="Authentication - Positive")
def test_authentication_positive_05(page: Page):
    """Corresponds to TC-LOGIN-POS-005: Verify 'Forgot password?' link"""
    page.goto(EnvironmentVariables.BASE_URL)
    page.get_by_role("button", name="FORGOT PASSWORD?").click()
    expect(page).to_have_url(re.compile(r".*/forgotpassword"))

@pytest.mark.tc(id="TC-LOGIN-POS-006", sheet="Authentication - Positive")
def test_authentication_positive_06(context):
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

@pytest.mark.tc(id="TC-LOGIN-POS-007", sheet="Authentication - Positive")
def test_authentication_positive_07(page: Page):
    """Corresponds to TC-LOGIN-POS-007: Verify successful logout from dashboard"""
    page.goto(EnvironmentVariables.BASE_URL)
    page.get_by_role("textbox", name="USERNAME").fill(EnvironmentVariables.USERNAME)
    page.get_by_role("textbox", name="PASSWORD").fill(EnvironmentVariables.PASSWORD)
    page.get_by_role("button", name="LOGIN").click()
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Logout").click()
    expect(page.get_by_role("button", name="LOGIN")).to_be_visible()

@pytest.mark.tc(id="TC-LOGIN-POS-008", sheet="Authentication - Positive")
def test_authentication_positive_08(page: Page):
    """Corresponds to TC-Login-POS-008: Verify logout from different pages within application"""
    page.goto(EnvironmentVariables.BASE_URL)
    page.get_by_role("textbox", name="USERNAME").fill(EnvironmentVariables.USERNAME)
    page.get_by_role("textbox", name="PASSWORD").fill(EnvironmentVariables.PASSWORD)
    page.get_by_role("button", name="LOGIN").click()
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Logout").click()
    #-------------------------------------------------------
    page.get_by_role("textbox", name="USERNAME").fill(EnvironmentVariables.USERNAME)
    page.get_by_role("textbox", name="PASSWORD").fill(EnvironmentVariables.PASSWORD)
    page.get_by_role("button", name="LOGIN").click()
    page.get_by_role("link", name="Properties").click()
    expect(page).to_have_url(re.compile(r".*/properties"))
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Logout").click()
    #-------------------------------------------------------
    page.get_by_role("textbox", name="USERNAME").fill(EnvironmentVariables.USERNAME)
    page.get_by_role("textbox", name="PASSWORD").fill(EnvironmentVariables.PASSWORD)
    page.get_by_role("button", name="LOGIN").click()
    page.get_by_role("link", name="Api Scope").click()
    expect(page).to_have_url(re.compile(r".*/api-docs"))
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Logout").click()

@pytest.mark.tc(id="TC-LOGIN-POS-009", sheet="Authentication - Positive")
def test_authentication_positive_09(page: Page):
    """Corresponds to TC-LOGIN-POS-009: Verify re-login after logout with same credentials"""
    page.goto(EnvironmentVariables.BASE_URL)
    page.get_by_role("textbox", name="USERNAME").fill(EnvironmentVariables.USERNAME)
    page.get_by_role("textbox", name="PASSWORD").fill(EnvironmentVariables.PASSWORD)
    page.get_by_role("button", name="LOGIN").click()
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Logout").click()
    #-------------------------------------------------------
    page.goto(EnvironmentVariables.BASE_URL)
    page.get_by_role("textbox", name="USERNAME").fill(EnvironmentVariables.USERNAME)
    page.get_by_role("textbox", name="PASSWORD").fill(EnvironmentVariables.PASSWORD)
    page.get_by_role("button", name="LOGIN").click()
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Logout").click()

@pytest.mark.tc(id="TC-LOGIN-POS-010", sheet="Authentication - Positive")
def test_authentication_positive_010(page: Page):
    """Corresponds to TC-LOGIN-POS-010: Verify re-login after logout with different credentials"""
    page.goto(EnvironmentVariables.BASE_URL)
    page.get_by_role("textbox", name="USERNAME").fill(EnvironmentVariables.USERNAME)
    page.get_by_role("textbox", name="PASSWORD").fill(EnvironmentVariables.PASSWORD)
    page.get_by_role("button", name="LOGIN").click()
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Logout").click()
    #------------------------------------------------------
    page.goto(EnvironmentVariables.BASE_URL)
    page.get_by_role("textbox", name="USERNAME").fill(EnvironmentVariables.USERNAME_B)
    page.get_by_role("textbox", name="PASSWORD").fill(EnvironmentVariables.PASSWORD)
    page.get_by_role("button", name="LOGIN").click()
    expect(page).to_have_url(re.compile(r".*/dashboard"), timeout=15000)

@pytest.mark.tc(id="TC-LOGIN-POS-011", sheet="Authentication - Positive")
def test_authentication_positive_011(page: Page):
    """Corresponds to TC-LOGIN-POS-011: Verify logout button visibility after login"""
    page.goto(EnvironmentVariables.BASE_URL)
    page.get_by_role("textbox", name="USERNAME").fill(EnvironmentVariables.USERNAME)
    page.get_by_role("textbox", name="PASSWORD").fill(EnvironmentVariables.PASSWORD)
    page.get_by_role("button", name="LOGIN").click()
    expect(page.get_by_text("Logout", exact=True)).to_be_visible()