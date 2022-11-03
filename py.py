import os

for f in os.listdir():
    if f[0] == 'h':
        #os.system(f'mv {f} {f[:5] + f[5:].zfill(2)}; ls -l')
        if int(f[5:]) % 2 == 0:
            os.system(f'echo {f} is even. >> {f}')
        else:
            os.system(f'echo {f} is odd. >> {f}')
