import os
from selene import browser, have, by, command
from demoqa_tests.data.users import user


class RegistrationPage:
    def __init__(self):
        pass

    def open(self):
        browser.config.window_width = 1920
        browser.config.window_height = 1080
        browser.open('https://demoqa.com/automation-practice-form')

    def register(self, user):
        browser.element('#firstName').type(f'{user.first_name}')

        browser.element('#lastName').type(f'{user.last_name}')

        browser.element('#userEmail').type(f'{user.email}')

        browser.all('[name=gender]').element_by(have.value(f'{user.gender}')).element('./following-sibling::label').click()

        browser.element('#userNumber').type(f'{user.mobile_number}')

        browser.element('#subjectsInput').type(f'{user.subjects}').press_enter()

        browser.all('[for^=hobbies-checkbox]').element_by(have.text(f'{user.hobbies}')).click()
        
        browser.element('#currentAddress').type(f'{user.current_address}')

        #Select birthday
        browser.element('#dateOfBirthInput').click()
        browser.element(
            '[class~=react-datepicker__year-select]'
        ).click().all('option').element_by(have.text(f'{user.year}')).click()
        browser.element(
            '[class~=react-datepicker__month-select]'
        ).click().all('option').element_by(have.text(f'{user.month}')).click()
        browser.element(f'.react-datepicker__day--0{user.day}:not(.react-datepicker__day--outside-month)').click()

        browser.element('#uploadPicture').send_keys(os.path.abspath(f'{user.photo}'))

        browser.element('#state').click()
        browser.element(by.text(f'{user.state}')).click()

        browser.element('#city').click()
        browser.element(by.text(f'{user.city}')).click()

        return self

    def submit(self):
        browser.element('#submit').click()

    def should_have_registered(
            self, first_name, last_name, email, gender, phone_number, day, month, year, subjects, hobbies, photo,
            current_address, state, city
    ):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                f'{first_name} {last_name}',
                f'{email}',
                f'{gender}',
                f'{phone_number}',
                f'{day} {month},{year}',
                f'{subjects}',
                f'{hobbies}',
                f'{photo}',
                f'{current_address}',
                f'{state} {city}',
            )
        )
