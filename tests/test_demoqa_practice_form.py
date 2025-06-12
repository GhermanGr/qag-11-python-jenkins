from selene import browser, be, by
import pytest
import conftest

# При заполнении всех обязательный полей в форме и нажатии на кнопку Submit, форма будет отправлена и
# отобразится ...
def test_practice_from_send(setup_formpage_chrome):
    #Заполнение базовых полей
    browser.element('#firstName').type('Johnny')
    browser.element('#lastName').type("Wicky")
    browser.element('#userEmail').type("johnny.wicky@continental.com")
    browser.element('[for=gender-radio-1]').click()
    browser.element('#userNumber').type('7777777777')
    browser.element('#subjectsInput').type('Arts').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#currentAddress').type('Rajasthan Continental')

    #Заполнение даты рождения
    browser.element('#dateOfBirthInput').click()
    browser.element('[class="react-datepicker__year-select"]').click().element('option[value="1993"]').click()
    browser.element('[class="react-datepicker__month-select"]').click().element('option[value="1"]').click()
    browser.element('[aria-label="Choose Thursday, February 25th, 1993"]').click()

    #Заполнение полей штата и города
    browser.element('#state').click()
    browser.element(by.text('Rajasthan')).click()
    browser.element('#city').click()
    browser.element(by.text('Jaiselmer')).click()

    #Отправка и проверка формы
    browser.element('#submit').click()

    browser.element(by.text('Thanks for submitting the form').should(be.visible))





