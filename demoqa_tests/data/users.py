import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile_number: str
    day: str
    month: str
    year: str
    subjects: str
    hobbies: str
    photo: str
    current_address: str
    state: str
    city: str

user = User(first_name='Johnny',
            last_name='Wicky',
            email='johnny.wicky@continental.com',
            gender='Male',
            mobile_number='0123456789',
            year='1993',
            month='February',
            day='25',
            subjects='Arts',
            hobbies='Sports',
            photo='./resources/man.jpg',
            current_address='Rajasthan Continental',
            state='Rajasthan',
            city='Jaiselmer')