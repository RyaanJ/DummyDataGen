from faker import Faker

fake = Faker()
n = int(input("Enter the number of people you want to generate: "))

for i in range(n):
    print("------------------------")
    print("Name: " + fake.name())
    print("Address: " + fake.address())
    print("Email: " + fake.email())
    print("Phone Number: " + fake.phone_number())
    print("Job: " + fake.job())
    print("Company: " + fake.company())
    print("------------------------")
