import re
import warnings
warnings.filterwarnings('ignore')

ip = '45-54-36-27-X-63-X-18-90-72'

def total_score(ip):
    if not ip:
        return 0
    return score(parse_ip(ip))

def parse_ip(ip):
    throws = []
    for frame in ip.split('-'):
        if frame[0] == 'X':
            throws.append(10)
            if len(frame) == 2:
                if frame[1] == 'X':
                    throws.append(10)
                else:
                    throws.append(int(frame[1]))
        elif frame.endswith('/'):
            throws.extend([int(frame[0]), 10 - int(frame[0])])
        else:
            throws.extend(map(int, frame))
    return throws

def score(throws, frame=1, total=0):
    if frame > 10 or not throws:
        return total
    elif throws[0] == 10:
        bonus = 0
        if len(throws) >= 3:
            bonus = sum(throws[1:3])
        elif len(throws) > 1:
            bonus = throws[1]
        return score(throws[1:], frame + 1, total + 10 + bonus)
    elif sum(throws[0:2]) == 10:
        bonus = 0
        if len(throws) >= 3:
            bonus = throws[2]
        return score(throws[2:], frame + 1, total + 10 + bonus)
    else:
        total += sum(throws[0:2])
        return score(throws[2:], frame + 1, total)

if __name__ == "__main__":
    print("Total Score is : {}".format(total_score(ip)))
