print("pembayaran dilakukan secara online")
print("1. Transfer Bank BCA")
print("2. GOPAY")
print("3. DANA")
metode_pembayaran = int(input("Masukan pilihan pembayaran (1/2/3): "))
if metode_pembayaran == 1:
    print("Masukan kode pembayaran via BCA")
    pby = input("kode pembayaran BCA : ")
elif metode_pembayaran == 2:
    print("Masukan kode pembayaran via GOPAY")
    input("kode pembayaran GOPAY : ")
elif metode_pembayaran == 3:
    print("Masukan kode pembayaran via DANA")
    input("kode pembayaran DANA : ")

print("Selamat, pembayaran anda telah terkonfirmasi")
os.system('cls')
