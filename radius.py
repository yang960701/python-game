#float　実数
r = float(input("半径の値を入力してください \n"))

area = r**2*3.14
circumference = 2*r*3.14
print(f"円の面　：　{r*r*3.14}")
print(f"円の面　：　{r**2*3.14}")
print(f"円の枠　：　{2*r*3.14}")

print(round(area,2))
print(round(circumference,2))
