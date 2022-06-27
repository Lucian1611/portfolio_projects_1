import string


def generator_parola(a, b, c, d):
    contor = 0
    for i in a:
        for j in b:
            for k in c:
                for l in d:
                    print(i, j, k, l)
                    contor += 1
    print(contor)

a1 = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)
b1 = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)
c1 = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)
d1 = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)

generator_parola(a1, b1, c1, d1)
# SAU

# def generator_parola(a):
#     for i in a:
#         for j in a:
#             for k in a:
#                 for l in a:
#                     print(i, j, k, l)
#
# a1 = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)
#
# generator_parola(a1)
