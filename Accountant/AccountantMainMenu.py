from Accountant import RecordPayment as RP
from Accountant import UpdatePayment as UP
from Accountant import ViewPaymentRecord as VP
from Accountant import UpdateMembership as UM
from Accountant import Membership as MS
from Accountant import GenerateIncomeSummary as GS
from Accountant import GenerateOutstandingList as GL
from Accountant import GenerateMonthlyFinancialSummary as GMS
def accountant_main_menu():
    while True:
        print(f"""
              {"=" * 40}
              Accountant Main Menu
              
              1. Record Payment
              2. Update Payment
              3. View Payment Record
              4. Update Membership Plan
              5. Membership Registration
              6. Generate Income Summary
              7. Generate Outstanding List
              8. Generate Monthly Financial Summary
              9. Back
              {"=" * 40}
              """)
        choice = input("Enter Choice: ")
        if choice == "1":
            RP.record_payment()
        elif choice == "2":
            UP.update_payment()
        elif choice == "3":
            VP.view_payment_record()
        elif choice == "4":
            UM.update_membershipplan()
        elif choice == "5":
            MS.membership()
        elif choice == "6":
            GS.generate_income_summary()
        elif choice == "7":
            GL.generate_outstanding_list()
        elif choice == "8":
            GMS.generate_monthly_financial_summary()
        elif choice == "9":
            return
        else:
            print("Wrong Choice!")
            