print(" data diri mahasiswa");

nama   =input("Masukan NAMA          : ");
nim    =input("Masukan nim           : ");
prodi  =input("Masukan Prodi         : ");
alamat =input("Masukan alamat        : ");
print("==============================================")
print("nama     : ",nama);
print("nim      : ",nim);
print("prodi    : ",prodi);
print("alamat   : ",alamat);
print("==============================================")
print("Program Menghitung Luas Lingkaran dan Keliling Lingkaran :")
r = int(input("Masukkan Jari - Jari = "))

phi     = 22/7
luas    = phi*r*r
kel     = 2*phi*r

print(("Luas Lingkaran Adalah                       = ", luas));
print(("Keliling Lingkaran Adalah                   = ", kel));
print("================================================")
print("program menghitung luas dan keliling Trapesium")

a =int(input("Masukan Alasnya                       = "))
c =int(input("Masukan Sisi yang sejajar Dengan Alas = "))
t =int(input("Masukan Tingginya                     = "))
sa=int(input("Masukan Sisi 1                        = "))
sb=int(input("Masukan sisi 2                        = "))
sc=int(input("Masukan sisi 3                        = "))
sd=int(input("Masukan sisi 4                        = "))

luas =1/2* (a+c)*t
kel  =sa+sb+sc+sd

print("Luas Trapesium Adalah                        =", luas)
print("Keliling Trapesium Adalah                    =", kel)
