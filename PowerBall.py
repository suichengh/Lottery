import random

num_white = 5
num_red = 1

range_white = (1, 69)
range_red = (1, 26)


def powerBall_Description():
    print "The rule of power ball:"
    print ("Select %d number from %d to %d for the red Powerball" % (num_red, range_red[0], range_red[1]))
    print ("then select %d numbers from %d to %d for the white balls" %(num_white, range_white[0], range_white[1]))

def randomBall(start, end, number):
    ret = random.sample(range(start, end+1), number)
    return ret


def powerBall(number):
    print "The key to Wealth:"
    for i in range(number):
        # random red ball
        red_answer = randomBall(range_red[0], range_red[1], num_red)
        red_answer.sort()
        white_answer = randomBall(range_white[0], range_white[1], num_white)
        white_answer.sort()
        print white_answer, red_answer