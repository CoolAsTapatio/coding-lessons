# Untitled.py
# Created by Kids on 1/19/21.

class Employee:
	def __init__(self, work_location_, superviser_name, salary, bonus, date_intiated):
		self.work_location = work_location_
		self.superviser_name = superviser_name
		self.job_detail = Job(salary, bonus, date_intiated)
	def get_bonus(self):
		return self.job_detail.bonus
	def get_salary(self):
		return self.job_detail.salary
	def get_date(self):
		return self.job_detail.date_init
	def get_superviser(self):
		return self.superviser_name
	def get_location(self):
		return self.work_location	
	def set_bonus(self, new_bonus):
		self.job_detail.bonus = new_bonus
	def set_salary(self, new_salary):
		self.job_detail.salary = new_salary
	def set_date(self, new_date):
		self.job_detail.date_init = new_date
	def set_superviser(self, new_superviser):
		self.superviser_name = new_superviser
	def set_location(self, new_location):
		self.work_location = new_location
class Job:
	def __init__(self, salary, bonus, date_init):
		self.salary = salary
		self.bonus = bonus
		self.date_init = date_init
if __name__ == "__main__":
	my_employee = Employee("kalihi", "me", 50, 100, "1/1/1")
	
	print(my_employee.get_bonus(), "\n", my_employee.get_salary(), "\n", my_employee.get_superviser(), "\n", my_employee.get_date(), "\n", my_employee.get_location())
	my_employee.set_bonus(1000)
	my_employee.set_salary(50)
	my_employee.set_date("1/2/21")
	my_employee.set_superviser("me")
	my_employee.set_location("mānoa")
	print(my_employee.get_bonus(), "\n", my_employee.get_salary(), "\n", my_employee.get_superviser(), "\n", my_employee.get_date(), "\n", my_employee.get_location())
	#finish calling setters, recall getters