import random

num_red = 6
num_blue = 1

range_red = (1, 33)
range_blue = (1, 16)


def doubleColorBall_Description():
    print "The rule of double color ball:"
    print ("%d red ball range in %d to %d, %d blue ball range in %d to %d" % (num_red, range_red[0], range_red[1],
        num_blue, range_blue[0], range_blue[1]))


def randomBall(start, end, number):
    ret = random.sample(range(start, end+1), number)
    return ret


def doubleColorBall(number):
    print "The key to Wealth:"
    for i in range(number):
        # random red ball
        red_answer = randomBall(range_red[0], range_red[1], num_red)
        red_answer.sort()
        blue_answer = randomBall(range_blue[0], range_blue[1], num_blue)
        blue_answer.sort()
        print blue_answer, red_answer
