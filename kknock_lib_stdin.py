#reader가 stdin으로만 입력함을 이용한 방법
import datetime
import pandas as pd

data = pd.read_csv("./kknock_books.csv")
if data[0][1] is None:
    print("y")
else:
    print('n')

while 1:
    print('================================')
    print('K.Knock Library rent System v0.1')
    print('================================')
    print('대여 : <도서 태그를 찍어주세요 > ')

    id = input()[:10]
    

    print(data[0][2],': ',)

    print("이름 : ",end='')
    name = input()[:10]

    d = str(datetime.datetime.now())[:10]
    print('대여일: ',d)

    print('대여 완료')



