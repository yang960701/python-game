# 変数の作成方法
#name = input("名前を入力してください。")
#print( name + "様、ようこう")


print("リンゴ、1個 : 50円")

#文字を数字に変更
count = int(input("必要なリンゴの数?"))

print("総額は", 50*count,"円です。")

#f-string Python 3.6以来
print(f"総額は {50*count} 円です。")
