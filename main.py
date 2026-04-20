"""
main.py - Week 4 Starter

Loads employees from employees.txt, then runs a menu loop.
"""

from payroll_processor import PayrollProcessor
from payroll_report import PayrollReport


def main():
    # TODO: create a PayrollProcessor
    # TODO: call load_from_file("employees.txt")
    # TODO: create a PayrollReport with the processor
    processor = PayrollProcessor()
    processor.load_from_file("employees.txt")

    report = PayrollReport(processor)

    # TODO: loop showing a menu:
    #   1. View all employees
    #   2. View payroll summary
    #   3. Generate report file
    #   4. Quit
    while True:
        print("\n1. View all employees")
        print("2. View payroll summary")
        print("3. Generate report file")
        print("4. Quit")

        choice = input("Enter choice: ")

        if choice == "1":
            report.display_all_employees()
        elif choice == "2":
            report.display_payroll_summary()
        elif choice == "3":
            report.generate_report_file("report.txt")
            print("Report saved!")
        elif choice == "4":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
