# i % 12 == 0
for i in range(1,101):
  if i % 4  == 0: 
    if i % 3  == 0: 
      print(i)

#Students Average
students = ["Alper", "Osman", "Fulya"]
Notes = [ 75, 80, 70]
Total_notes = sum(Notes)
Total_students = len(Notes)
Average = Total_notes / Total_students 
 
print("Notes:", Notes)
print("Average Class Notes:", Average)

#Odd Number Even Number
for i in range(1,1001):
 if i % 2 == 0: 
  print(i, "Even Number")
 else: 
  print(i, "Odd Number")



