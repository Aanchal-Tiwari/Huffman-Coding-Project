from huffmancodingcode import huffmancoding

path=r"C:\Users\Aanchal\Desktop\HuffmanCodingProject\huffmansampletext.txt"
file=huffmancoding(path)
print("Compressing , please wait. It will Take a while")
print()
compressed_file_path=file.compress()
print()
print("Thanks for being patience")
print()
print("Location of compressed file : ",compressed_file_path)
print()
print("Decompressing , please wait!!")
print()
decompressed_file_path=file.decompress(compressed_file_path)
print()
print("Location of decompressed file : ",decompressed_file_path)
