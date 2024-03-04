def hitung_grade(nilai):
    if nilai >= 80:
        return 'A'
    elif nilai >= 77:
        return 'A-'
    elif nilai >= 74:
        return 'B+'
    elif nilai >= 68:
        return 'B'
    elif nilai >= 65:
        return 'B-'
    elif nilai >= 62:
        return 'C+'
    elif nilai >= 56:
        return 'C'
    elif nilai >= 45:
        return 'D'
    else:
        return 'E'

def main():
    try:
        nama = input("Masukkan nama mahasiswa: ")
        nim = input("Masukkan NIM mahasiswa: ")
        nilai = float(input("Masukkan nilai mahasiswa: "))
        if 0 <= nilai <= 100:
            grade = hitung_grade(nilai)
            print(f"Identitas: {nama} ({nim})")
            print(f"Grade untuk nilai {nilai} adalah: {grade}")
        else:
            print("Input nilai tidak valid. Nilai harus berada dalam rentang 0 hingga 100.")
    except ValueError:
        print("Input tidak valid. Mohon masukkan nilai numerik.")

if __name__ == "__main__":
    main()
