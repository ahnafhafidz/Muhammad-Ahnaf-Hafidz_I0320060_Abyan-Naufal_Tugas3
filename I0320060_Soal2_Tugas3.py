#Soal 2

dict = {'Nama':'Muhammad Ahnaf Hafidz','Hobi':'Mendaki gunung dan Futsal', 'Sosial media':'Line : ahnaf_hafidz, Instagram : @ahnaf.hafidz',
        'Lagu favorit':'Astronaut In The Ocean-Masked Wolf, Desember-ERK', 'Makanan favorit' : 'Mie Ayam dan Steak'}

print("dict['Nama']: ", dict['Nama'])
print("dict['Hobi']: ", dict['Hobi'])
print("dict['Sosial media']: ", dict['Sosial media'])
print("dict['Lagu favorit']: ", dict['Lagu favorit'])
print("dict['Makanan favorit']: ", dict['Makanan favorit'])
print("dict", dict)

#mengubah nilai dict

dict['Hobi'] = 'Mendaki gunung dan Bermain game'
dict['Sosial media'] = 'Line : ahnaf_hafidz dan WA : 081391504200'

print("dict['Hobi'] yang sudah diubah: ", dict['Hobi'])
print("dict['Sosial media'] yang sudah diubah: ", dict['Sosial media'])
print("dict yang sudah diubah: ", dict)

#menghapus elemen dict

del dict['Makanan favorit']
print("dict setelah dihapus: ", dict)

#menambahkan item dict

dict.update({'Hobi':'Mendaki gunung, Bermain game, dan Bermain basket'})
print("dict setelah ditambah: ", dict)
