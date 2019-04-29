from datasources import Manifest

def Sentinel1(event, context):
    manifest = Manifest()
    manifest['Sentinel1'].search(**event)
    response = manifest.execute()
    return response


