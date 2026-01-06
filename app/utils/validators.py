import re

PASSWORD_REGEX = re.compile(
    r"""
    ^
    (?=.*[a-z])
    (?=.*[A-Z])
    (?=.*\d)
    (?=.*[@$!%*?&#^()_+=-])
    [A-Za-z\d@$!%*?&#^()_+=-]
    {8,}
    $
    """,
    re.VERBOSE,
)

COMMON_PASSWORDS = {
    "password",
    "123456",
    "qwerty",
    "admin",
    "password123",
}

def validate_password_strength(password: str) -> None:
    if password.lower() in COMMON_PASSWORDS:
        raise ValueError("Password is too common")

    if not PASSWORD_REGEX.match(password):
        raise ValueError(
            "Password must be at least 8 characters long and include "
            "uppercase, lowercase, number, and special character"
        )
