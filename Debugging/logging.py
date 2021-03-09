import logging
logging.basicConfig(filename='error.txt', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)  # 临时关闭 log 功能，禁止 Critical 以及以下的功能

# logging 的初始化, 可以记录 function 每一步的步骤
logging.DEBUG('Start of program')


def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(1, n+1):  # range 从 0 开始
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))
        # 这里的 debug 可以换成五个级别的任何一个

    logging.debug('Return value is %s' % (total))
    return total


print(factorial(5))
logging.debug("End of program")

''' 
Five levels
debug
info
warning 
error
critical(highest)
```


