from pathlib import Path

def read_word(file, size, spacer):
    word = b""
    for i in range(size):
        b = file.read(1)
        if b == spacer: return word
        else: word += b

def read_word_fix(file, size):
    word = b""
    for i in range(size):
        b = file.read(4)
        return word

def write_word_var(x, file, byteorder="little", spacer=b"\x00"):
    file.write(x.to_bytes((x.bit_length()+7) // 8, byteorder))
    file.write(spacer)

def write_word_fix(x, file, byteorder="little"):
    file.write(x.to_bytes(4, byteorder))

def decode_as_list(path, bound, byteorder="little", spacer=b"\x00"):
    list = []
    file_size = Path(path).stat().st_size
    with open(path, "rb") as file:
        while file_size > 0:
            w = read_word(file, file_size, spacer)
            n = int.from_bytes(w, byteorder)
            if bound != 0 and n > bound:
                break
            list.append(n)
            file_size -= len(w)+1       # 1 because of the 1 byte spacer
    return list
