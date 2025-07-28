from demoqa_tests.model.pages.registration_page import RegistrationPage


'''
Средне-уровневый тест регистрационной формы.
При заполнении всех обязательный полей в форме и нажатии на кнопку Submit, форма будет отправлена и
отобразится её заполненный вариант, соответствующий тестовым данным.
'''

def test_page_object():
    registration_page = RegistrationPage()

    registration_page.open()
    (
        registration_page
        .fill_first_name('Johnny')
        .fill_last_name('Wicky')
        .fill_email('johnny.wicky@continental.com')
        .select_gender('Male')
        .fill_phone_number('0123456789')
        .select_birthday('1993', 'February', '25')
        .select_subjects('Arts')
        .select_hobbies('Sports')
        .upload_picture('./resources/man.jpg')
        .fill_current_address('Rajasthan Continental')
        .select_state('Rajasthan')
        .select_city('Jaiselmer')
        .submit()
    )

    registration_page.should_have_registered(
        'Johnny', 'Wicky', 'johnny.wicky@continental.com', 'Male',
        '0123456789', '25', 'February','1993', 'Arts', 'Sports',
        'man.jpg', 'Rajasthan Continental','Rajasthan','Jaiselmer'
    )




