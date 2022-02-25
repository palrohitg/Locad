import csv


class Employee():

    def __init__(self, max_profit=54000):
        self.max_profit = max_profit
        self.emp_details = self.get_emp_details()
        self.emp_ratings = self.get_emp_rating_details()
        self.rating_ratio_map = self.get_rating_ratio_map()
        self.emp_details_with_salary_ratio, self.total_rating_salary_emp = self.set_emp_details_with_salary_ratio()

    def get_emp_details(self):
        emp_details_list = []
        try:
            with open('emp.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    if line_count == 0:  # ignore first row
                        pass
                    else:
                        emp_details_list.append(list(row))
                    line_count += 1
            return emp_details_list
        except Exception as e:
            print("Error Occured {}", e)
        return None

    def get_emp_rating_details(self):
        try:
            emp_ratings = []
            with open('rating.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    if line_count == 0:  # ignore first row
                        pass
                    else:
                        emp_ratings.append(list(row))
                    line_count += 1
            return emp_ratings
        except Exception as e:
            print("Error Occured {}", e)

        return None

    def get_rating_ratio_map(self):
        rating_ration_map = {"A": 6, "B": 3, "C": 2}
        return rating_ration_map

    def set_emp_details_with_salary_ratio(self):
        emp_salary_rating = []
        total_rating_salary_emp = 0
        try:
            for i in range(0, len(self.emp_ratings)):
                print
                emp_detail = self.emp_details[i]
                emp_rating = self.emp_ratings[i]

                id = emp_detail[0] if emp_detail[0] else None
                rating = emp_rating[1] if emp_rating[1] else None
                salary = int(emp_detail[3]) if emp_detail[3] else None
                current_rating_salary = salary * self.rating_ratio_map[rating]
                total_rating_salary_emp += current_rating_salary

                emp_dic = {
                    "Id": id,
                    "Salary": salary,
                    "Rating": rating,
                    "salary_with_rating": current_rating_salary,
                }
                emp_salary_rating.append(emp_dic)
        except Exception as e:
            print("Error Occured {}", e)

        return emp_salary_rating, total_rating_salary_emp

    def get_bonus_allocation(self):
        results = []
        try:
            if self.emp_details_with_salary_ratio:
                for each_emp in self.emp_details_with_salary_ratio:
                    bonus_give = (each_emp.get("salary_with_rating")
                                  * self.max_profit) // self.total_rating_salary_emp
                    current_list = [each_emp.get("Id"), bonus_give]
                    results.append(current_list)
                return results
            else:
                return None
        except Exception as e:
            print("Error Occured {}", e)


if __name__ == "__main__":
    max_profit = 54000
    obj = Employee(max_profit)
    ans = obj.get_bonus_allocation()
    print(ans)
