import utils.ODRL as ODRL


def is_license_viable(license):
    return (license.permissions.isdisjoint(license.obligations) and license.permissions.isdisjoint(license.prohibitions) and license.obligations.isdisjoint(license.prohibitions) and is_permissions_viable(license))


def is_compatibility_viable(license_i, license_j):
    if ODRL.SHARE_ALIKE in license_i.obligations:
        return False
    if ODRL.DERIVATIVE_WORKS in license_i.prohibitions:
        return False
    return True

def is_actions_viable(action_i, action_j, license):
    if action_i in license.permissions:
        if action_j in license.permissions:
            return True
        else:
            return False
    elif action_i in license.obligations:
        if action_j in license.obligations:
            return True
        else:
            return False

def is_permissions_viable(license):
    boolean = True
    return boolean

def browse_dict(tree, license):
    boolean = True
    for key in ARBRE:
        if ODRL.key in license.permissions:
            boolean = boolean and nom(ARBRE[key], license)
        else:
            boolean = boolean and browse_dict(ARBRE[key], license)
    return boolean

def nom(action, license):
    boolean = True
    if action != {}:
        for key in action:
            if not(ODRL.key in license.permissions)
                boolean = False
            else:
                boolean = boolean and nom(action[key], license)
    return boolean
