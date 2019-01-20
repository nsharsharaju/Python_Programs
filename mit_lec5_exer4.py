L1 = ["bacon","eggs"]
L2 = ["toast","jam"]
brunch = L1
L1.append("juice")
brunch.extend(L2)

print(L1)
print(brunch)