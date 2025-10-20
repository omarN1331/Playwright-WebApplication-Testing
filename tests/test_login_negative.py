from playwright.sync_api import Page, expect
import pytest
from conftest import USERNAME, PASSWORD


@pytest.mark.tc(id="TC-LOGIN-NEG-001", sheet="Login - Negative")
def test_login_negative_001(page: Page):
    """Corresponds to TC-LOGIN-NEG-001: Enter mixed-case username"""
    page.goto("http://52.19.50.152:40001/login")
    page.get_by_role("textbox", name="USERNAME").fill("SuperVisor")
    page.get_by_role("textbox", name="PASSWORD").fill(PASSWORD)
    page.get_by_role("button", name="LOGIN").click()
    error_popup = page.get_by_text("Login failed. Please check")
    expect(error_popup).to_be_visible()


@pytest.mark.tc(id="TC-LOGIN-NEG-002", sheet="Login - Negative")
def test_login_negative_002(page: Page):
    """Corresponds to TC-LOGIN-NEG-002: Enter unregistered username"""
    page.goto("http://52.19.50.152:40001/login")
    page.get_by_role("textbox", name="USERNAME").fill("USERNAME")
    page.get_by_role("textbox", name="PASSWORD").fill(PASSWORD)
    page.get_by_role("button", name="LOGIN").click()
    error_popup = page.get_by_text("Login failed. Please check")
    expect(error_popup).to_be_visible()


@pytest.mark.tc(id="TC-LOGIN-NEG-003", sheet="Login - Negative")
def test_login_negative_003(page: Page):
    """Corresponds to TC-LOGIN-NEG-003: Enter valid username with invalid Password"""
    page.goto("http://52.19.50.152:40001/login")
    page.get_by_role("textbox", name="USERNAME").fill(USERNAME)
    page.get_by_role("textbox", name="PASSWORD").fill(USERNAME)
    page.get_by_role("button", name="LOGIN").click()
    error_popup = page.get_by_text("Login failed. Please check")
    expect(error_popup).to_be_visible()


@pytest.mark.tc(id="TC-LOGIN-NEG-004", sheet="Login - Negative")
def test_login_negative_004(page: Page):
    """Corresponds to TC-LOGIN-NEG-004: Leave username field empty, enter valid password"""
    page.goto("http://52.19.50.152:40001/login")
    page.get_by_role("textbox", name="USERNAME").fill(" ")
    page.get_by_role("textbox", name="PASSWORD").fill(PASSWORD)
    page.get_by_role("button", name="LOGIN").click()
    error_popup = page.get_by_text("Login failed. Please check")
    expect(error_popup).to_be_visible()


@pytest.mark.tc(id="TC-LOGIN-NEG-005", sheet="Login - Negative")
def test_login_negative_005(page: Page):
    """Corresponds to TC-LOGIN-NEG-005: Enter valid username, leave password field empty"""
    page.goto("http://52.19.50.152:40001/login")
    page.get_by_role("textbox", name="USERNAME").fill(USERNAME)
    page.get_by_role("textbox", name="PASSWORD").fill(" ")
    page.get_by_role("button", name="LOGIN").click()
    error_popup = page.get_by_text("Login failed. Please check")
    expect(error_popup).to_be_visible()


@pytest.mark.tc(id="TC-LOGIN-NEG-006", sheet="Login - Negative")
def test_login_negative_006(page: Page):
    """Corresponds to TC-LOGIN-NEG-006: Leave both fields empty"""
    page.goto("http://52.19.50.152:40001/login")
    page.get_by_role("textbox", name="USERNAME").fill(" ")
    page.get_by_role("textbox", name="PASSWORD").fill(" ")
    page.get_by_role("button", name="LOGIN").click()
    error_popup = page.get_by_text("Login failed. Please check")
    expect(error_popup).to_be_visible()
