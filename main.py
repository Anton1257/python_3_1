from datetime import datetime as dt
from application.salary import calculate_salary
from application.db.people import get_employees
from qt import show_qt_widget


def get_current_date():
    return f'Текущая дата: {dt.now().date()}'


def main():
    show_qt_widget(get_current_date(), calculate_salary())
    show_qt_widget(get_current_date(), get_employees())


if __name__ == '__main__':
    main()