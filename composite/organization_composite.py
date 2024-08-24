from abc import ABC, abstractmethod

# Component
class OrganizationComponent(ABC):
    @abstractmethod
    def get_salary(self):
        pass

    @abstractmethod
    def display(self):
        pass

# Leaf
class Employee(OrganizationComponent):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary

    def display(self):
        print(f'Employee: {self.name}, Salary: {self.salary}')

# Composite
class Department(OrganizationComponent):
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def get_salary(self):
        total_salary = sum(member.get_salary() for member in self.members)
        return total_salary

    def display(self):
        print(f'Department: {self.name}')
        for member in self.members:
            member.display()

# Usage example
if __name__ == "__main__":
    # Create employees
    emp1 = Employee("Alice", 5000)
    emp2 = Employee("Bob", 4000)
    emp3 = Employee("Charlie", 3000)
    emp3.display()

    # Create departments and add employees
    department1 = Department("HR")
    department1.add_member(emp1)
    department1.add_member(emp2)

    department2 = Department("Engineering")
    department2.add_member(emp3)

    # Create a top-level department and add sub-departments
    company = Department("Company")
    company.add_member(department1)
    company.add_member(department2)

    # Display organization structure and total salaries
    company.display()
    print(f'Total Salary in the company: {company.get_salary()}')
