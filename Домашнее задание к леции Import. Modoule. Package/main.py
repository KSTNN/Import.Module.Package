from application.salary import calculate_salary
from application.db.people import get_employees

if __name__ == '__main__':
    print("Запуск программы 'Бухгалтерия'")
    calculate_salary()
    get_employees()
