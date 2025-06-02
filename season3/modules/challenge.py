#  Generate a random 8-character password
import secrets
import string

def generate_random_password(length=8):
      """Generate a random password of specified length."""
      characters = string.ascii_letters + string.digits + string.punctuation
# The underscore _ is a convention to indicate that we don't care about the loop variable.
      password = ''.join(secrets.choice(characters) for _ in range(length))
      print(f'password: {password}')
      return password

print(generate_random_password(8))
