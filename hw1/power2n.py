# 方法 d：用遞迴+查表

pow=[None]*10000
pow[0]=1

def power2n_d(n):
    if not pow[n] is None:
        return pow[n]
    pow[n]=power2n_d(n-1)+power2n_d(n-1)
    return pow[n]

print('power2n_d(40)=', power2n_d(40))