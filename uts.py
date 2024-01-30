# Definisi data jabatan dan divisi
divisi = {
    10: "Pengembangan Sumber Daya Manusia",
    20: "Teknologi Informasi",
    30: "Pemasaran",
    40: "Produksi"
}

jabatan = {
    240: {"nama": "Kepala Divisi", "gaji_pokok": 5000000},
    110: {"nama": "Kepala Sub Devisi", "gaji_pokok": 3000000},
    100: {"nama": "Karyawan", "gaji_pokok": 2500000}
}

while True:
    # Input manual data karyawan
    nik = input("\nMasukan NIK karyawan (9 digit angka): ")
    
    kode_divisi = int(nik[0:2])
    kode_jabatan = int(nik[2:5])
    nama_lengkap = input("Nama Lengkap: ")
    
    # Validasi Jenis Kelamin (case-insensitive)
    jenis_kelamin = input("Jenis Kelamin (L/P): ")
    while jenis_kelamin.upper() not in ('L', 'P'):
        print("Jenis Kelamin harus diisi dengan 'L' atau 'P'.")
        jenis_kelamin = input("Jenis Kelamin (L/P): ")
    
    alamat = input("Alamat Lengkap: ")

    # Menghitung gaji bersih
    nama_divisi = divisi[kode_divisi] if kode_divisi in divisi else "Divisi Tidak Diketahui"
    jabatan_karyawan = jabatan[kode_jabatan] if kode_jabatan in jabatan else {"nama": "Jabatan Tidak Diketahui", "gaji_pokok": 0}

    gaji_pokok = jabatan_karyawan["gaji_pokok"]
    tunjangan_profesi = 4000000
    pajak_penghasilan = 5/100 * gaji_pokok
    potongan_bpjs_kesehatan = 4/100 * tunjangan_profesi
    potongan_bpjs_tenaga_kerja = 3/100* tunjangan_profesi

    gaji_bersih = (gaji_pokok + tunjangan_profesi) - (pajak_penghasilan + potongan_bpjs_kesehatan + potongan_bpjs_tenaga_kerja)

    # Menampilkan output sesuai format yang diinginkan
    print("\nOutput:")
    print("===================================================================")
    print("-------------------Jumlah gaji karyawan PT.UNISS-------------------")
    print("===================================================================")
    print("NIK                        :" ,nik)
    print("Nama Karyawan              :" ,nama_lengkap)
    print("Jenis Kelamin              :" ,jenis_kelamin)
    print("Alamat Lengkap             :" ,alamat)
    print("Nama Divisi                :" ,nama_divisi)
    print("Nama Jabatan               :" ,jabatan_karyawan['nama'])
    print("Gaji Pokok                 :" ,gaji_pokok)
    print("Tunjangan Profesi          :" ,tunjangan_profesi)
    print("-------------------Terdapat potongan gaji-------------------------")
    print("1. PPH                     :" ,pajak_penghasilan)
    print("2. Pot. BPJS Kesehatan     :" ,potongan_bpjs_kesehatan)
    print("3. Pot. BPJS Tenaga Kerja  :" ,potongan_bpjs_tenaga_kerja)
    print("Gaji Bersih                :" ,gaji_bersih)
    print("===================================================================")
