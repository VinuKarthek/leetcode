from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


def get_fy_months(fiscal_year:str, first_month:str = 'OCT'):

    fiscal_year = fiscal_year.replace('FY','').strip()
    start_year = fiscal_year[:2]
    end_year = fiscal_year[2:]

    start_month = datetime.strptime(f"{first_month}{start_year}", "%b%y")
    end_month = start_month + relativedelta(months=11)

    fy_months_list = []
    current_month = start_month

    while current_month <= end_month:
        month_name = current_month.strftime('%b%y').upper()
        fy_months_list.append(month_name)
        current_month = current_month + timedelta(days=32)
        current_month = current_month.replace(day=1)

    return(fy_months_list)

def get_trailing_months(given_month: str, n: int =12):
    # Convert the given_month string to a datetime object
    given_date = datetime.strptime(given_month, "%b%y")

    # Initialize an empty list to store the trailing months
    trailing_months = []

    # Add the given month to the list
    trailing_months.append(given_date.strftime("%b%y").upper())

    # Calculate and add the rest of the trailing months
    for i in range(n-1):
        # Subtract one month from the current date
        trailing_date = given_date + relativedelta(months=i)
        trailing_months.append(trailing_date.strftime("%b%y").upper())

    return trailing_months

# Example usage:
given_month = "JAN23"
trailing_months_list = get_trailing_months(given_month)
print(trailing_months_list)

print(get_fy_months('FY2324'))


common_items = [item for item in get_trailing_months(given_month) if item in get_fy_months('FY2324')]

print(common_items)