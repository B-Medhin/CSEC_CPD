item = input()
val1=ord('a')
rotate=0
for i in item:
    rotate+=min(abs(val1-ord(i)),26-(abs(val1-ord(i))))
    val1=ord(i)
print(rotate)
