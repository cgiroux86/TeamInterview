def validate_register_fields(req):
    data = req.get_json(silent=True)
    fields = ['first_name', 'last_name', 'email', 'password']
    for d in data.keys():
        if d not in fields:
            return False
    return True
