import utils.ODRL as ODRL


def is_license_viable(license):
    return (license.permissions.isdisjoint(license.obligations) and license.permissions.isdisjoint(license.prohibitions) and license.obligations.isdisjoint(license.prohibitions) and is_actions_viable(ODRL.ARBRE, license))


def is_compatibility_viable(license_i, license_j):
    if ODRL.SHARE_ALIKE in license_i.obligations:
        return False
    if ODRL.DERIVATIVE_WORKS in license_i.prohibitions:
        return False
    return True


def is_actions_viable(tree, license):
    boolean = True
    for key in tree:
        if key in license.prohibitions:
            boolean = boolean and browse_prohibitions(tree[key], license)
        else:
            boolean = boolean and is_actions_viable(tree[key], license)
    return boolean


def browse_prohibitions(action, license):
    boolean = True
    if action != {}:
        for key in action:
            if key not in license.prohibitions or key in license.permissions or key in license.obligations:
                boolean = False
            else:
                boolean = boolean and browse_prohibitions(action[key], license)
    return boolean
