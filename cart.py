tup=[]
d=0
no=int(input("enter no of item:"))
for i in range(no):
   print("items:",i+1)
   name=input("enter item name")
   q=int(input("enter quantity"))
   p=int(input("enter price"))
   t=(name,q,p)
   tup.append(t)
print("item details")
for t in tup:
   print(t)
for e in tup:
   d+=e[1]*e[2]
   st=d
print("subtotal:",st)
gst_rate=0.05
gst_amount=gst_rate*st
total_amount=st+gst_amount
print("the total amount for all product:",total_amount)
dr=0.10
m=3000
if total_amount>m:
   da=total_amount*dr
   ta=total_amount-da
   print("after discount",ta)
else:
   print("no discount")
print(" BILL DETAILS")
discount=ta
for t in tup:
   print(t)
print("subtotal",st)
print("gst",gst_amount)
print("discount",ta)
print("totalamount",total_amount)
