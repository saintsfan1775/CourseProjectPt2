## John Saraya CIS261 Wk5CourseProjectPart2 Using Lists and Dictionaries to Store and Retrieve Data


def get_name():
    name = input("Enter employee name: ")
    return name
def get_dates_worked():
    fromdate = input("Enter Start Date (mm/dd/yyyy): ")
    todate = input("Enter To Date (mm/dd/yyyy): ")
    return fromdate, todate
def get_hours_worked():
    hours = float(input("Enter total hours worked: "))
    return hours
def get_hourly_rate():
    hourly_rate = float(input("Enter hourly rate: "))
    return hourly_rate
def get_tax_rate():
    tax_rate = float(input("Enter tax rate: "))
    return tax_rate
def calculate_tax_and_netpay(hours, hourly_rate, tax_rate):
    grosspay = hours * hourly_rate
    tax = grosspay * tax_rate
    net_pay = grosspay - tax
    return grosspay, tax, net_pay

def print_info(EmpDetailList):
    total_employees = 0
    total_hours = 0.00
    total_gross_pay = 0.00
    total_tax = 0.00
    total_net_pay = 0.00
    for EmpList in EmpDetailList:
        fromdate = EmpList[0]
        todate = EmpList[1]
        name = EmpList[2]
        hours = EmpList[3]
        hourly_rate = EmpList[4]
        tax_rate = EmpList[5]
        grosspay, tax, net_pay = calculate_tax_and_netpay(hours, hourly_rate, tax_rate)
        print(fromdate, todate, name, f"{hours:,.2f}", f"{grosspay:,.2f}", f"{tax_rate:,.1%}", f"{tax:,.2f}", f"{net_pay:,.2f}")
        total_employees +=1
        total_hours += hours
        total_gross_pay += grosspay
        total_tax += tax
        total_net_pay += net_pay
        EmpTotals["TotEmp"] = total_employees
        EmpTotals["TotHrs"] = total_hours
        EmpTotals["TotGrossPay"] = total_gross_pay
        EmpTotals["TotTax"] = total_tax
        EmpTotals["TotNetPay"] = total_net_pay


def display_total_info(EmpTotals):
    print()
    print(f'Total number of employees: {EmpTotals["TotEmp"]}')
    print(f'Total hours worked: {EmpTotals["TotHrs"]:,.2f}')
    print(f'Total gross pay: {EmpTotals["TotGrossPay"]:,.2f}')
    print(f'Total tax: {EmpTotals["TotTax"]:,.2f}')
    print(f'Total net pay: {EmpTotals["TotNetPay"]:,.2f}')
    

if __name__=="__main__":
    EmpDetailList = []
    EmpTotals = {}
    while True:
        name = get_name()
        if (name.upper() == "END"):
            break
        fromdate, todate = get_dates_worked()
        hours = get_hours_worked()
        hourly_rate = get_hourly_rate()
        tax_rate = get_tax_rate()
        EmpDetail = [fromdate, todate, name, hours, hourly_rate, tax_rate]
        EmpDetailList.append(EmpDetail)

    print_info(EmpDetailList)
    display_total_info(EmpTotals)


    
    
    
    
    
    

    
    
    
  




