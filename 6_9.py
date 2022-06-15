def users_without_email(users: dict) -> list[str]:
    result: list = []
    for user in users:
        if "email" not in users[user] or not users[user]["email"]:
            result.append(users[user]["fname"])
    return result
users: dict = {
    1: {
        "fname": "fname1",
        "email": "email1"
    },
    2: {
        "fname":"fname2",
        "email": ""
    },
    3: {
        "fname": "fname3"
    }
}