#数字を分離する。
a,b = input("掛け算する数字を入力してください。 ex)10 4\n").split()
print(int(a) * int(b))

#escape sequence
# \n 行の変更
# \t tap
# \\ \の出力

print(f"掛け算の結果は{int(a) * int(b)}")
print(f"{a} * {b} = {int(a) * int(b)}")
