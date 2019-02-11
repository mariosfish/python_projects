def ack(m, n):
    # ans = null
    if m == 0:
        ans = n + 1
    elif n == 0:
        ans = ack(m - 1, 1)
    else:
        ans = ack(m - 1, ack(m, n - 1))
    return ans


def is_prime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True


# for i in range(100):
#     t = ack(2, i)
#     print(f"{t} is:", is_prime(t))

for i in range(5):
    print(ack(i, i))

# print(f"ackerman ({i},{j}) is: {ack(i,j)}")


# num = 2
# for i in range(100):
#     a = ack(2, i)
#     for a in range(a, num):
#         if a % num == 0:
#             print(f"{a}:not prime")
#         else:
#             print(f"{a}: prime")


# ackerman = []
# for i in range(100):
#     ackerman.append(ack(2, i))

# for j in ackerman:
#     if j%
