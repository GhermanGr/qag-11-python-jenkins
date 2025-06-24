import os.path
from selene import browser, be, by, have
import pytest
import conftest


'''
При заполнении всех обязательный полей в форме и нажатии на кнопку Submit, форма будет отправлена и
отобразится её заполненный вариант, соответствующий тестовым данным.
'''
def test_registration_form_send(setup_formpage_chrome):
    #Заполнение базовых полей
    browser.element('#firstName').type('Johnny')
    browser.element('#lastName').type('Wicky')
    browser.element('#userEmail').type('johnny.wicky@continental.com')
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


    #Отправка картинки
    browser.element('#uploadPicture').send_keys(r'D:\Python\Projects\qaguru-pb-hw\qaguru-pb-hw-5\tests\resources\man.jpg')
    #Относительный путь отправки картинки я не сделал, т.к. даже после просмотра разбора ДЗ я не понял, как это правильно делается. Буду разбираться потом.

    #Заполнение полей штата Rajasthan и города Jaiselmer
    browser.element('#state').click()
    browser.element(by.text('Rajasthan')).click()

    browser.element('#city').click()
    browser.element(by.text('Jaiselmer')).click()


    #Отправка и проверка формы
    browser.element('#submit').click()

    browser.element('.table').all('td').should(
        have.texts(
            'Student Name','Johnny Wicky',
            'Student Email','johnny.wicky@continental.com',
            'Gender','Male',
            'Mobile','0123456789',
            'Date of Birth','25 February,1993',
            'Subjects','Arts',
            'Hobbies','Sports, Music',
            'Picture','man.jpg',
            'Address','Rajasthan Continental',
            'State and City','Rajasthan Jaiselmer'
        )
    )





