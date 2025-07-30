from demoqa_tests.model.pages.registration_page import RegistrationPage
from demoqa_tests.data.users import user


'''
Верхне-уровневый тест регистрационной формы.
При заполнении всех обязательный полей в форме и нажатии на кнопку Submit, форма будет отправлена и
отобразится её заполненный вариант, соответствующий тестовым данным.
'''

def test_page_object():
    registration_page = RegistrationPage()

    registration_page.open()
    registration_page.register(user)
    registration_page.submit()

    registration_page.should_have_registered(
        'Johnny', 'Wicky', 'johnny.wicky@continental.com', 'Male',
        '0123456789', '25', 'February','1993', 'Arts', 'Sports',
        'man.jpg', 'Rajasthan Continental','Rajasthan','Jaiselmer'
    )




