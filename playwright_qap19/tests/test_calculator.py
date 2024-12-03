from playwright.sync_api import Page, expect


def test_calculator(page: Page):
    page.goto('https://testpages.eviltester.com/styled/calculator')
    number1, number2 = 10, 12
    page.locator('id=number1').fill(str(number1))
    page.locator('id=number2').fill(str(number2))

    page.locator('id=calculate').click()

    expect(page.locator('id=answer')).to_have_text(str(number1 + number2))
