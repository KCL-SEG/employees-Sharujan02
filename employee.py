"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:

    def __init__(self, name, salary_type, salary_amount):
        self.name = name
        self.salary_type = salary_type
        self.salary_amount = salary_amount

    def getContractHours(self):
        if self.salary_type == 'contract':
            hours = list(self.salary_amount.keys())[0]
        return hours
    
    def getContractPPHours(self):
        if self.salary_type == 'contract':
            pay_per_hour = self.salary_amount[self.getContractHours()]
        return pay_per_hour

    def get_pay(self):
        if self.salary_type == 'monthly':
            pay = self.salary_amount
        elif self.salary_type == 'contract':
            hours = self.getContractHours()
            pay_per_hour = self.getContractPPHours()
            pay = hours * pay_per_hour
        return pay

    def __str__(self):
        if self.salary_type == 'monthly':
            str = f"{self.name} works on a {self.salary_type} salary of {self.salary_amount}.  Their total pay is {self.get_pay()}."
        elif self.salary_type == 'contract':
            pay_per_hour = self.getContractPPHours()
            str = f"{self.name} works on a {self.salary_type} of {self.getContractHours()} hours at {pay_per_hour}/hour.  Their total pay is {self.get_pay()}."

        return str
    
class CommisionEmployee(Employee):
    def __init__(self, name, salary_type, salary_amount, contract_type, contract_amount):
        super().__init__(name, salary_type, salary_amount)
        self.contract_type = contract_type
        self.contract_amount = contract_amount

    def getContractCommisionNum(self):
        contract_num = list(self.contract_amount.keys())[0]
        return contract_num 
    
    def getContractCommisionAmount(self):
        pay_per_contract = self.contract_amount[self.getContractCommisionNum()]
        return pay_per_contract

    def get_pay(self):
        pay = super().get_pay()
        if self.contract_type == 'bonus_commision':
            pay += self.contract_amount
        elif self.contract_type == 'contract_commision':
            contract_num = self.getContractCommisionNum()
            pay_per_contract = self.getContractCommisionAmount()
            pay += contract_num * pay_per_contract
        return pay
    
    def __str__(self):
        if self.salary_type == 'monthly':
            if self.contract_type == 'contract_commision':
                str = f"{self.name} works on a {self.salary_type} salary of {self.salary_amount} and receives a commission for {self.getContractCommisionNum()} contract(s) at {self.getContractCommisionAmount()}/contract.  Their total pay is {self.get_pay()}."
            elif self.contract_type == 'bonus_commision':
                str = f"{self.name} works on a {self.salary_type} salary of {self.salary_amount} and receives a bonus commission of {self.contract_amount}.  Their total pay is {self.get_pay()}."
        elif self.salary_type == 'contract':
            if self.contract_type == 'contract_commision':
                str = f"{self.name} works on a contract of {super().getContractHours()} hours at {super().getContractPPHours()}/hour and receives a commission for {self.getContractCommisionNum()} contract(s) at {self.getContractCommisionAmount()}/contract.  Their total pay is {self.get_pay()}."
            elif self.contract_type == 'bonus_commision':
                str = f"{self.name} works on a contract of {super().getContractHours()} hours at {super().getContractPPHours()}/hour and receives a bonus commission of {self.contract_amount}.  Their total pay is {self.get_pay()}."
        return str


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 'monthly', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 'contract', {100: 25})

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = CommisionEmployee('Renee', 'monthly', 3000, "contract_commision", {4: 200})

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = CommisionEmployee('Jan', 'contract', {150: 25}, "contract_commision", {3: 220})

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = CommisionEmployee('Robbie', 'monthly', 2000, "bonus_commision", 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = CommisionEmployee('Ariel', 'contract', {120: 30}, "bonus_commision", 600)

print(billie.__str__())
print(charlie.__str__())
print(renee.__str__())
print(jan.__str__())
print(robbie.__str__())
print(ariel.__str__())