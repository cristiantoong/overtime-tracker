# Ot Tracker
import csv

class OTData:
  def __init__(self, year, month, date, overtime):
    self.year = year
    self.month = month
    self.date = date
    self.overtime = overtime

class OTTracker:
  def __init__(self):
    self.ot_lists = []
    self.ot_total = []

  def __str__(self):
    return f"{self.date} : {self.overtime}"

  def add_overtime(self, overtime):
    self.ot_lists.append(overtime.__dict__)

  def display_overtime(self):
    print(self.ot_lists[0]['year'] + '\t|\t' + self.ot_lists[0]['month'])
    print('Date  | Overtime')

    for ot in self.ot_lists:
      print(f"{ot['date']} | {ot['overtime']}")
    return ''


  def sum_of_overtime(self):
    sum = 0
    for i in self.ot_lists:
      sum = sum + i['overtime']
    return sum

  def calc_ot_amount(self):
    amt_per_hr = 120
    sum = 0
    total_ot_amt = 0
    for i in self.ot_lists:
      sum = sum + i['overtime']
      total_ot_amt = amt_per_hr * sum
    return total_ot_amt

  def save(self):
    with open('overtime_tracker.csv', 'w') as f:
      fieldnames = ['year', 'month', 'date', 'overtime']
      writer = csv.DictWriter(f, fieldnames=fieldnames)
      writer.writeheader()
      for ot in self.ot_lists:
        writer.writerow(ot)


ot_tracker = OTTracker()

# MAIN
def add_ot(year, month, date, overtime):
  ot_data = OTData(year, month, date, overtime)
  ot_tracker.add_overtime(ot_data)

def save_ot_total_amt():
  ot_tracker.save()
  with open('overtime_summary', 'w') as f:
    f.write(f"Total Overtime: {ot_tracker.sum_of_overtime()} \n")
    f.write(f"Total Overtime Amount: {ot_tracker.calc_ot_amount()}")

def display_ot_info():
  ot_tracker.display_overtime()
  print(f"Total Overtime: {ot_tracker.sum_of_overtime()}")


def menu():
  choice = input("""
  1.) r - Add overtime
  2.) d - display overtime
  3.) s - save data
  4.) c - Total hours amount
  5.) q - quit
  """)
  while choice != 'q':
    if choice == 'r':
      year = input('Enter year: ')
      month = input('Enter month: ')
      date = input('Enter date: ')
      overtime = int(input('Enter overtime: '))
      add_ot(year, month, date, overtime)

    elif choice == 'd':
      display_ot_info()
    elif choice == 's':
      #ot_tracker.save()
      save_ot_total_amt()
    elif choice == 'c':
      print(ot_tracker.calc_ot_amount())
    elif choice == 'q':
      break
    choice = input("""
  1.) r - Add overtime
  2.) d - display overtime
  3.) s - save data
  4.) c - Total hours amount
  5.) q - quit
  """)

menu()
