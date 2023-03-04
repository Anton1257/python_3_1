from datetime import *
from application.salary import *
from application.db.people import *
from qt import *


def get_current_date():
    return f'Текущая дата: {datetime.now().date()}'


def main():
    show_qt_widget(get_current_date(), calculate_salary())
    show_qt_widget(get_current_date(), get_employees())


if __name__ == '__main__':
    main()