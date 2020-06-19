import pytest
from pytest_django.asserts import TestCase

from djhl.user.models import User


class UserModelTest(TestCase):
    def setUp(self) -> None:
        self.user_common = User.objects.create_user(
            name="Fulano de Tal",
            email="fulano@djhl.com.br"
        )
        self.user_admin = User.objects.create_superuser(
            name="Beltrano de Tal",
            email="beltrano@djhl.com.br"
        )

    @pytest.mark.django_db
    def test_create(self):
        self.assertTrue(User.objects.exists())

    @pytest.mark.django_db
    def test_str(self):
        """"Must return name of user"""
        self.assertTrue(self.user_common, "Fulano de Tal")
        self.assertTrue(self.user_admin, "Beltrano de Tal")

    @pytest.mark.django_db
    def test_get_user_by_email(self):
        """Must return users searched by email"""
        user_common = User.objects.get(email="fulano@djhl.com.br")
        user_admin = User.objects.get(email="beltrano@djhl.com.br")
        self.assertTrue(self.user_common, user_common)
        self.assertTrue(self.user_admin, user_admin)

    @pytest.mark.django_db
    def test_user_not_is_staff(self):
        """Must return false if you are not a superuser"""
        self.assertFalse(self.user_common.is_staff)

    @pytest.mark.django_db
    def test_user_is_staff(self):
        """Must return true if superuser"""
        self.assertTrue(self.user_admin.is_staff)
