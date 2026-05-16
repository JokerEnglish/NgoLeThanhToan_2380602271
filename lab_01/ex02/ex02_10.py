def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]
input_string=input("moi nhap chuoi can dao nguoc: ")
print("chuoi sau khi dao nguoc la: ",dao_nguoc_chuoi(input_string))