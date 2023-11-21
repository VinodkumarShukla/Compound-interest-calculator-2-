def calculate_compound_interest(principal, rate, time):
    # Formula for compound interest
    compound_interest = principal * (1 + rate/100)**time - principal
    return compound_interest

# Example usage:
principal_amount = float(input("Enter the principal amount: "))
interest_rate = float(input("Enter the annual interest rate (%): "))
time_period = float(input("Enter the time period (in years): "))

# Calculate compound interest
interest = calculate_compound_interest(principal_amount, interest_rate, time_period)

# Display the result
print(f"The compound interest is: {interest:.2f}")