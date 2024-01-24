import boto3
import json
import time

list_of_ou =[
"ou-n39q-tlum1nyv",
"ou-n39q-q15ys0m1",
"ou-n39q-h5ssupdt",
"ou-n39q-vldrrg47",
"ou-n39q-f74o9x3z",
"ou-n39q-llh8qlhk",
"ou-n39q-jg5o7cut",
"ou-n39q-1gp92tsm",
"ou-n39q-79qnggt3",
"ou-n39q-0v6blm6e",
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


#"arn:aws:controltower:us-east-1::control/GTXSQEJWOBFI AGREGAR AL FINAL
list_of_rules = [
"arn:aws:controltower:us-east-1::control/LEGXJUSWUBYG",
"arn:aws:controltower:us-east-1::control/XQGJDGQQKGCR",
"arn:aws:controltower:us-east-1::control/SSXFCVHAAYDY",
"arn:aws:controltower:us-east-1::control/GTXSQEJWOBFI",
"arn:aws:controltower:us-east-1::control/AWS-GR_EC2_VOLUME_INUSE_CHECK",
"arn:aws:controltower:us-east-1::control/VVDNPMRRUWKZ",
"arn:aws:controltower:us-east-1::control/KFDQQXDMBXXV",
"arn:aws:controltower:us-east-1::control/FKQAQCYRILAK",
"arn:aws:controltower:us-east-1::control/DKOGNVMOVXDM",
"arn:aws:controltower:us-east-1::control/LHUKYNEKRWTH",
"arn:aws:controltower:us-east-1::control/UKYGXEVHJUTL",
"arn:aws:controltower:us-east-1::control/IOGKXEBDRDUW",
"arn:aws:controltower:us-east-1::control/MDWFCNUYEZKH",
"arn:aws:controltower:us-east-1::control/PWBOAFLALALP",
"arn:aws:controltower:us-east-1::control/UWMYPVTQGECU",
]

client = boto3.client('controltower')
aws_ou_alegra = 'arn:aws:organizations::867317361707:ou/o-pv5am593q3/'
#rule = "arn:aws:controltower:us-east-1::control/FKQAQCYRILAK"

counter = 0
for rule in list_of_rules:
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
    
