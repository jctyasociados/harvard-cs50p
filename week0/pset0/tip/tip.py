""" Python script to calculate tip given to server in a restaurant """

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

""" Function that converts dollars to floating point with two decimals """
def dollars_to_float(d):
  return float('%.2f' % float(d.strip("$")))

""" Function that converts tip given in percentage to floating point number with two decimals """
def percent_to_float(p):
  tip = float(p.strip("%"))
  return float('%.2f' % (tip / 100))
  

main()
