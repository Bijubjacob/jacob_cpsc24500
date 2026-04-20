"""
payroll_processor.py - Week 4 Starter

The PayrollProcessor manages a list of Employee objects and computes statistics.

Notes:
- self._employees should be private
- The `employees` property returns a COPY of the internal list (use list(self._employees))
- load_from_file() reads tab-delimited lines: name<TAB>id<TAB>rate<TAB>hours
- Skip blank lines and lines with the wrong number of fields (print a warning)
- Catch ValueError from the Employee constructor and print a warning
- Catch FileNotFoundError if the file doesn't exist
"""

from employee import Employee


class PayrollProcessor:

    def __init__(self):
        # TODO: initialize self._employees as an empty list
        self._employees = []

    @property
    def employees(self):
        # TODO: return a COPY of the list, not the original
        return list(self._employees)

    def load_from_file(self, filename):
        # TODO: open the file in a try/except for FileNotFoundError
        # TODO: for each line:
        #   - strip whitespace; skip blank lines
        #   - split on tab; if not exactly 4 fields, print a warning and continue
        #   - try to create an Employee; catch ValueError and print a warning
        #   - append to self._employees on success
        try:
            with open(filename, "r") as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue

                    parts = line.split("\t")
                    if len(parts) != 4:
                        print("Skipping bad line:", line)
                        continue

                    try:
                        name, eid, rate, hours = parts
                        emp = Employee(name, eid, float(rate), float(hours))
                        self._employees.append(emp)
                    except ValueError as e:
                        print("Invalid data:", line, e)

        except FileNotFoundError:
            print("File not found!")

    def calculate_total_payroll(self):
        # TODO: return the sum of gross pay across all employees
        return sum(emp.calculate_gross_pay() for emp in self._employees)

    def find_highest_paid(self):
        # TODO: return the Employee with the highest gross pay (or None if empty)
        return max(self._employees, key=lambda e: e.calculate_gross_pay(), default=None)

    def find_lowest_paid(self):
        # TODO: return the Employee with the lowest gross pay (or None if empty)
        return min(self._employees, key=lambda e: e.calculate_gross_pay(), default=None)

    def get_employee_count(self):
        # TODO
        return len(self._employees)

    def calculate_average_pay(self):
        # TODO: return total / count, or 0.0 if empty
        if not self._employees:
            return 0.0
        return self.calculate_total_payroll() / len(self._employees)
