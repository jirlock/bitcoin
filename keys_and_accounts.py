import elliptic_curve as ec

def create_pub_key(sec_key):
    #calculate k * G
    bin_sec_key = bin(sec_key).lstrip('0b')
    secp256k1 = ec.Curve(0,7,0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F,0)
    g = (0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8)
    K = ec.ec_mul(g,sec_key,secp256k1)
    return K


if __name__ == '__main__':
    print(create_pub_key(0x1E99423A4ED27608A15A2616A2B0E9E52CED330AC530EDCC32C8FFC6A526AEDD))
        


