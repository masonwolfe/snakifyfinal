H = int(input())
M = int(input())
S = int(input())
T = ((60 * M)+(3600 * H) + S)
F = T / 43200
print(F * 360)
