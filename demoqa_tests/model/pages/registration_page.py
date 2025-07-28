import os
from selene import browser, have, by, command


class RegistrationPage:
    def __init__(self):
        pass

    def open(self):
        browser.config.window_width = 1920
        browser.config.window_height = 1080
        browser.open('https://demoqa.com/automation-practice-form')

    def fill_first_name(self, value):
        browser.element('#firstName').type(f'{value}')
        return self

    def fill_last_name(self, value):
        browser.element('#lastName').type(f'{value}')
        return self

    def fill_email(self, value):
        browser.element('#userEmail').type(f'{value}')
        return self

    def select_gender(self, value):
        browser.all('[name=gender]').element_by(have.value(f'{value}')).element('./following-sibling::label').click()
        return self

    def fill_phone_number(self, value):
        browser.element('#userNumber').type(f'{value}')
        return self

    def select_subjects(self, value):
        browser.element('#subjectsInput').type(f'{value}').press_enter()
        return self

    def select_hobbies(self, value):
        browser.all('[for^=hobbies-checkbox]').element_by(have.text(f'{value}')).click()
        return self

    def fill_current_address(self, value):
        browser.element('#currentAddress').type(f'{value}')
        return self

    def select_birthday(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element(
            '[class~=react-datepicker__year-select]'
        ).click().all('option').element_by(have.text(f'{year}')).click()

        browser.element(
            '[class~=react-datepicker__month-select]'
        ).click().all('option').element_by(have.text(f'{month}')).click()

        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()
        return self

    def upload_picture(self, value):
        browser.element('#uploadPicture').send_keys(os.path.abspath(f'{value}'))
        return self

    def select_state(self, value):
        browser.element('#state').click()
        browser.element(by.text(f'{value}')).click()
        return self

    def select_city(self, value):
        browser.element('#city').click()
        browser.element(by.text(f'{value}')).click()
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
