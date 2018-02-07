class Curve(object):
    def __init__(self, a, b, prime, n):
        self.a = a
        self.b = b
        self.prime = prime
        self.n = n

    def print_info():
        print(a,b,prime,n)


def inverse_modulo(a,p):
    #calculates 1/a mod p
    #this function assumes that a and p are relatively prime otherwise this doesn't work
    a = a % p
    q, r = p // a, p % a
    if r == 1:
        return -q % p
    else:
        m = inverse_modulo(r,a)
        n = (r * m - 1) // a
        return (-1 * (m * q + n)) % p

def ec_double(p,curve):
    px,py = p[0],p[1]
    prime = curve.prime
    a,b = curve.a, curve.b
    s = ((3 * px ** 2 + a) * inverse_modulo(2 * py, prime)) % prime
    t = ((-3 * px ** 3 - a * px + 2 * py ** 2) * inverse_modulo(2 * py, prime)) % prime
    x = (s ** 2 - 2 * px) % prime
    y = (-1 * s * x - t) % prime
    return (x,y)

def ec_add(p,q,curve):
    if p == 'inf':
        return q
    elif q == 'inf':
        return p
    else:
        if p == q:
            return ec_double(p,curve)
        elif p[0] == q[0]:
            return 'inf'
        else:
            px,py,qx,qy = p[0],p[1],q[0],q[1]
            a,b,prime = curve.a,curve.b,curve.prime
            x_d = inverse_modulo(qx - px, prime) % prime
            s = ((qy - py) * x_d) % prime
            t = ((py * qx - qy * px) * x_d) % prime
            x = (s ** 2 - px - qx) % prime
            y = (-1 * s * x - t) % prime
            return (x,y)

def ec_mul(p,n,curve):
    n_bin = bin(n).lstrip('0b')
    ans = 'inf'
    tmp = p
    for i,x in enumerate(reversed(n_bin)):
        if x == '1':
            ans = ec_add(ans, tmp, curve)
        else:
            pass
        tmp = ec_double(tmp,curve)
    return ans


'''
if __name__ == '__main__':
    secp256k1 = Curve(0,7,0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F,0)
    g = (0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798,0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8)
    k = 0x1E99423A4ED27608A15A2616A2B0E9E52CED330AC530EDCC32C8FFC6A526AEDD
    K = ec_mul(g,k,secp256k1)
    print(K)
    print(int('F028892BAD7ED57D2FB57BF33081D5CFCF6F9ED3D3D7F159C2E2FFF579DC341A',16))
'''






