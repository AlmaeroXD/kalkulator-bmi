def hitung_bmi(berat, tinggi):
    """
    Menghitung Body Mass Index (BMI)
    
    Parameter:
    berat (float): Berat badan dalam kilogram
    tinggi (float): Tinggi badan dalam meter
    
    Return:
    tuple: (BMI, kategori)
    """
    try:
        # Rumus BMI: berat / (tinggi^2)
        bmi = berat / (tinggi ** 2)
        
        # Kategorisasi BMI
        if bmi < 18.5:
            kategori = "Kekurangan Berat Badan"
        elif 18.5 <= bmi < 24.9:
            kategori = "Berat Badan Normal"
        elif 25 <= bmi < 29.9:
            kategori = "Kelebihan Berat Badan"
        else:
            kategori = "Obesitas"
        
        return round(bmi, 2), kategori
    
    except ZeroDivisionError:
        return "Error: Tinggi badan tidak boleh nol"
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("=== Kalkulator BMI ===")
    
    while True:
        try:
            # Input dari pengguna
            berat = float(input("Masukkan berat badan (kg): "))
            tinggi = float(input("Masukkan tinggi badan (m): "))
            
            # Hitung BMI
            bmi, kategori = hitung_bmi(berat, tinggi)
            
            # Tampilkan hasil
            print(f"\nBMI Anda: {bmi}")
            print(f"Kategori: {kategori}")
            
            # Opsi untuk menghitung lagi
            lanjut = input("\nIngin menghitung lagi? (y/n): ").lower()
            if lanjut != 'y':
                print("Terima kasih telah menggunakan Kalkulator BMI!")
                break
        
        except ValueError:
            print("Error: Masukkan angka yang valid!")

# Jalankan aplikasi jika script dieksekusi langsung
if __name__ == "__main__":
    main()