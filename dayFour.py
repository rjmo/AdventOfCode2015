import hashlib
m = hashlib.md5()
counter = 0
string_to_hash = 'bgvyzdsv'

bytes_to_hash = string_to_hash.encode()

m.update(bytes_to_hash)

hash_value = m.hexdigest()


while hash_value[0:6] != '000000':

    string_to_hash = 'bgvyzdsv' + str(counter)

    hash_value = hashlib.md5(string_to_hash.encode()).hexdigest()

    print(counter)
    counter += 1


