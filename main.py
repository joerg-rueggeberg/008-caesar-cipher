from art import logo

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
    'x', 'y', 'z'
]


def caesar(text_chosen, shift_chosen, direction_chosen):
    cipher = ""

    if direction_chosen == "dekodiert":
        shift_chosen *= -1
    for c in text_chosen:
        if c not in alphabet:
            cipher += c
        elif (alphabet.index(c) + shift_chosen) < len(alphabet):
            cipher += alphabet[alphabet.index(c) + shift_chosen]
        else:
            diff = (alphabet.index(c) + shift_chosen) - len(alphabet)
            cipher += alphabet[diff]
    print(f"\nDie {direction_chosen}e Nachricht lautet: {cipher}")


end = False
print(logo)
while not end:
    direction = input(
        "\nTippe 'kodiert' um zu verschlüsseln oder 'dekodiert' um zu entschlüsseln:\n"
    )
    text = input("\nTippe deine Nachricht:\n").lower()
    shift = int(input("\nTippe deine Rotationsnummer:\n"))
    shift = shift % 26

    caesar(text, shift, direction)

    con = input("\nNoch einmal? 'ja'/ 'nein': ")
    if con == "nein":
        end = True
print("\nBis zum nächsten mal!")
