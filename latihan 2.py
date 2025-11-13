# Program: Input Data Nilai Mahasiswa
# Nama: [Isikan Namamu]
# Kelas: [Isikan Kelasmu]

# List untuk menyimpan data mahasiswa
data_mahasiswa = []

while True:
    print("\nMasukkan Data Mahasiswa")
    nama = input("Nama Mahasiswa: ")
    tugas = float(input("Nilai Tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))

    # Hitung nilai akhir
    nilai_akhir = (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

    # Simpan ke list (pakai tuple atau dictionary)
    data_mahasiswa.append({
        'Nama': nama,
        'Tugas': tugas,
        'UTS': uts,
        'UAS': uas,
        'Nilai Akhir': nilai_akhir
    })

    # Tanya apakah mau menambah data lagi
    tambah = input("Tambah data lagi? (y/t): ").lower()
    if tambah == 't':
        break

# Tampilkan hasil
print("\nDaftar Nilai Mahasiswa")
print("="*60)
print(f"{'Nama':20} {'Tugas':>7} {'UTS':>7} {'UAS':>7} {'Akhir':>10}")
print("-"*60)
for mhs in data_mahasiswa:
    print(f"{mhs['Nama']:20} {mhs['Tugas']:7.2f} {mhs['UTS']:7.2f} {mhs['UAS']:7.2f} {mhs['Nilai Akhir']:10.2f}")
print("="*60)
