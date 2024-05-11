import random

def generate_otp():
    # Generate a 6-digit OTP
    return ''.join(random.choices('0123456789', k=6))