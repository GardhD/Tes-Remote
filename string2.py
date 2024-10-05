
# Sambung String
first = "Oke"
second = "Gan"

full = first + " " + second
print(full)

#Count Length String
print("Panjang Stringnya : ", len(full))

#Operator string
#Cek karakter dalam string
cek = "O" not in full
print("O ada di string full?", cek)

#Loop String
print("OKE "*3)

#Indexing
print("Index Ke - 2 : ", full[2])
print("Index Ke - (-1) : ", full[-1])
print("Index Ke 0-2: ", full[0:3])
print("Index Ke - [0,2,4,6]: ", full[0:7:2]) #cari string dengan jeda
