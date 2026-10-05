from Maintenance import AddNewEquipment as ANE
from Maintenance import ViewEquipment as VE
from Maintenance import UpdateEquipmentMaintenanceStatus as UE
from Maintenance import LogMaintenanceRecord as LMR
from Maintenance import GenerateMaintenanceSummaryReport as GMSR
def maintenance_main_menu():
    while True:
        print(f"""
              {"=" * 40}
              Maintenance Main Menu
              
              1. Add New Equipment
              2. View Equipment
              3. Update Equipment Maintenance Status
              4. Log Maintenance Record
              5. Generate Maintenance Summary
              6. Back
              {"=" * 40}
              """)
        choice = input("Enter Choice: ")
        if choice == "1":
            ANE.add_new_equipment()
        elif choice == "2":
            VE.view_equipment()
        elif choice == "3":
            UE.update_equipment_maintenance_status()
        elif choice == "4":
            LMR.log_maintenance_record()
        elif choice == "5":
            GMSR.generate_maintenance_summary_report()
        elif choice == "6":
            return
        else:
            print("Wrong Choice!")
        