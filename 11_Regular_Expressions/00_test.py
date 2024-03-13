### Match All Words
#
# import re
#
# regex = r"\w+"
#
# test_str = ("_ (Underscores) are also word characters!")
#
# matches = re.findall(regex, test_str)
# print(matches)

### Match Dates
#
# import re
#
# regex = r"\b\d{1,2}-[A-Z][a-z]{2}-\d{4}"
#
# text = ''''
# I am born on 30-Dec-1994.
#  My father is born on the 9-Jul-1955.
#  01-July-2000 is not a valid date.
#  '''
#
# matches = re.findall(regex, text)
# print(matches)

### Email Validation
#
# import re
#
# regex = r"^[a-zA-Z0-9_]+@+[a-zA-Z]+\.[a-zA-Z]+"
#
# email_data = ['valid123@email.bg', 'invalid*name@emai1.bg']
#
# for email in email_data:
#     if re.match(regex, email):
#         print(f"{email} is valid")
#     else:
#         print(f"{email} is not valid")