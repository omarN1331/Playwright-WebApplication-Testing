import re
from playwright.sync_api import Page, expect, sync_playwright
import pytest_playwright



def test_login_positive_01(page: Page):
    page.goto("http://52.19.50.152:40001/login")
    page.get_by_role("textbox", name="USERNAME").fill("supervisor")
    page.get_by_role("textbox", name="PASSWORD").fill("P@ssw0rd")
    page.get_by_role("button", name="LOGIN").click(button="left")
    expect(page.get_by_role("complementary")).to_match_aria_snapshot("- img \"Logo\"\n- text: Connector")
    page.close()

def test_login_positive_02(page: Page):
    page.goto("http://52.19.50.152:40001/login")
    page.get_by_role("textbox", name="PASSWORD").fill("P@ssw0rd")
    page.get_by_role("textbox", name="USERNAME").fill("supervisor")
    page.get_by_role("button", name="LOGIN").click(button="left")
    page.get_by_role("checkbox", name="REMEMBER ME").check()
    expect(page.get_by_role("complementary")).to_match_aria_snapshot("- img \"Logo\"\n- text: Connector")
    page.close()

def test_login_positive_03(page: Page):
    page.goto("http://52.19.50.152:40001/login")
    page.get_by_role("button", name="FORGOT PASSWORD?").click()
    expect(page.get_by_role("complementary")).to_match_aria_snapshot("- img \"Logo\"\n- text: Connector")
    page.close()


def test_login_positive_04(page: Page):
    page.goto("http://52.19.50.152:40001/login")
    page.get_by_role("textbox", name="PASSWORD").fill("P@ssw0rd")
    page.get_by_role("textbox", name="USERNAME").fill("supervisor")
    page.get_by_role("checkbox", name="REMEMBER ME").check()
    page.get_by_role("button", name="LOGIN").click(button="left")
    expect(page.get_by_role("complementary")).to_match_aria_snapshot("- img \"Logo\"\n- text: Connector")
    context = page.context
    page.close()
    new_page = context.new_page()
    new_page.goto("http://52.19.50.152:40001/login")
    expect(new_page.get_by_role("complementary")).to_match_aria_snapshot("- img \"Logo\"\n- text: Connector")

def test_login_positive_05(page: Page):
    page.goto("http://52.19.50.152:40001/login")
    page.get_by_role("button", name="FORGOT PASSWORD?").click()
    expect(page.get_by_role("complementary")).to_match_aria_snapshot("- img \"Logo\"\n- text: Connector")
    page.close()

def test_login_positive_06(context):
    page = context.new_page()
    page.goto("http://52.19.50.152:40001/login")
    page.get_by_role("textbox", name="USERNAME").fill("supervisor")
    page.get_by_role("textbox", name="PASSWORD").fill("P@ssw0rd")
    page.get_by_role("button", name="LOGIN").click(button="left")
    expect(page.get_by_role("complementary")).to_match_aria_snapshot("- img \"Logo\"\n- text: Connector")
    page2 = context.new_page()
    page2.goto("http://52.19.50.152:40001/login")
    page2.get_by_role("textbox", name="USERNAME").fill("supervisor")
    page2.get_by_role("textbox", name="PASSWORD").fill("P@ssw0rd")
    page2.get_by_role("button", name="LOGIN").click(button="left")
    expect(page2.get_by_role("complementary")).to_match_aria_snapshot("- img \"Logo\"\n- text: Connector")
    page.close()
    page2.close()



