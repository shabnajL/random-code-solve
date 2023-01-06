# problemset-link : https://www.codingame.com/training/easy/horse-racing-duals
import sys
import math

n = int(input())
pi = []
for i in range(n):
    x = int(input())
    pi.append(x)
#print(pi)
pi.sort()
#print(pi)
mn = sys.maxsize
for i in range(1,n):
    answer = pi[i] - pi[i-1]
    mn = min(mn, answer)

print(mn)
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
pi.clear()

