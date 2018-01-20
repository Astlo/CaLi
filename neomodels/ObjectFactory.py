from objectmodels.License import License
from objectmodels.Dataset import Dataset


def objectLicense(neo_license):
    obj_license = License()
    obj_license.set_labels(neo_license.labels)
    obj_license.set_permissions(set(neo_license.permissions))
    obj_license.set_obligations(set(neo_license.obligations))
    obj_license.set_prohibitions(set(neo_license.prohibitions))
    obj_license.set_datasets([])
    return obj_license


def objectDataset(neo_dataset):
    obj_dataset = Dataset()
    obj_dataset.set_label(neo_dataset.label)
    obj_dataset.set_uri(neo_dataset.uri)
    obj_dataset.set_description(neo_dataset.description)
    return obj_dataset