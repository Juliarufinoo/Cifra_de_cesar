MODE_ENCRYPT = 0
MODE_DECRYPT = 1 

def caesar(data, key, mode):
    alphabet = 'abcdefghijklmnopqrstuvwyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÕÍÚÇ'
    new_data = ''  
    
    for c in data: 
        index = alphabet.find(c)
        if index == -1:
            new_data += c  
        else:
            new_index = index + key if mode == MODE_ENCRYPT else index - key
            new_index = new_index % len(alphabet)  
            new_data += alphabet[new_index]  
    return new_data

key = int(input("Digite aqui o valor da chave: "))
original = input("Digite a frase para ser encriptada: ")
print('Original:', original)
ciphered = caesar(original, key, MODE_ENCRYPT)
print('Encriptada:', ciphered)
plain = caesar(ciphered, key, MODE_DECRYPT)
print('Decriptada:', plain)
