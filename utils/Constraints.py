import utils.ODRL as ODRL


def is_license_viable(license):
    if not(license.permissions.isdisjoint(license.obligations) and license.permissions.isdisjoint(license.prohibitions) and license.obligations.isdisjoint(license.prohibitions)):
        return False
    return True


def is_compatibility_viable(license_i, license_j):
    if ODRL.SHARE_ALIKE in license_i.obligations:
        return False
    if ODRL.DERIVATIVE_WORKS in license_i.prohibitions:
        return False
    return True

def is_actions_viable(action_i, action_j, licence):
    if action_i in licence.permissions:
        if action_j in licence.permissions:
            return True
        else:
            return False
    elif action_i in licence.obligations:
        if action_j in licence.obligations:
            return True
        else:
            return False

def is_permissions_viale(license):
    boolean = True
    for permission in license.permissions
        for key in ARBRE
            boolean = browse_dict(key, ARBRE)
    return boolean


def browse_dict(node, action):

    for key in ARBRE:
        print (key), ARBRE[key]
