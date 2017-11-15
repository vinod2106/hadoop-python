'''
Created on 12 Nov 2017

@author: vinsharm
'''
import bcrypt as c


def test_pass(encrypted_pass, filename):
    salt = encrypted_pass[0:2]
    dict_file = open(filename, 'r')
    for word in dict_file.readlines():
        word = word.strip('\n')
        #crypt_word = c.crypt(word, salt)
        crypt_word = c.hashpw(word, c.gensalt())
        if (crypt_word == encrypted_pass.strip('\n')):
            print("[$] Found Password: " + word + "\n")
            return
    print("[~] Password not found.\n")
    return


def main(filename, dict_file):
    pass_file = open(filename, 'r')
    for line in pass_file.readlines():
        if ":" in line:
            user = line.split(':')[0]
            crypt_pass = line.split(':')[1].strip(' ')
            print(crypt_pass)
            print ("[^] Cracking Password For: " + user)
            test_pass(crypt_pass, dict_file)


#dict_file = input("What is your dictionary file name? ")
#password_file = input("What is your password file name? ")
if __name__ == '__main__':
    password_file = 'passwords.txt'
    dict_file = 'dictionary.txt'
    main(password_file, dict_file)
