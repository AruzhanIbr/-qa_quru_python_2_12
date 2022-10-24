from voluptuous import Schema, PREVENT_EXTRA, Required, Optional, ALLOW_EXTRA


create_user_schema = Schema(
    {
        "name": str,
        "job": str,
        "id": str,
        "createdAt": str,
    },
    required=True,
    extra=PREVENT_EXTRA,
)

update_user_schema = Schema(
    {
        "name": str,
        "job": str,
    },
    required=True,
    extra=ALLOW_EXTRA
)

get_single_user_schema = Schema(
    {
        "data": {
            "id": int,
            "email": str,
            "first_name": str,
            "last_name": str,
            Optional("avatar"): str
        },
        "support": {
            "url": str,
            "text": str
        }
    },
    required=True,
    extra=PREVENT_EXTRA
)

successful_register_user_schema = Schema(
    {
        "id": int,
        "token": str
    },
    required=True,
    extra=PREVENT_EXTRA
)

