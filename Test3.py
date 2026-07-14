def calculate_tax(*salaries):
    try:
        lam = lambda salary: salary * 0.10
        taxes = map(lam, salaries)
        print("Tax for each month: ", list(taxes))
        total_tax = sum(taxes)
        return total_tax

    except TypeError:
        print("Type Error: Salary must be a number.")

    except Exception as e:
        print("Error:", e)

total = calculate_tax(50000, 45000, 60000, 55000)
print("Total Tax: ", total)