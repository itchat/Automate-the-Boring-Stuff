"""
*********
*       *
*       *
*********
"""

def boxPrint(symbol, width, height):
    print(symbol * width)
    if (width < 2) or (height < 2):
        rasie Exception("width and height must be greater or equal to 2.")
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

boxPrint("*", 15, 5)
boxPrint("O", 5, 16)

# 这个 function 在 ** 或者 1,1 的时候会出错, raise function 安排

# 导入 log 方法
import traceback
try:
    raise Exception("This is the error message")
except:
    errorFile = open('error_log.txt', 'a') # append mode
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print("The traceback info was written error_log.txt")

# assertion and assert mode 
market_2nd = {'ns':'green','ew':'red'}

def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] == 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] == 'red'
        elif intersection[key] == 'red':
            intersection[key] == 'green'
    assert 'red' in intersection.values(), "Neither light is red!" + str(intersection)
    # I assert this condtion always hold true, if it's not then "Neither..." should crash
    # assertion are using for programmer errors not for users
print(market_2nd)
switchLights(market_2nd)
print(market_2nd)
