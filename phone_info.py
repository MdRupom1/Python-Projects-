import phonenumbers
from phonenumbers import geocoder, carrier, timezone, PhoneNumberFormat, format_number, number_type, PhoneNumberType, is_possible_number, is_valid_number

# Input the users phone number 
raw_number = input("Enter Your Phone Number with Country Code (Ex. +8801712345678): ")

# Parse number
try:
    parsed_number = phonenumbers.parse(raw_number, None)

    print("\n---Informations of the phone numbe---")
    print(f"Parsed Number (Country code + National number): {parsed_number}")

    # Validation
    print(f"Possible numbers? : {is_possible_number(parsed_number)}")
    print(f"Valid number? : {is_valid_number(parsed_number)}")

    # Formats
    print("\n Formats:")
    print("International:", format_number(parsed_number, PhoneNumberFormat.INTERNATIONAL))
    print("National:", format_number(parsed_number, PhoneNumberFormat.NATIONAL))
    print("E.164:", format_number(parsed_number, PhoneNumberFormat.E164))

    # Number type
    num_type = number_type(parsed_number)
    type_dict = {
        PhoneNumberType.FIXED_LINE: "Fixed line",
        PhoneNumberType.MOBILE: "Mobile",
        PhoneNumberType.FIXED_LINE_OR_MOBILE: "Fixed line or Mobile",
        PhoneNumberType.TOLL_FREE: "Toll free",
        PhoneNumberType.PREMIUM_RATE: "Premium rate",
        PhoneNumberType.SHARED_COST: "Shared cost",
        PhoneNumberType.VOIP: "VoIP",
        PhoneNumberType.PERSONAL_NUMBER: "Personal number",
        PhoneNumberType.PAGER: "Pager",
        PhoneNumberType.UAN: "UAN",
        PhoneNumberType.UNKNOWN: "Unknown",
    }
    print("\n Number type:", type_dict.get(num_type, "Unknown"))

    # Geocoding
    print("Region Country:", geocoder.description_for_number(parsed_number, "en"))  

    # Carrier
    print("Operator (Carrier):", carrier.name_for_number(parsed_number, "en"))

    # Timezones
    print("Possible time zone:", timezone.time_zones_for_number(parsed_number))

except phonenumbers.NumberParseException as e:
    print("❌ The number could not be parsed.:", e)
