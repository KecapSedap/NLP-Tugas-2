import nltk.tokenize.punkt

print("Memulai Algoritma Punkt ...")

dir = 'C:/Users/User/Documents/Important Stuff/KULI-AH/Semester6/NLP/Tugas/Tugas2/Tugas 2a/'

f = open(f"{dir}Teks Asli.txt", "r", encoding='utf8')
teks = f.read()
f.close()

seg_kalimat = nltk.data.load('indonesian.pickle')
teks_kalimat = seg_kalimat.tokenize(teks)

with open((f'{dir}Punkt.txt'), 'w', encoding='utf8') as f:
  f.write("")

  for kalimat in teks_kalimat:
    with open((f'{dir}Punkt.txt'), 'a', encoding='utf8') as f:
      f.write(kalimat.strip())
      f.write("\n")

print("Teks Berhasil Disimpan!")
