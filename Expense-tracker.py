expense = "expense.txt"

def add_expense(amount,category):
    with open(expense, "a",encoding="utf-8") as f:
        f.write(str(amount) + "-"  + category + "\n")
    print("Expense Added")

def read_expense():
    try:
        with open(expense,"r", encoding="utf-8") as f:
            lines = f.readlines()

        if not lines:
            print("No Expense Saved Yet!")
            return
        
        print("\n------Your Expenses------")
        for i, line in enumerate(lines,1):   
            amount, category = line.strip().split("-")
            print(f"{i}. {amount} - {category}")
        
    except FileNotFoundError:
        print("No File Found")

def total_expense():
    try:
        with open(expense, "r", encoding="utf-8") as f:
            lines = f.readlines()
        total = 0
        
        for line in lines:
            amount, category = line.strip().split("-")
            total += int(amount)
        print(f"Total Expense: {total}")       
    except FileNotFoundError:
        print("No file")
        

def main():
    while True:
        print("----Select What You want to do (1-5)!-----")
        print("1. Add Expense to FIle: ")
        print("2. See the Expenses: ")
        print("3. Calculate the Expenses: ")
        print("4. Quit!")

        try:
            choice = int(input("Enter A No. (1-4): "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        if choice == 1:
            amount = int(input("Enter Amount Spend: "))
            category = input("Enter Category Amount spend on: ")
            add_expense(amount,category)
        elif choice == 2:
            read_expense()
        elif choice == 3:
            total_expense()
        elif choice == 4:
            print("Bye!")
            break
        else:
            print("Invalid Number")

main()