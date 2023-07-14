import cuenta as c

def db_init():
    db = {}
    db['21345'] = c.Cuenta('21345', 'Arnaldo', 200, ['123', '456'])
    db['123'] = c.Cuenta('123', 'Luisa', 400, ['456'])
    db['456'] = c.Cuenta('456', 'Andrea', 300, ['21345'])
    return db