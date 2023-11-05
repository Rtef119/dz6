def divider(a, b):
   try:
       return a / b

   except ZeroDivisionError:
       print("Nemozna dilutu na 0!")
       return 0

   except TypeError:
       print("Dilutu ne huslovi znakena nemozna!")
       return 0

   except ValueError:
       print("Dilutu ne huslovi znakena nemozna!")
       return 0

"Ctertu "#" ckob pobazutu rezyttat:"
#data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}
#Dilutu ne huslovi znakena nemozna Nemozna dilutu na 0! [5.0, 0.4, 0, 0, 2.0]
"abo"
#data = {10: 2, 2: 5, 123: 4, 18: 0, 8: 4}
#Nemozna dilutu na 0! [5.0, 0.4, 30.75, 0, 2.0]
"abo"
#data = {10: 2, 2: 5, 123: 4, 18: 4}
#[5.0, 0.4, 30.75, 4.5]
"vse"

result = []
for key in data:
   res = divider(key, data[key])
   result.append(res)

print(result)