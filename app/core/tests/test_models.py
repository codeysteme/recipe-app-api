"""
Tests for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test models."""

    def test_create_user_with_successfull(self):
        """Test create user with an email is successfull"""
        email = "test@example.com"
        password = "azerty123"
        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.password, password)

    def test_new_user_email_normolized(self):
        """Test email is normalized for new users."""
        sample_emails = [
            ["test@EXAMPLE.com", "test@example.com"],
            ["TEst1710@EXAMPLE.COm", "TEst1710@example.com"],
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, "azerty1710")
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_erro(self):
        """Test that creating a user without an email raists a ValueError."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user("", "test123")

    def test_create_superuser(self):
        """Test creating a superuser"""
        user = get_user_model().objects.create_superuser(
            "test@example.com", "tests11234"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
