
class Employee:
    no_of_leaves = 8
    pass

mustafa = Employee()
hassan = Employee()

mustafa.name = "Mustafa"
mustafa.salary = 455

mustafa.role = "Instructor"

hassan.name = "Hassan"
hassan.salary = 4554
hassan.role = "Student"

print(Employee.no_of_leaves)
print(Employee.__dict__)
Employee.no_of_leaves = 9
print(Employee.__dict__)
print(Employee.no_of_leaves)

