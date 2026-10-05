from Accountant import Function as F

def generate_monthly_financial_summary():
    while True:
        print(f"""
              {"=" * 40}
              Generate Monthly Financial Summary
              
              1. Generate monthly financial summary
              2. Back
              {"=" * 40}
              """)

        choice = input("Enter Choice: ")

        if choice == "1":
            month_list = {}

            try:
                with open("txt/Payment.txt", "r") as file:
                    for line in file:
                        datas = line.strip().split(",")
                        if len(datas) < 6:
                            continue

                        data = datas[5].strip().split("-")
                        year = data[0]
                        month = data[1]

                        name = F.get_month(month)
                        key = f"{year}:{name}"
                        if key not in month_list:
                            month_list[key] = {
                                "Paid": 0,
                                "Unpaid": 0
                            }

                        if datas[4] == "Paid":
                            month_list[key]["Paid"] += float(datas[3])

                        elif datas[4] == "Unpaid":
                            month_list[key]["Unpaid"] += float(datas[3])

                print("\nMonthly Financial Summary")
                print(f"{'Year':<10}{'Month':<15}{'Paid':<15}{'Unpaid':<15}")
                for key in month_list:
                    year, month = key.split(":")

                    print(
                        f"{year:<10}"
                        f"{month:<15}"
                        f"{month_list[key]['Paid']:<15}"
                        f"{month_list[key]['Unpaid']:<15}"
                    )

            except FileNotFoundError:
                print("file is not found.")

        elif choice == "2":
            return
        else:
            print("Wrong Choice") 