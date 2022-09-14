import json
import boto3
import pprint 
import webbrowser, os
import io
from io import BytesIO
import sys
import unicodedata
import parser

def strip_accents(text):
    try:
        text = unicode(text, 'utf-8')
    except NameError: # unicode is a default on python 3 
        pass

    text = unicodedata.normalize('NFD', text)\
           .encode('ascii', 'ignore')\
           .decode("utf-8")

    return str(text)

def lambda_handler(event, context):
    
    print(event)
    
    client = boto3.client('textract')
    response = client.analyze_expense(
        Document={
            'S3Object': {
                'Bucket': 'plaza-textract',
                'Name': event['Records'][0]['s3']['object']['key'].replace("+"," ")
            }
        }
        
    )
    
    response_forms = client.analyze_document(
        Document={
            'S3Object': {
                'Bucket': 'plaza-textract',
                'Name': event['Records'][0]['s3']['object']['key'].replace("+"," ")
            }
        },
        FeatureTypes=[
            'FORMS'
        ]
        
    )
    
    print(response)
    
    print("--------FORM RESPONSE---------------")
    
    print(response_forms)
    
    print("----------------EXPENSE MAP--------------------")
    formatter_response = parser.tax_parser(response)
    print(formatter_response)
    print('------------------FORM MAP---------------------------')
    word_map = parser.map_word_id(response_forms)
    key_map = parser.get_key_map(response_forms, word_map)
    value_map = parser.get_value_map(response_forms, word_map)
    final_map = parser.get_kv_map(key_map, value_map)
    print(final_map)
    json_response = {}
    json_items_array = []
    
    if len(response["ExpenseDocuments"][0]["LineItemGroups"][0]["LineItems"]) == 0 :
        items = []
        aux = {}
        aux['CÓDIGO'] = formatter_response['CÓDIGO']
        aux['Cantidad'] = formatter_response['Cantidad']
        aux['Precio Venta Unitario'] = formatter_response['Precio Venta Unitario']
        aux['TOTAL'] = formatter_response['TOTAL']
        formatter_response.pop('CÓDIGO')
        formatter_response.pop('Cantidad')
        formatter_response.pop('Precio Venta Unitario')
        formatter_response.pop('TOTAL')
        final_map.pop('CÓDIGO')
        final_map.pop('Cantidad')
        final_map.pop('Precio Venta Unitario')
        final_map.pop('TOTAL')
        items.append(aux)
        formatter_response['Items'] = items
        # FALTA AGREGAR CODIGO O DESCRIPCION 
    else:
        listofitems = parser.additems(response)
        formatter_response['Items'] = listofitems
    for clave in final_map:
        if not clave in formatter_response:
            formatter_response[clave] = final_map[clave]
    print(formatter_response)
    
    
    
   
   # VER SI TODAS LAS CLAVES ESTAN BIEN #
    
    for clave in formatter_response:
        if clave != None and ":" in clave:
            print("estoy aqui %s"% clave)
            new_clave = clave.replace(":","")
            formatter_response[new_clave] = formatter_response.pop(clave)
    
    
    print(formatter_response)
    with open('/tmp/sample.txt', 'w') as f:
        json.dump(formatter_response, f)
    s3_client = boto3.client('s3')
    response = s3_client.upload_file('/tmp/sample.txt', 'plaza-textract', event['Records'][0]['s3']['object']['key'].replace("+"," ").replace("pdf","json"))
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }