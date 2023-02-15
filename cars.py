class Car:
   def __init__(car,name,color,year):
      car.name=name
      car.color=color
      car.year=year
   
   
   def myfunc(car):
    print("A " + car.name, "of color " + car.color , "was bought in the year " + car.year)

c1 = Car("BMW","grey","2004")
c2= Car("Renault","white","2007")
c3= Car("Msc","red","2045")
c4=Car("BMB","orange","2056")
c5=Car("Eagle","blue","2024")
c1.myfunc() 
c2.myfunc()
c3.myfunc()
c4.myfunc()
c5.myfunc()   
print("The MSC was the most Fastest and Performing car during the 20th century")
