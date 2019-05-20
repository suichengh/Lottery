import DoubleColorBall
import PowerBall

LotteryType = {
    'DoubleColorBall' : 1,
    'PowerBall' : 2,
}

print("Do you want to be rich?")

while True:
    ret = input("1 - Yes, 2 - No \n")
    if ret == 2:
        print "Have a nice day!"
        exit()
    elif ret == 1:
        break
    else:
        print "Are you Sure?"

print "choose the type of lottery"
print LotteryType
ret = input()

if ret == LotteryType['DoubleColorBall']:
    DoubleColorBall.doubleColorBall_Description()
    number = input("How many tickets do you need:")
    DoubleColorBall.doubleColorBall(number)
elif ret == LotteryType['PowerBall']:
    PowerBall.powerBall_Description()
    number = input("How many tickets do you need:")
    PowerBall.powerBall(number)
else:
    print "Do not supported"

raw_input("Press enter to exit.")