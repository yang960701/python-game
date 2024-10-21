coffee = """
         {
      {   }
       }_{ __{
    .-{   }   }-.
   (   }     {   )
   |`-.._____..-'|
   |             ;--.
   |            (__  \\
   |             | )  )
   |             |/  /
   |             /  /    -Felix Lee-
   |            (  /
   \\             y'
    `-.._____..-'

"""

menu = """
    coffee
    -menu-
  1:アメリカーノ       180円
  2:カフェラッテ　　　 270円
  3:ホットチョコレート 230円
  
"""

print(coffee)
print(menu)
print("=" * 45)

coffee_price = 0
total_price = 0
change = 0

order = int(input("COFFEEを選択さいてください。番号の入力>>> "))

if order == 1:
    coffee_price = 180
elif order == 2:
    coffee_price = 270
elif order == 3:
    coffee_price = 230

cups = int(input("何枚さしあげましょうか？ >>> "))
total_price = coffee_price * cups

received = int(input(f"総額は　{total_price} です。 お金を入れてください　>> "))
if received >= total_price:
    change = received - total_price
    print(f"{received}円をいただきました。おつりは{change}円です。")

    
else :
    print("お金がたりないです。注文を取り消します。")
    



