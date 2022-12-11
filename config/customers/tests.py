from django.test import TestCase
from .models import Customer, Address, Profile, OtpCode


class CustomerTestCase(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(user_name="masoud", email="masoudpro2@gmail.com",
                                                phone_number="09120572655", password="123456")

    def test_customer_creation(self):
        self.assertEqual(self.customer.user_name, "masoud")
        self.assertEqual(self.customer.email, "masoudpro2@gmail.com")
        self.assertEqual(self.customer.phone_number, "09120572655")

    def test_customer_str(self):
        self.assertEqual(str(self.customer), "masoud")


class ProfileTestCase(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(user_name="masoud", email="masoudpro2@gmail.com",
                                                phone_number="09120572655", password="123456")
        self.profile = Profile.objects.create(customer=self.customer, first_name="masoud", last_name="zandi",
                                              gender="male", birth_date="1997-07-09", image="profile_image")

    def test_profile_creation(self):
        self.assertEqual(self.profile.first_name, "masoud")
        self.assertEqual(self.profile.last_name, "zandi")
        self.assertEqual(self.profile.gender, "male")
        self.assertEqual(self.profile.birth_date, "1997-07-09")
        self.assertEqual(self.profile.image, "profile_image")

    def test_profile_str(self):
        self.assertEqual(str(self.profile), "masoud")


class AddressTestCase(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(user_name="masoud", email="masoudpro2@gmail.com",
                                                phone_number="09120572655", password="123456")
        self.profile = Profile.objects.create(customer=self.customer, first_name="masoud", last_name="zandi",
                                              gender="male", birth_date="1997-07-09", image="profile_image")
        self.address = Address.objects.create(profile=self.profile, province="tehran", city="tehran",
                                              address1="tehranapars", address2="mofateh", tel="02177721111",
                                              postal_code="1234567890")

    def test_address_creation(self):
        self.assertEqual(self.address.province, "tehran")
        self.assertEqual(self.address.city, "tehran")
        self.assertEqual(self.address.address1, "tehranapars")
        self.assertEqual(self.address.address2, "mofateh")
        self.assertEqual(self.address.tel, "02177721111")
        self.assertEqual(self.address.postal_code, "1234567890")

    def test_address_str(self):
        self.assertEqual(str(self.address), "tehran")


class OtpCodeTestCase(TestCase):
    def setUp(self):
        self.otp_code = OtpCode.objects.create(phone_number="09120572655", code=123456, email="masourpro2@gmail.com")

    def test_otp_code_creation(self):
        self.assertEqual(self.otp_code.phone_number, "09120572655")
        self.assertEqual(self.otp_code.code, 123456)
        self.assertEqual(self.otp_code.email, "masourpro2@gmail.com")

    def test_otp_code_str(self):
        self.assertEqual(str(self.otp_code), "09120572655")
