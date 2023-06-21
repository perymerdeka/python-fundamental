# mengenal Tipe data Untaian Atau List

print('Membuat List')

# contoh Data List
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# Hitung panjang List
print("Panjang List: ", len(thislist))

# list Campuran
list1 = ["abc", 34, True, 40, "male"]


# akses List
print('Akses List')
print(thislist[0]) # <- hasilnya apple
print(thislist[-1]) # <- Cherry


# Loop List
for data_buah in thislist:
    print(f"Saya Punya Buah {data_buah}")


# consructor
thislist = list(("apple", "banana", "cherry"))
print(thislist)


# List Indexing
print('Indexing List')
print(thislist[2:5])
print(thislist[:4])
