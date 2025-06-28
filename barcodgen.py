import barcode
from barcode.writer import ImageWriter

def generate_barcode(data, filename):

    code128 = barcode.get_barcode_class('code128')
   
    barcode_obj = code128(data, writer=ImageWriter())

 
    full_filename = barcode_obj.save(filename)
    print(f"Barcode Succesfully: {full_filename}")

if __name__ == "__main__":
    user_input = input("Input teks or number for barcode: ")
    filename = input("Name file: ")
    generate_barcode(user_input, filename)
