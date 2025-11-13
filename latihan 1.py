# Latihan List - Modul Praktikum 4
# Nama: [Isikan Namamu]
# Kelas: [Isikan Kelasmu]

# Buat list sebanyak 5 elemen dengan nilai bebas
A = [10, 20, 30, 40, 50]
print("List A awal:", A)

# --- Akses List ---
print("\nAkses List:")
print("Elemen ke-3:", A[2])  # indeks dimulai dari 0
print("Elemen ke-2 sampai ke-4:", A[1:4])
print("Elemen terakhir:", A[-1])

# --- Ubah Elemen List ---
print("\nUbah Elemen List:")
A[3] = 99  # ubah elemen ke-4
print("Ubah elemen ke-4 dengan nilai lain:", A)

A[3:] = [100, 200]  # ubah elemen ke-4 sampai terakhir
print("Ubah elemen ke-4 sampai terakhir:", A)

# --- Tambah Elemen List ---
print("\nTambah Elemen List:")
# Ambil 2 bagian dari list pertama (A) dan jadikan list baru B
B = A[0:2]
print("List B (2 elemen pertama dari A):", B)

# Tambah list B dengan nilai string
B.append("Python")
print("List B setelah ditambah string:", B)

# Tambah list B dengan 3 nilai
B.extend([60, 70, 80])
print("List B setelah ditambah 3 nilai:", B)

# Gabungkan list B dengan list A
C = B + A
print("Gabungan list B dan A:", C)
