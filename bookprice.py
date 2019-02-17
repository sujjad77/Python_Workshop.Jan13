cover_price=240
discount=(40/100)*240
cost_price=cover_price-discount
shipping_cost1=25
shipping_cost2=15
cp1=(20*shipping_cost1)+cost_price*20
cp2=(40*shipping_cost2)+cost_price*20
total_price=cp1+cp2
print("The wholesale price for 60 books is Rs.{}".format(total_price))

