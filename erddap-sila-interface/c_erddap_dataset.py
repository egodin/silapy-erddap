from xml.etree.ElementTree import Element, SubElement


class ERDDAPDataset:
    def __init__(self, dataset_type, dataset_id, dataset_active, dataset_filename):
        # set the dataset root and its attributes as a dictionary
        # For example: <dataset type="EDDTableFromAsciiFiles" datasetID="downloads_d035_742e_ed6e" active="true">
        root = Element('dataset', {'type': dataset_type, 'datasetID': dataset_id, 'active': dataset_active})

        # set the default dataset attributes
        reloadEveryNMinutes = SubElement(root, 'reloadEveryNMinutes')
        updateEveryNMillis = SubElement(root, 'updateEveryNMillis')  # default=10000
        fileDir = SubElement(root, 'fileDir')  # default=/ var / www / html / downloads /
        fileNameRegex = SubElement(root, 'fileNameRegex')  # filename of the data file, as a class arg
        recursive = SubElement(root, 'recursive')  # default=true
        pathRegex = SubElement(root, 'pathRegex')  # default=.*
        metadataFrom = SubElement(root, 'metadataFrom')  # default=last
        standardizeWhat = SubElement(root, 'standardizeWhat')  # default=0
        charset = SubElement(root, 'charset')  # default=UTF - 8
        columnSeparator = SubElement(root, 'columnSeparator')  # default=,
        columnNamesRow = SubElement(root, 'columnNamesRow')  # default=1
        firstDataRow = SubElement(root, 'firstDataRow')  # default=2
        sortedColumnSourceName = SubElement(root, 'sortedColumnSourceName')  # default=time
        sortedFilesBySourceNames = SubElement(root, 'sortedFilesBySourceNames')  # default=time
        fileTableInMemory = SubElement(root, 'fileTableInMemory')  # default=false
        accessibleViaFiles = SubElement(root, 'accessibleViaFiles')  # default=false

        # set values to default dataset attributes
        reloadEveryNMinutes.text = str(1400)
