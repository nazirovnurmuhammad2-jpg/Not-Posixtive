from pwn import *
import re

# --- SOZLAMALAR ---
HOST = '154.57.164.67'  # HTB bergan IP manzilni bura yozing
PORT = 32054         # HTB bergan Portni bura yozing
# ------------------

def solve():
    try:
        # Serverga ulanish
        io = remote(HOST, PORT)
        print(f"[+] Serverga ulandi: {HOST}:{PORT}")

        while True:
            # Serverdan kelgan ma'lumotni o'qish
            try:
                data = io.recvline().decode().strip()
            except EOFError:
                print("[!] Server ulanishni uzdi (Ehtimol flag yuborildi).")
                break

            if not data:
                continue

            print(f"[*] Kelgan matn: {data}")

            # 1. Flagni tekshirish
            if "HTB{" in data:
                print(f"\n[!!!] FLAG TOPILDI: {data}\n")
                break

            # 2. Matematik amalni qidirish (RegEx orqali)
            # Bu qator: raqam + belgi + raqam formatini qidiradi
            match = re.search(r'(\d+[\s\+\-\*\/]+\d+)', data)
            
            if match:
                expression = match.group(1)
                try:
                    # Misolni hisoblash
                    result = eval(expression)
                    # Javobni yuborish
                    io.sendline(str(result).encode())
                    print(f"[>] Yuborilgan javob: {result}")
                except Exception as e:
                    print(f"[X] Hisoblashda xato: {e}")
            
    except Exception as e:
        print(f"[X] Ulanishda xato: {e}")
    finally:
        # Oxirida terminalni ochiq qoldirish (agar flag kelsa ko'rish uchun)
        try:
            io.interactive()
        except:
            pass

if __name__ == "__main__":
    solve()
