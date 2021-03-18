#Soal 1

list = ['Alam', 'Iffa', 'Nana', 'Ojat', 'Issa', 'Hani', 'Titus', 'Nadya', 'Faqih', 'Ilham']
print("List Teman: ", list)

print("Nama pada indeks 4: ", list[4])
print("Nama pada indeks 6: ", list[6])
print("Nama pada indeks 7: ", list[7])

list[3] = 'Aji'
list[5] = 'Firnas'
list[9] = 'Tazkiya'
print("List teman baru yang diganti: ", list)

list.append('Hafizh')
list.append('Tito')
print("Tambahan teman pada list: ", list)

for teman in list :
    print("Teman: ", teman)

print("Jumlah daftar nama teman: ", len(list))