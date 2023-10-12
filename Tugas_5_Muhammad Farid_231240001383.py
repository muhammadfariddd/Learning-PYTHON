# Inputan Menggunakan Numerik

x = "-"

print ("*************************************************************************")
print ("************** Program Menghitung Total Penjumlahan *********************")
print ("*************************************************************************")

print (" ")
print (" ")

print ("Nilai Akhir Semester Adalah 25%UTS + 25%UAS + 15%Tugas + 20%Kehadiran")

print (" ")

nama        = input("\t Masukkan Nama Mahasiswa             :  ")
nim         = input("\t Masukkan NIM Mahasiswa              :  ")
mata_kuliah = input("\t Masukkan Mata Kuliah                :  ")
nilai_uts   = input("\t Masukkan Nilai UTS                  :  ")
nilai_uas   = input("\t Masukkan Nilai UAS                  :  ")
tugas       = input("\t Masukkan Nilai Tugas                :  ")
keaktifan   = input("\t Masukkan Nilai Keaktifan            :  ")
kehadiran   = input("\t Masukkan Nilai Kehadiran            :  ")
nilai_akhir = 0.25 * float(nilai_uts) + 0.25 * float(nilai_uas) + 0.25 * float(tugas) + 0.25 * float(kehadiran)

print (" ")

 
print ("-------------------------------------------------------------------------")

print (" ")

print ("\t Nilai Akhir Semester")
print ("\t Nama Mahasiswa                      : ",nama)
print ("\t NIM Mahasiswa                       : ",nim)
print ("\t Mata Kuliah                         : ",mata_kuliah)
print ("\t Adalah                              : ",float(nilai_akhir))
print ("\t Nilai Dibulatkan Menjadi            : ",round(nilai_akhir))

print (" ")

print ("-------------------------------------------------------------------------")
 

 
print (" ")
print (" ")

print ("******************** Belajar Lebih Giat Lagi Ya !!! *********************")

