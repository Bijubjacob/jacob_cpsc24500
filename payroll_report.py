"""
payroll_report.py - Week 4 Starter

PayrollReport handles all display and file output. It does not store data itself --
it gets data from the PayrollProcessor passed into its constructor.
"""


class PayrollReport:

    def __init__(self, processor):
        # TODO: store the processor
        self._processor = processor

    def display_all_employees(self):
        # TODO: print a header row, then each employee on its own line
        # Use self._processor.employees to get the list
        print("=" * 60)
        print(f"{'Name':15} {'ID':6} {'Rate':>8} {'Hours':>6} {'Gross Pay':>12}")
        print("=" * 60)
        for emp in self._processor.employees:
            print(emp)
        print("=" * 60)

    def display_payroll_summary(self):
        # TODO: print total employees, total payroll, average pay,
        #       highest paid, lowest paid
        print("\n--- Payroll Summary ---")
        print("Total employees:", self._processor.get_employee_count())
        print("Total payroll: $", round(self._processor.calculate_total_payroll(), 2))
        print("Average pay: $", round(self._processor.calculate_average_pay(), 2))

        highest = self._processor.find_highest_paid()
        lowest = self._processor.find_lowest_paid()

        if highest:
            print(f"Highest paid: {highest.name} (${highest.calculate_gross_pay():.2f})")
        if lowest:
            print(f"Lowest paid: {lowest.name} (${lowest.calculate_gross_pay():.2f})")

    def generate_report_file(self, filename):
        # TODO: write the full report (employees + summary) to a text file
        # Use a `with` block
        with open(filename, "w") as f:
            f.write("Payroll Report\n")
            for emp in self._processor.employees:
                f.write(str(emp) + "\n")
