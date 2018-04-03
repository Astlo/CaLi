import utils.ODRL as ODRL


def is_license_viable(license):
    if not(license.permissions.isdisjoint(license.obligations) and license.permissions.isdisjoint(license.prohibitions) and license.obligations.isdisjoint(license.prohibitions)) or is_relation_viable(ODRL.REPRODUCTION, ODRL.CONCURRENTUSE, license):
        return False
    return True


def is_compatibility_viable(license_i, license_j):
    if ODRL.SHARE_ALIKE in license_i.obligations:
        return False
    if ODRL.DERIVATIVE_WORKS in license_i.prohibitions:
        return False
    return True

def is_relation_viable(action_i, action_j, licence):
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
