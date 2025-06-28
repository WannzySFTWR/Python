import barcode
from barcode.writer import ImageWriter

# Fungsi untuk membuat barcode
def generate_barcode(data, filename):

    code128 = barcode.get_barcode_class('code128')
   
    barcode_obj = code128(data, writer=ImageWriter())

 
    full_filename = barcode_obj.save(filename)
    print(f"Barcode berhasil dibuat: {full_filename}")

if __name__ == "__main__":
    user_input = input("Masukkan teks atau angka untuk barcode: ")
    filename = input("Masukkan nama file hasil (tanpa ekstensi): ")
    generate_barcode(user_input, filename)
