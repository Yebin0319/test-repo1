st_sum=""
sum=0
while True:
    num=int(input("정수입력 : "))
    print("202303475 구예빈 컴퓨터공학과")
    if num == 0:
        break
    else:
        sum+=num
        if num!=0:
            st_sum+=str(num)+'+'
        else:
            st_sum+='='+sum
print(st_sum)

