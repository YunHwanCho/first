num = int(input())

target = 666
cnt = 0

while True:
    if '666' in str(target):
        cnt += 1
    if cnt == num:
        print(target)
        break
    target+=1