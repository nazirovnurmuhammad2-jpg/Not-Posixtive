from pwn import *
import os

# Server ma'lumotlarini o'zgartiring
HOST = '154.57.164.67'  # HTB bergan IP
PORT = 32054              # HTB bergan Port

def solve():
    try:
        r = remote(HOST, PORT)
        
        while True:
            line = r.recvline().decode().strip()
            if not line: continue
            
            print(f"Serverdan keldi: {line}")

            if "HTB{" in line:
                print(f"TABRIKLAYMAN! Flag: {line}")
                return

            if "=" in line:
                # Misol: "5 + 10 = ?" -> problem = "5 + 10"
                problem = line.split('=')[0].strip()
                # Xavfsizroq hisoblash uchun eval ishlatamiz
                result = eval(problem)
                
                r.sendline(str(result).encode())
                print(f"Yuborilgan javob: {result}")
                
    except EOFError:
        print("Server ulanishni uzdi.")
    except Exception as e:
        print(f"Xato yuz berdi: {e}")

if __name__ == "__main__":
    solve()
