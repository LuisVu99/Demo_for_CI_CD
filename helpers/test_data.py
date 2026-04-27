from faker import Faker
import random

faker = Faker()

class TestData:
    @staticmethod
    def random_email(domain = "luisxyz.com"):
        return faker.user_name() + "@" + domain
    
    @staticmethod
    def random_first_name():
        return faker.first_name()
    
    @staticmethod
    def random_last_name():
        return faker.last_name()
    
    @staticmethod
    def random_user_name():
        return faker.user_name()
    
    @staticmethod
    def random_password():
        return faker.password()
    
    @staticmethod
    def random_company():
        return faker.company()
    
    @staticmethod
    def random_country():
        return faker.country()
    
    @staticmethod
    def randon_phone():
        return faker.phone_number()
    
    @staticmethod
    def randon_address():
        return faker.address()
    
    @staticmethod
    def random_title():
        return f"Title_{faker.word()}"
    
    @staticmethod
    def random_date_time():
        return faker.date_this_year().isoformat()
    
    @staticmethod
    def random_boolean():
        return faker.boolean()
    
    @staticmethod
    def random_int():
        return faker.random_int(min=1, max = 10000)