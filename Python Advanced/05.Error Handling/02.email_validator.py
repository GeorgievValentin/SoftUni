class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


email = input()

while not email == "End":
    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    name, domain = email.split("@")

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if domain[domain.index('.'):] not in ".com .bg .org .net":
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")

    email = input()