s1 = input("sentence 1 : ")
s2 = input("sentence 2 : ")

s1Set = set(s1)
s2Set = set(s2)

print("similar=%s"  % "".join(s1Set.intersection(s2Set)))
print("difference=%s" % "".join(s1Set.difference(s2Set)))

