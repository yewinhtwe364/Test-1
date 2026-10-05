def generate_maintenance_summary_report():
    while True:
        print(f"""
              {"=" * 40}
              Generate Maintenance Summary Report
              
              1. generate mainntenance summary report
              2. back
              """)
        choice = input("Enter Choice: ")
        summary = {}
        if choice == "1":
            try:
                with open("txt/MaintenanceRecord.txt", "r") as file:
                    for line in file:
                        data = line.strip().split(",")
                        if len(data) < 5:
                            print(f"Incomplete Data: {data}")
                            continue
                        if data[2] in summary:
                            summary[data[2]] += 1
                        else:
                            summary[data[2]] = 1
                        if data[4] in summary:
                            summary[data[4]] += 1
                        else:
                            summary[data[4]] = 1
                    print("""\nMaintenance Summary Report""")
                    print("=" * 40)

                    for key in summary:
                        print(f"{key:<15}: {summary[key]}")
                        
            except FileNotFoundError:
                print("File is not found!")               
        elif choice == "2":
            return
        else:
            print("Wrong choice")           
                            
                            
                            
                            
                            
                            
                            
                            