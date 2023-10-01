# Constants
FEDERAL_STANDARD_DEDUCTION = 13200  # 2023 value
STATE_STANDARD_DEDUCTION = {
    'California': 4609,  # 2023 value for single filers
    'New York': 8000     # Using the previous value as it was not specified in the link
}

FEDERAL_TAX_BRACKETS = [
    (10400, 0.10),
    (41225, 0.12),
    (89400, 0.22),
    (174050, 0.24),
    (215400, 0.32),
    (549900, 0.35),
    (1000000, 0.37)
]

STATE_TAX_BRACKETS = {
    'California': [
        (9076, 0.01),
        (22771, 0.02),
        (34211, 0.04),
        (48898, 0.06),
        (48897, 0.08),
        (59878, 0.093),
        (71805, 0.103),
        (100000, 0.113)
    ],
    'New York': [
        (8500, 0.04),
        (11700, 0.045),
        (13900, 0.0525),
        (21400, 0.059),
        (80650, 0.0645),
        (215400, 0.0685),
        (1077550, 0.0882),
        (1000000, 0.103)
    ]
}

def calculate_tax(income, brackets):
    tax = 0
    for bracket in brackets:
        if income > bracket[0]:
            tax += bracket[0] * bracket[1]
            income -= bracket[0]
        else:
            tax += income * bracket[1]
            break
    return tax

def main():
    # User Input
    GROSS_SALARY = float(input("Enter your gross salary: "))
    STATE = input("Enter your state (California or New York): ")

    # Federal Tax
    deducted_salary = GROSS_SALARY - FEDERAL_STANDARD_DEDUCTION
    federal_tax = calculate_tax(deducted_salary, FEDERAL_TAX_BRACKETS)

    # State Tax
    deducted_salary_state = GROSS_SALARY - STATE_STANDARD_DEDUCTION.get(STATE, 0)
    state_tax = calculate_tax(deducted_salary_state, STATE_TAX_BRACKETS[STATE])

    # FICA
    fica = 0.0765 * GROSS_SALARY if GROSS_SALARY < 147000 else (0.0765 * 147000)

    # Net Salary
    net_salary = GROSS_SALARY - (federal_tax + state_tax + fica)

    # Display
    print(f"Gross Salary: ${GROSS_SALARY}")
    print(f"Federal Tax: ${federal_tax}")
    print(f"State Tax ({STATE}): ${state_tax}")
    print(f"FICA: ${fica}")
    print(f"Net Salary: ${net_salary}")

if __name__ == "__main__":
    main()
