#
employee_records = [('joe', 1, 53), ('beck', 2, 26), ('ele', 6, 32), ('neo', 3, 45), ('christ', 5, 33),
                    ('trinity', 4, 29)]

#
print sorted(employee_records, key=lambda emp: emp[0])

#
print sorted(employee_records, key=lambda emp: emp[1])

#
print sorted(employee_records, key=lambda emp: emp[2])