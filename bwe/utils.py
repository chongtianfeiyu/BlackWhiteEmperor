def find_by_id(id, entries):
    for entry in entries:
        if entry.id == id:
            return entry
    return None

import json
def build_list_json(entries):
    array = []
    for entry in entries:
        entryDict = {}
        for field in entry.fieldList:
            entryDict[field] = getattr(entry, field)
        array.append(entryDict)
    return json.dumps(array)

def build_single_json(entry):
    entryDict = {}
    for field in entry.fieldList:
        entryDict[field] = getattr(entry, field)
    array.append(entryDict)
    return json.dumps(entryDict)
