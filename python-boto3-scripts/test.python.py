import boto3


client = boto3.client('lambda')
first = 0
response = { "NextMarker": "first"}
resutl = []
while "NextMarker" in response:
    if response["NextMarker"] == "first":
        response = client.list_functions(
        FunctionVersion='ALL',
        MaxItems=50)
    else:
        response = client.list_functions(
        Marker=response["NextMarker"],
        FunctionVersion='ALL',
        MaxItems=50)
    
    for functions in response['Fuctions']:
        if "WORKFLOW" in function["FunctionName"].upper() and 'QA' in function["FunctionName"].upper():
            resutl.append(function)


print(resutl)

