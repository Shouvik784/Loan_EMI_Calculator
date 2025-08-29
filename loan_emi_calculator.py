def calculate_emi(principal, annual_rate, years):
    """
    Calculate EMI using the formula:
    EMI = P * R * (1+R)^N / ((1+R)^N - 1)
    where:
    P = Principal amount
    R = Monthly interest rate (annual rate / 12 / 100)
    N = Loan tenure in months
    """
    # Convert annual rate to monthly and percentage to decimal
    monthly_rate = annual_rate / 12 / 100
    months = years * 12
    
    # Calculate EMI using the formula
    emi = (principal * monthly_rate * (1 + monthly_rate)**months) / \
          ((1 + monthly_rate)**months - 1)
    
    return emi

def get_float_input(prompt):
    """Helper function to get valid float input from user"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def get_int_input(prompt):
    """Helper function to get valid integer input from user"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")

def main():
    print("\n=== Loan EMI Calculator ===\n")
    
    # Get user inputs
    principal = get_float_input("Enter the principal amount (₹): ")
    annual_rate = get_float_input("Enter the annual interest rate (%): ")
    years = get_int_input("Enter the loan tenure (in years): ")
    
    # Calculate EMI
    emi = calculate_emi(principal, annual_rate, years)
    total_payment = emi * years * 12
    total_interest = total_payment - principal
    
    # Display results
    print("\n=== Loan Details ===")
    print(f"Principal Amount:      ₹{principal:,.2f}")
    print(f"Annual Interest Rate:  {annual_rate}%")
    print(f"Loan Tenure:           {years} years")
    print("\n=== EMI Calculation ===")
    print(f"Monthly EMI:           ₹{emi:,.2f}")
    print(f"Total Payment:         ₹{total_payment:,.2f}")
    print(f"Total Interest:        ₹{total_interest:,.2f}")

if __name__ == "__main__":
    while True:
        main()
        
        # Ask if user wants to calculate another EMI
        another = input("\nDo you want to calculate another EMI? (yes/no): ").lower()
        if another not in ['y', 'yes']:
            print("\nThank you for using the Loan EMI Calculator!")
            break
