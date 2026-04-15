from pwn import *

# 1. Serverga ulanish parametrlarini kiriting
HOST = '154.57.164.67'  # HTB bergan IP
PORT = 32054              # HTB bergan Port

try:
    # Serverga ulanamiz
    r = remote(HOST, PORT)

    # Odatda boshida biron bir matn chiqadi (masalan, "Ready? Press Enter")
    # r.recvuntil(b"Enter")
    # r.sendline(b"")

    while True:
        # 2. Savolni qabul qilish
        # 'recvline' yoki 'recvuntil' orqali savol turgan qatorni ushlaymiz
        line = r.recvline().decode().strip()
        print(f"Serverdan keldi: {line}")

        # Agar "flag" so'zi ko'rinsa, siklni to'xtatamiz
        if "HTB{" in line:
            print(f"TABRIKLAYMAN! Flag: {line}")
            break

        # 3. Logika (Matematika yoki Matnni qayta ishlash)
        # Misol: Server "5 + 10 = ?" ko'rinishida savol bersa:
        try:
            # Faqat misol qismini ajratib olamiz
            # Bu joyni challange turiga qarab o'zgartirasiz
            if "=" in line:
                problem = line.split('=')[0]
                result = eval(problem) # Matematik amalni bajarish
                
                # 4. Javobni yuborish
                r.sendline(str(result).encode())
                print(f"Yuborilgan javob: {result}")
        except:
            continue

except EOFError:
    print("Server ulanishni uzdi.")
