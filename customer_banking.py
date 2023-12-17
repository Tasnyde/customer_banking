# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account import create_cd_account    

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = float(input("Enter the savings account balance: "))
    savings_interest = float(input("Enter the savings interest rate: "))    
    savings_maturity = int(input("Enter the number of months: ")) 

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance = savings_balance + (savings_balance * savings_interest * savings_maturity / 12)
    interest_earned_savings = updated_savings_balance - savings_balance
    
    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Savings Account - Updated Balance: {'{:,.2f}'.format(updated_savings_balance)}")
    print(f"Savings Account - Interest Earned: {'{:,.2f}'.format(interest_earned_savings)}")
   
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = float(input("Enter the CD account balance: "))
    cd_interest = float(input("Enter the CD interest rate: "))
    cd_maturity = int(input("Enter the number of months for CD: "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance = cd_balance + (cd_balance * cd_interest * cd_maturity / 12)
    interest_earned_cd = updated_cd_balance - cd_balance
    
    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"CD Account - Updated Balance: {'{:,.2f}'.format(updated_cd_balance)}")
    print(f"CD Account - Interest Earned: {'{:,.2f}'.format(interest_earned_cd)}")

if __name__ == "__main__":
    # Call the main function    
    main()
