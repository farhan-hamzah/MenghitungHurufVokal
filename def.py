def vokal(var):
    total = 0
    for i in var:
        if i in 'aiueoAIUEO':
            total += 1
    return total

# Meminta input dari pengguna
teks = input("Masukkan sebuah teks: ")
print(f"Jumlah huruf vokal: {vokal(teks)}")
