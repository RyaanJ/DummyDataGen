from faker import Faker
import random
import time

faker = Faker()


def generate_log_message():
    log_levels = ["DEBUG", "INFO", "WARNING", "ERROR"]
    log_level = random.choice(log_levels)
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    message = faker.sentence()
    return f"{timestamp} [{log_level}] - {message}"


# Generate 10 fake log messages
for i in range(10):
    print(generate_log_message())
