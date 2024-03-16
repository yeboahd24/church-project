import random
import string

from django.utils.crypto import get_random_string


def generate_profile_id():
    """Generate a string like 'asac2323'."""
    letters = random.choices(string.ascii_lowercase, k=4)
    digits = random.choices(string.digits, k=4)
    return "".join(letters + digits)


def create_random_password():
    """
    Generate a random password.

    Returns:
        str: The randomly generated password.
    """
    password = get_random_string(length=20)  # Generate a random string of length 20
    return password