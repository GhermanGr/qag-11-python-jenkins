import os.path

from selene import browser, be, by, have
import pytest
import conftest
import tests



'''
При заполнении всех обязательный полей в форме и нажатии на кнопку Submit, форма будет отправлена и
отобразится ...
'''
def test_registration_form_send(setup_formpage_chrome):
    #Заполнение базовых полей
    browser.element('#firstName').type('Johnny')
    browser.element('#lastName').type("Wicky")
    browser.element('#userEmail').type("johnny.wicky@continental.com")
    browser.all('[name=gender]').element_by(have.value('Male')).element('./following-sibling::label').click()
    browser.element('#userNumber').type('0123456789')
    browser.element('#subjectsInput').type('Arts').press_enter()
    browser.all('[for^=hobbies-checkbox]').element_by(have.text('Sports')).click()
    browser.all('[for^=hobbies-checkbox]').element_by(have.text('Music')).click()
    browser.element('#currentAddress').type('Rajasthan Continental')

    #Заполнение даты рождения 25 февраля 1993
    browser.element('#dateOfBirthInput').click()
    browser.element(
        '[class~=react-datepicker__year-select]'
    ).click().all('option').element_by(have.text('1993')).click()

    browser.element(
        '[class~=react-datepicker__month-select]'
    ).click().all('option').element_by(have.text('February')).click()

    browser.element('[aria-label="Choose Thursday, February 25th, 1993"]').click()

    #Заполнение полей штата Rajasthan и города Jaiselmer
    browser.element('#state').click()
    browser.element(by.text('Rajasthan')).click()

    browser.element('#city').click()
    browser.element(by.text('Jaiselmer')).click()

    #Отправка и проверка формы
    browser.element('#submit').click()

    browser.element(by.text('Thanks for submitting the form').should(be.visible))





