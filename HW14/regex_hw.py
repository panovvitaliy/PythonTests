import re

my_string = ("Place of delivery of goods: 82172, Ukraine, Lviv Region, Stryi, str. Doroshenko, 1. Deadline for "
             "delivery of goods: 31.12.2024")


if __name__ == '__main__':
    data = dict(country=re.search(r'(?<=\d{5},\s)[A-Za-z\s]+', my_string).group(),
                region=re.search(r'(\d{5},\s[A-Za-z\s]+,\s)([A-Za-z\s]+)', my_string).group(2),
                city=re.search(r'(\d{5},\s[A-Za-z\s]+,\s)([A-Za-z\s]+,\s)([A-Za-z\s]+)', my_string).group(3),
                postal=re.search(r'\b\d{5}\b', my_string).group(),
                address=re.search(r'(\d{5},\s[A-Za-z\s]+,\s[A-Za-z\s]+,\s[A-Za-z\s]+,\s)(.*)(?=.\sDeadline)',
                                  my_string).group(2),
                deadline=re.search(r'\d{2}\.\d{2}\.\d{4}', my_string).group())
    print(data)
