def calculate_monthly_mortgage_payment(principal, annual_interest_rate, loan_term_years):
    # Convert annual interest rate to a monthly rate
    monthly_interest_rate = annual_interest_rate / 100 / 12
    # Convert loan term in years to number of monthly payments
    number_of_payments = loan_term_years * 12
    
    # Calculate the monthly payment using the formula
    monthly_payment = (principal * monthly_interest_rate * (1 + monthly_interest_rate)**number_of_payments) / \
                      ((1 + monthly_interest_rate)**number_of_payments - 1)
    
    return monthly_payment

# Get user input
principal = float(input("Enter the principal amount (loan amount): "))
annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
loan_term_years = int(input("Enter the loan term (in years): "))

# Calculate the monthly mortgage payment
monthly_payment = calculate_monthly_mortgage_payment(principal, annual_interest_rate, loan_term_years)

# Print the result
print(f"The monthly mortgage payment is: ${monthly_payment:.2f}")
