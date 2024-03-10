companies_dict = {}

while True:
    command = input()
    if command == "End":
        break

    split_command = command.split(" -> ")
    company_name = split_command[0]
    employee_id = split_command[1]

    if company_name not in companies_dict:
        companies_dict[company_name] = []
    if employee_id not in companies_dict[company_name]:
        companies_dict[company_name].append(employee_id)

for each_company, each_employee in companies_dict.items():
    print(each_company)
    for employee in each_employee:
        print(f"-- {employee}")