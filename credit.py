# Given CC number, calculate check_digit
def calc_check_digit(card_number):

    check_sum = 0

    # Use card number length to determine which positions are even
    if len(card_number) % 2 != 0:


        for i, c in enumerate(str(card_number)):
            if i % 2 != 0:
                # If the current char position is even, multiply it by 2
                #   and accumulate the digits of the product into the checksum
                product = int(c) * 2
                for n in str(product):
                    check_sum += int(n)
            else:
                # Otherwise take the current char and accumulate iinto checksum
                check_sum += int(c)
    else:
        # Same as above execpt multiply by 2 for odd char ordinalities
        for i, c in enumerate(str(card_number)):
            if i % 2 == 0:
                product = int(c) * 2
                for n in str(product):
                    check_sum += int(n)
            else:
                check_sum += int(c)

    # Check digit is the least signficant digit in the checksum
    check_digit = int(str(check_sum)[-1:])

    return check_digit


def main():

    check_digit = 1
    card_number = input("Card number: ")

    # Define dictionary of issuers based upon key of first 1 or 2 digits of CC
    card_types = {
        "34": "AMEX",
        "35": "AMEX",
        "36": "AMEX",
        "37": "AMEX",
        "51": "MASTERCARD",
        "52": "MASTERCARD",
        "53": "MASTERCARD",
        "54": "MASTERCARD",
        "55": "MASTERCARD",
        "4":  "VISA"
    }

    if card_number[:1] == '4':
        card_type = 'VISA'
    else:
        try:
            card_type = card_types[card_number[:2]]
        except KeyError:
            card_type = 'INVALID'

    # Check for proper CC lengths based upone issuer
    if card_type == "VISA" and (len(card_number) != 13 and len(card_number) != 16):
        card_type = 'INVALID'

    if card_type == "MASTERCARD" and len(card_number) != 16:
        card_type = 'INVALID'

    if card_type == "AMEX" and len(card_number) != 15:
        card_type = 'INVALID'

    # Calculate check_digit for valid issuers
    if card_type != 'INVALID':
        check_digit = calc_check_digit(card_number)

    # If check digit is 0 for valid issuer print issuer, otherwise INVALID
    if check_digit != 0 and card_type != "INVALID":
        card_type = 'INVALID'

    print(f"{card_type}\n")


main()