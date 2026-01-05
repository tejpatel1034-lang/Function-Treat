"""
Thank you for using the Data Analyzer and Transformer Program. Goodbye!
"""
data = []
def summary(**kwargs):
    for key, value in kwargs.items():
        print(f"- {key}: {value}")


while True:
    print("\nWelcome to the Data Analyzer and Transformer Program")
    print("\nMain Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")

    choice = input("Please enter your choice: ")

    match choice:
        case "1":
          
            data = list(map(int, input(
                "Enter data for a 1D array (separated by spaces): "
            ).split()))
            print("Data has been stored successfully!")

        case "2":

            if not data:
                print("No data available")
            else:
                total = len(data)
                minimum = min(data)
                maximum = max(data)
                total_sum = sum(data)
                average = round(total_sum / total, 2)

                print("Data Summary:")
                summary(
                    **{
                        "Total elements": total,
                        "Minimum value": minimum,
                        "Maximum value": maximum,
                        "Sum of all values": total_sum,
                        "Average value": average
                    }
                )

      
        case "3":
          
            num = int(input("Enter a number to calculate its factorial: "))

            def factorial(n):
                """Calculate factorial using recursion"""
                if n == 0 or n == 1:
                    return 1
                return n * factorial(n - 1)

            print(f"Factorial of {num} is:", factorial(num))

       
        case "4":
           
            if not data:
                print("No data available")
            else:
                threshold = int(input("Enter a threshold value to filter out data above this value: "))
                filter_data = list(filter(lambda x: x >= threshold, data))

                print(f"\nFiltered Data (values >= {threshold}):")
                print(", ".join(map(str, filter_data)))

        case "5":
            if not data:
                print("No data available")
            else:
                print("Choose sorting option:")
                print("1. Ascending")
                print("2. Descending")

                sort_choice = input("Enter your choice: ")

                if sort_choice == "1":
                    data.sort()
                    print("\nSorted Data in Ascending Order:")
                elif sort_choice == "2":
                    data.sort(reverse=True)
                    print("\nSorted Data in Descending Order:")
                else:
                    print("Invalid choice")
                    continue

                print(", ".join(map(str, data)))

       
        case "6":
            if not data:
                print("No data available")
            else:
                minimum = min(data)
                maximum = max(data)
                total_sum = sum(data)
                average = round(total_sum / len(data), 2)

                print("Dataset Statistics:")
                summary(
                    **{
                        "Minimum value": minimum,
                        "Maximum value": maximum,
                        "Sum of all values": total_sum,
                        "Average value": average
                    }
                )

        case "7":
             print(__doc__)
             break

      
        case _:
             print("Invalid choice, please try again.")


