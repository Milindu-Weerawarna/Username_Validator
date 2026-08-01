"""Username validation helpers."""

MIN_USERNAME_LENGTH = 3


def validate_username(username: str) -> tuple[bool, str | None]:
    """Return whether a username is valid and an optional error message."""
    if not isinstance(username, str):
        return False, "Username must be a string"

    if username.strip() == "":
        return False, "Username is required"

    if len(username) < MIN_USERNAME_LENGTH:
        return (
            False,
            f"Username must contain at least {MIN_USERNAME_LENGTH} characters",
        )

    return True, None
