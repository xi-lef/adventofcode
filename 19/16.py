import sys

init = [int(v) for v in sys.stdin.readline().strip()]
offset = int(''.join(str(v) for v in init[:7]))
pattern = [0, 1, 0, -1]

def fft(signal):
    n = len(signal)
    for x in range(100):
        #print(x)
        #print(''.join(str(x) for x in signal))
        new = []
        for i in range(n):
            #s = sum(v * pattern[(j + 1) // (i + 1) % 4] for j, v in enumerate(signal))
            s = 0
            f = 1
            for j in range(i, n, 2 * (i + 1)):
                s += sum(f * v for v in signal[j:j + i + 1])
                f *= -1
            new.append(abs(s) % 10)
        signal = new
    return ''.join(str(v) for v in signal)

print(fft(init)[:8])
print(fft(10000 * init)[offset : offset + 8])
