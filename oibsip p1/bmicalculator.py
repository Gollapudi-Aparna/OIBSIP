def bmi(w, h):
  print("\n weigth=",w,"(pounds)")
  print("\n height=",h,"(inches)")
  w=w*703
  h=h*h
  bmi=w/h
  print("\n bmi=",bmi,"\n")
  if(bmi<=18.5):
    print("under weight ,health risk: minimal")
  elif(bmi>18.5 and bmi<=24.9):
    print("normal weight,health risk: minimal")
  elif(bmi>24.9 and bmi<=29.9):
    print("over weight,health risk: increased")
  elif(bmi>29.9 and bmi<=34.9):
    print("obese,health risk: high")
  elif(bmi>34.9 and bmi<=39.9):
    print("severly obese,health risk: very high")
  elif(bmi>39.9):
    print("morbidly obese,health risk: extremly high")
n=int(input("choose 1-kg,2-pounds"))
k=0.0
if(n==1):
  k=float(input("enter weight in kgs"))
  k=k*2.2
elif(n==2):
  k=float(input("enter weight in pounds"))
11
n=int(input("choose 1-cm,2-inches"))
h=0.0
if(n==1):
  h=float(input("enter weight in cm"))
  h=h/2.54
elif(n==2):
  h=float(input("enter weight in inches"))
bmi(k,h)
