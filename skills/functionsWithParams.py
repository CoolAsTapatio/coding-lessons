
def sum_of_three_salaries(s1, s2, s3):
	sall = s1 + s2 + s3
	return sall
'''def total_artist_salary(salarylist):
	sum1st3 = sum_of_three_salaries(salarylist[0],salarylist[1] , salarylist[2]) 
	sum2nd3 = sum_of_three_salaries(salarylist[3], salarylist[4], salarylist[5])
	sum3rd3 = sum_of_three_salaries(salarylist[6], salarylist[7], salarylist[8])
	sum_of_all = sum_of_three_salaries(sum1st3, sum2nd3, sum3rd3)
	return sum_of_all'''
def sum_total(salarylist):
	sums = 0
	for i in range(0, len(salarylist), 3):
		sums = sums + sum_of_three_salaries(salarylist[i], salarylist[i + 1], salarylist[i + 2])
	return sums	
if __name__ == "__main__":
	listartist = ["salvador dali", "vincent van gogh", "pablo picassa", "leonardo davinci", "rembrant", "michealangelo", "claude monet", "marcel duchamp", "andy warhol"]
	listofsalaries = [32023, 27058, 29502, 88058, 10202, 5032, 1010101, 32523, 52342]
	sum_var = sum_total(listofsalaries)
	print(sum_var)
	