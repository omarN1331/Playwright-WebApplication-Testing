import re
from playwright.sync_api import Page, expect
import pytest
from conftest import EnvironmentVariables


@pytest.mark.tc(id="TC-LOGIN-NEG-001", sheet="Authentication - Negative")
def test_authentication_negative_001(page: Page):
    """Corresponds to TC-LOGIN-NEG-001: Enter mixed-case username"""
    page.goto(EnvironmentVariables.BASE_URL)
    page.get_by_role("textbox", name="USERNAME").fill("SuperVisor")
    page.get_by_role("textbox", name="PASSWORD").fill(EnvironmentVariables.PASSWORD)
    page.get_by_role("button", name="LOGIN").click(timeout=15000)
    error_popup = page.get_by_text("Login failed. Please check")
    expect(error_popup).to_be_visible()


@pytest.mark.tc(id="TC-LOGIN-NEG-002", sheet="Authentication - Negative")
def test_authentication_negative_002(page: Page):
    """Corresponds to TC-LOGIN-NEG-002: Enter unregistered username"""
    page.goto(EnvironmentVariables.BASE_URL)
    page.get_by_role("textbox", name="USERNAME").fill("USERNAME")
    page.get_by_role("textbox", name="PASSWORD").fill(EnvironmentVariables.PASSWORD)
    page.get_by_role("button", name="LOGIN").click()
    error_popup = page.get_by_text("Login failed. Please check")
    expect(error_popup).to_be_visible()

@pytest.mark.tc(id="TC-LOGIN-NEG-003", sheet="Authentication - Negative")
def test_authentication_negative_003(page: Page):
    """Corresponds to TC-LOGIN-NEG-003: Enter valid username with invalid Password"""
    page.goto(EnvironmentVariables.BASE_URL)
    page.get_by_role("textbox", name="USERNAME").fill(EnvironmentVariables.USERNAME)
    page.get_by_role("textbox", name="PASSWORD").fill(EnvironmentVariables.USERNAME)
    page.get_by_role("button", name="LOGIN").click()
    error_popup = page.get_by_text("Login failed. Please check")
    expect(error_popup).to_be_visible()

@pytest.mark.tc(id="TC-LOGIN-NEG-004", sheet="Authentication - Negative")
def test_authentication_negative_004(page: Page):
    """Corresponds to TC-LOGIN-NEG-004: Leave username field empty, enter valid password"""
    page.goto(EnvironmentVariables.BASE_URL)
    page.get_by_role("textbox", name="USERNAME").fill(" ")
    page.get_by_role("textbox", name="PASSWORD").fill(EnvironmentVariables.PASSWORD)
    page.get_by_role("button", name="LOGIN").click()
    error_popup = page.get_by_text("Login failed. Please check")
    expect(error_popup).to_be_visible()

@pytest.mark.tc(id="TC-LOGIN-NEG-005", sheet="Authentication - Negative")
def test_authentication_negative_005(page: Page):
    """Corresponds to TC-LOGIN-NEG-005: Enter valid username, leave password field empty"""
    page.goto(EnvironmentVariables.BASE_URL)
    page.get_by_role("textbox", name="USERNAME").fill(EnvironmentVariables.USERNAME)
    page.get_by_role("textbox", name="PASSWORD").fill(" ")
    page.get_by_role("button", name="LOGIN").click()
    error_popup = page.get_by_text("Login failed. Please check")
    expect(error_popup).to_be_visible()

@pytest.mark.tc(id="TC-LOGIN-NEG-006", sheet="Authentication - Negative")
def test_authentication_negative_006(page: Page):
    """Corresponds to TC-LOGIN-NEG-006: Leave both fields empty"""
    page.goto(EnvironmentVariables.BASE_URL)
    page.get_by_role("textbox", name="USERNAME").fill(" ")
    page.get_by_role("textbox", name="PASSWORD").fill(" ")
    page.get_by_role("button", name="LOGIN").click()
    error_popup = page.get_by_text("Login failed. Please check")
    expect(error_popup).to_be_visible()

@pytest.mark.tc(id="TC-LOGIN-NEG-007", sheet="Authentication - Negative")
def test_authentication_negative_007(page: Page):
    """Corresponds to TC-LOGIN-NEG-007: Verify browser back button after logout"""
    page.goto(EnvironmentVariables.BASE_URL)
    page.get_by_role("textbox", name="USERNAME").fill(EnvironmentVariables.USERNAME)
    page.get_by_role("textbox", name="PASSWORD").fill(EnvironmentVariables.PASSWORD)
    page.get_by_role("button", name="LOGIN").click()
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Logout").click()
    page.go_back()
    expect(page).not_to_have_url(re.compile(r".*/superdashboard"))

@pytest.mark.tc(id="TC-LOGIN-NEG-008", sheet="Authentication - Negative")
def test_authentication_negative_008(page: Page):
    """Corresponds to TC-LOGIN-NEG-008: Verify direct URL access after logout"""
    page.goto(EnvironmentVariables.BASE_URL)
    page.get_by_role("textbox", name="USERNAME").fill(EnvironmentVariables.USERNAME)
    page.get_by_role("textbox", name="PASSWORD").fill(EnvironmentVariables.PASSWORD)
    page.get_by_role("button", name="LOGIN").click()
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Logout").click()
    expect(page.get_by_text("Login", exact=True)).to_be_visible()
    page.goto(EnvironmentVariables.DASHBOARD_URL)
    expect(page).to_have_url(re.compile(r".*/login"))
