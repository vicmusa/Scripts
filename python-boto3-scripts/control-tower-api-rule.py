import boto3
import json
import time

list_of_ou =[
"ou-n39q-ju7vwq1u",
"ou-n39q-g2o6yn14",
"ou-n39q-5t3xp2qx",
"ou-n39q-p0lwpiuw",
"ou-n39q-kpuekqa0",
"ou-n39q-it9t4lle",
"ou-n39q-dace87ux",
"ou-n39q-hs64yle8",
"ou-n39q-9wkuiq40",
"ou-n39q-trebqyed",
"ou-n39q-spc814jy",
"ou-n39q-ns4ttlal",
"ou-n39q-3jdijux1",
"ou-n39q-lsuj3c8t",
"ou-n39q-pgv3qd8g",
"ou-n39q-kvuvh58g",
"ou-n39q-pba6v9ak",
"ou-n39q-2w6e8o9g",
"ou-n39q-5dbigaez",
"ou-n39q-wgk13i4s"
]

client = boto3.client('controltower')
aws_ou_alegra = 'arn:aws:organizations::867317361707:ou/o-pv5am593q3/'
rule = 'arn:aws:controltower:us-east-1::control/GTXSQEJWOBFI'

counter = 0
for ou in list_of_ou:
    unit = aws_ou_alegra + ou
    response = client.enable_control(
         controlIdentifier = rule,
         targetIdentifier=unit
    )
    print(response)
    counter += 1
    if counter == 10:
         time.sleep(60*10)
         counter = 0
    
