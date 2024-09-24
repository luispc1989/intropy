def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Verifica se o comprimento da matrícula é válido
    if not valid_length(s):
        return False

    # Verifica se a matrícula começa com pelo menos duas letras
    if not starts_with_two_letters(s):
        return False

    # Verifica se os números estão no final e que o primeiro número não é zero
    if not numbers_at_end(s):
        return False

    # Verifica se a matrícula contém apenas letras e números (sem espaços, pontuações, etc.)
    if not all_characters_valid(s):
        return False

    return True


def valid_length(s):
    # Verifica se a matrícula tem entre 2 e 6 caracteres
    return 2 <= len(s) <= 6


def starts_with_two_letters(s):
    # Verifica se os dois primeiros caracteres são letras
    return s[0:2].isalpha()


def numbers_at_end(s):
    # Encontra a posição do primeiro número
    for i in range(len(s)):
        if s[i].isdigit():
            # Verifica se todos os caracteres após o primeiro número são números
            if not s[i:].isdigit():
                return False
            # Verifica se o primeiro número não é '0'
            if s[i] == '0':
                return False
            break
    return True


def all_characters_valid(s):
    # Verifica se todos os caracteres são letras ou números
    return s.isalnum()


main()
