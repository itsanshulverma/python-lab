
def calc(sales):
    total_sales = 4*sales
    com_amt = 0 #Commission
    if total_sales >= 50000:
        com_amt = total_sales*0.05
    remarks = ""
    if total_sales >= 80000:
        remarks = "Excellent"
    elif total_sales >= 60000:
        remarks = "Good"
    elif total_sales >= 40000:
        remarks = "Average"
    elif total_sales < 40000:
        remarks = "Work Hard"

    return total_sales, com_amt, remarks

if __name__ == "__main__":
    sales = int(input("Enter the sales per week: "))
    t_sales, comm, remarks = calc(sales)

    print("Total Sales: Rs.{:.2f}".format(t_sales))
    print("Commission: Rs.{:.2f}".format(comm))
    print("Remarks: ", remarks)