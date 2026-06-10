import json

data=[]

def main():
    while True:
        print("\n--- Soal ---")
        pertanyaan=input("Masukkan Pertanyaan: ")
        jawaban=input("Masukkan jawabanmu: ") 

        soal= {
            "Pertanyaan":pertanyaan,
            "Jawaban":jawaban
        }
        data.append(soal)

        lagi=input("lagi? y/n: ")
        if lagi.lower() != "y":
            break
    with open ("Flashcards.json", "w", encoding="utf-8") as write:
      json.dump(data, write, indent=2, ensure_ascii=False)  
    print(f"--- {len(data)} soal disimpan di Flashcards.json ---")  

def baca_catatan():
    print("\n --- Kamu mau baca file .json kamu? ---")
    answer=input("Masukkan jawabanmu y/n?: ")
    if answer.lower() == "y":
        with open("flashcards.json", "r") as read:
            isi=read.read()
            print(isi)
    else:
        print("Baiklah")

main()
baca_catatan()
