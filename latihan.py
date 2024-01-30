identitas = ["Anggraini", 19, " Indonesia"]
prodi_1 = ["Informatika",10]
prodi_2 = ["Sistem Informatika",11]
dosen_1 = [10, "Mr.Mursalim"]
dosen_2 = [11, "Mr.Hanif"]

print("Cetak semua data... ") 
print ("=====================================================")
print ("Nama : %s, Usia: %d, Negara : %s"%(identitas[0],identitas[1],identitas[2]))
print ("=====================================================")
print ("\nCetak program studi... ")
print ("=====================================================")
print ("Program Studi 1:\nNama Prodi Pertama: %s, ID: %d\nProgram Studi Kedua:\nNama Prodi Kedua: %s, ID: %s"%(prodi_1[0],prodi_1[1],prodi_2[0],prodi_2[1]))
print ("=====================================================")
print ("\nDosen Pengampu... ")
print ("=====================================================")
print ("Dosen Informatika       : %s, Id: %d"%(dosen_1[1],dosen_1[0]))
print ("Dosen Sistem Informatika: %s, Id: %d"%(dosen_2[1],dosen_2[0]))
print (type(identitas),type(prodi_1),type(prodi_2),type(dosen_1),type(dosen_2))
