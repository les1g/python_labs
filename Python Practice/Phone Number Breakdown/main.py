phone_number = int(input())

''' Type your code here. '''
area_code = phone_number // 10000000
office_code = ((phone_number // 10000) % 1000)
subscriber_number = phone_number % 10000

print(f'({area_code}) {office_code}-{subscriber_number}')

# Alternatively, using string formatting:
phone_str = str(phone_number).zfill(10)
area_code_str = phone_str[0:3]
office_code_str = phone_str[3:6]
subscriber_number_str = phone_str[6:10]
print(f'({area_code_str}) {office_code_str}-{subscriber_number_str}')