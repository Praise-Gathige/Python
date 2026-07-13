while True:
    try:
        total_bill = float(input("What is the total bill? "))
        number_of_people = int(input("What is the total number of people? "))
        cost_per_person = total_bill / number_of_people

    except ValueError:
        print("Error. Please enter valid numbers.")
    except ZeroDivisionError:
        print("Error. You need at least one person to pay the bill.")
    else:
        print(f"Each person owes: ${cost_per_person}")
        break
    finally:
        print("--- Transaction Attempt Concluded ---")