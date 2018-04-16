# https://codejam.withgoogle.com/2018/challenges/00000000000000cb/dashboard/0000000000007a30

import sys
import math
import random
import logging

logger = logging.getLogger('go_gopher')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('log', mode='w')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
logger.debug('===== GO GOPHER STARTED ====')

def log_pool(logger, pool):
    for row in pool:
        logger.debug(row)

def deploy(a):
    pool = [[0] * 3 for _ in range(3)]
    log_pool(logger, pool)
    num_undeployed = 9
    j_offset = 0
    i_desired, j_desired = 2, 2 + j_offset
    print(i_desired, j_desired, flush=True)
    for num_exchange in range(0, 1000 + 1):
        i_deployed, j_deployed = map(int, input().strip().split())
        logger.debug('Exchange {0}: {1} {2}'.format(num_exchange, i_deployed, j_deployed))
        if i_deployed == -1 and j_deployed == -1:
            return False
        if i_deployed == 0 and j_deployed == 0:
            return True
        i_pool, j_pool = i_deployed - 1, j_deployed - j_offset - 1
        if not pool[i_pool][j_pool]:
            logger.debug('  Deploy at {0} {1}'.format(i_deployed, j_deployed))
            pool[i_pool][j_pool] = 1
            num_undeployed -= 1
            a -= 1
            logger.debug('  Remain in pool: {0}'.format(num_undeployed))
            logger.debug('  Remain: {0}'.format(a))
        if not num_undeployed:
            new = min(int((a - 1) / 3 + 1), 3)
            pool_new = [row[new:] + [0] * new for row in pool]
            pool, num_undeployed = pool_new, 3 * new
            j_offset += new
            j_desired += new
            log_pool(logger, pool)
        print(i_desired, j_desired, flush=True)

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a = int(input())
        if not deploy(a):
            exit(1)
