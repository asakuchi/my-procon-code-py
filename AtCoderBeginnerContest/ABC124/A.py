A, B = map(int, input().split())

if A == B:
    print(2 * A)
elif A > B:
    print(A + (A - 1))
else:
    print(B + (B - 1))
