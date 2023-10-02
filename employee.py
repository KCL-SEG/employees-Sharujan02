"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    
    def __init__(self, name, salary_type, salary_amount):
        self.name = name
        self.salary_type = salary_type
        self.salary_amount = salary_amount

    def get_pay(self):
        if self.salary_type == 'monthly':
            pay = self.salary_amount
        elif self.salary_type == 'contract':
            hours = list(self.salary_amount.keys())[0]
            pay_per_hour = self.salary_amount[hours]
            pay = hours * pay_per_hour
            
        return pay

    def __str__(self):
        return self.name
    
class CommisionEmployee(Employee):
    def __init__(self, name, salary_type, salary_amount, contract_amount):
        super().__init__(name, salary_type, salary_amount)
        self.contract_amount = contract_amount

    def get_pay(self):
        pay = super().get_pay()
        if type(self.contract_amount) == int:
            pay += self.contract_amount
        else:
            contract_num = list(self.contract_amount.keys())[0]
            pay_per_contract = self.contract_amount[contract_num]
            pay += contract_num * pay_per_contract
        return pay

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 'monthly', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 'contract', {100: 25})

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = CommisionEmployee('Renee', 'monthly', 3000, {4: 200})

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = CommisionEmployee('Jan', 'contract', {150: 25}, {3: 220})

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = CommisionEmployee('Robbie', 'monthly', 2000, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = CommisionEmployee('Ariel', 'contract', {120: 30}, 600)