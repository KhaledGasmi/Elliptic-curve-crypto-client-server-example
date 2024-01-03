a = 2
p = 17
G = (5, 11)  # Generator point (example)

def point_double(P, a, p):
    if P is None:
        return None  # Point at infinity
    else:
        x, y = P
        s = (3 * x**2 + a) % p
        inv_s = pow(2 * y, -1, p)
        m = (s * inv_s) % p
        x_r = (m**2 - 2 * x) % p
        y_r = (m * (x - x_r) - y) % p
        return (x_r, y_r)

def point_add(P, Q, a, p):
    if P is None:
        return Q
    elif Q is None:
        return P
    else:
        x_p, y_p = P
        x_q, y_q = Q
        if P != Q:
            s = ((y_q - y_p) * pow(x_q - x_p, -1, p)) % p
        else:
            s = ((3 * x_p**2 + a) * pow(2 * y_p, -1, p)) % p
        x_r = (s**2 - x_p - x_q) % p
        y_r = (s * (x_p - x_r) - y_p) % p
        return (x_r, y_r)

def doubleAndAdd(t, P, a, p):
    tBinary = bin(t)[2:]
    result = None
    for i in range(len(tBinary)):
        result = point_double(result, a, p)
        if tBinary[i] == "1":
            result = point_add(result, P, a, p)
        # Reduce result modulo p
        result = (result[0] % p, result[1] % p)
    return result

# Example usage:
t = 26
result = doubleAndAdd(t, G, a, p)
print("Result:", result)
