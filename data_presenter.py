data = ('../CupcakeInvoices.csv')

for row in data:
    print(row)
    

for row in data:
  values = row.split(',')
  print(values[2])

  
  
  
  
total = 0

for row in data:
    values = row.split(',')
    total = total + (int(values[3]) * float(values[4]))
    
print(total)
  
data.close()
