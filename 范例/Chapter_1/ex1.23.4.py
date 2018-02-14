from operator import itemgetter

#
employee_records = [('joe', 1, 53), ('beck', 2, 26), ('ele', 6, 32), ('neo', 3, 45), ('christ', 5, 33),
                    ('trinity', 4, 29)]

#
print sorted(employee_records, key=itemgetter(0))
print sorted(employee_records, key=itemgetter(0,1))

#
print sorted(employee_records, key=itemgetter(1))

#
print sorted(employee_records, key=itemgetter(2))


#
class employee(object):
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age

    def pretty_print(self):
        print self.name, self.id, self.age

    def random_method(self):
        return self.age / self.id


#
employee_records = []
emp1 = employee('joe', 1, 53)
emp2 = employee('beck', 2, 26)
emp3 = employee('ele', 6, 32)

employee_records.append(emp1)
employee_records.append(emp2)
employee_records.append(emp3)

#
for emp in employee_records:
    emp.pretty_print()

from operator import attrgetter, methodcaller

#
employee_records_sorted = sorted(employee_records, key=attrgetter('age'))
for emp in employee_records_sorted:
    emp.pretty_print()

#
employee_records_sorted = sorted(employee_records, key=methodcaller('random_method'))
for emp in employee_records_sorted:
    emp.pretty_print()
