import boto3

test =[
  {
    "FunctionName": "workflow-complete-task-qa",
    "FunctionArn": "arn:aws:lambda:us-east-1:583980982166:function:workflow-complete-task-qa:$LATEST",
    "Runtime": "python3.10",
    "Role": "arn:aws:iam::583980982166:role/service-role/workflow-complete-task-qa-role-6y3bmy8v",
    "Handler": "lambda_function.lambda_handler",
    "CodeSize": 681,
    "Description": "",
    "Timeout": 3,
    "MemorySize": 128,
    "LastModified": "2023-12-29T02:38:14.181+0000",
    "CodeSha256": "30rVJ3kkr3EErr8/TzfM9bIL4Dtml5qCVtsSgW9kvbo=",
    "Version": "$LATEST",
    "TracingConfig": {
      "Mode": "PassThrough"
    },
    "RevisionId": "978af9c2-c99e-4ec7-868c-b0f657ea26d3",
    "Layers": [
      {
        "Arn": "arn:aws:lambda:us-east-1:583980982166:layer:requests-python39:2",
        "CodeSize": 788128
      }
    ],
    "PackageType": "Zip",
    "Architectures": [
      "x86_64"
    ],
    "EphemeralStorage": {
      "Size": 512
    },
    "SnapStart": {
      "ApplyOn": "None",
      "OptimizationStatus": "Off"
    }
  },
  {
    "FunctionName": "workflow-get-available-tasks-qa",
    "FunctionArn": "arn:aws:lambda:us-east-1:583980982166:function:workflow-get-available-tasks-qa:$LATEST",
    "Runtime": "python3.10",
    "Role": "arn:aws:iam::583980982166:role/service-role/workflow-get-available-tasks-qa-role-myi1ktgy",
    "Handler": "lambda_function.lambda_handler",
    "CodeSize": 844,
    "Description": "",
    "Timeout": 3,
    "MemorySize": 128,
    "LastModified": "2024-01-17T18:08:49.155+0000",
    "CodeSha256": "Nk7c9Mym3n/36CbbeafeCglV9MmY6QAMcFB0Tgc3rzA=",
    "Version": "$LATEST",
    "TracingConfig": {
      "Mode": "PassThrough"
    },
    "RevisionId": "1271f134-1785-4111-bdc6-ebc96a6225e2",
    "Layers": [
      {
        "Arn": "arn:aws:lambda:us-east-1:583980982166:layer:requests-python39:2",
        "CodeSize": 788128
      }
    ],
    "PackageType": "Zip",
    "Architectures": [
      "x86_64"
    ],
    "EphemeralStorage": {
      "Size": 512
    },
    "SnapStart": {
      "ApplyOn": "None",
      "OptimizationStatus": "Off"
    }
  },
  {
    "FunctionName": "workflow-claim-task-qa",
    "FunctionArn": "arn:aws:lambda:us-east-1:583980982166:function:workflow-claim-task-qa:$LATEST",
    "Runtime": "python3.10",
    "Role": "arn:aws:iam::583980982166:role/service-role/workflow-claim-task-qa-role-pej2wv24",
    "Handler": "lambda_function.lambda_handler",
    "CodeSize": 683,
    "Description": "",
    "Timeout": 3,
    "MemorySize": 128,
    "LastModified": "2023-12-29T02:21:32.645+0000",
    "CodeSha256": "CMdVLCt+33ADCHBUj24//BoCDQd0rJ3sCs4PqlFmoNg=",
    "Version": "$LATEST",
    "TracingConfig": {
      "Mode": "PassThrough"
    },
    "RevisionId": "264b353b-acbf-47d3-b37b-ea791822cce5",
    "Layers": [
      {
        "Arn": "arn:aws:lambda:us-east-1:583980982166:layer:requests-python39:2",
        "CodeSize": 788128
      }
    ],
    "PackageType": "Zip",
    "Architectures": [
      "x86_64"
    ],
    "EphemeralStorage": {
      "Size": 512
    },
    "SnapStart": {
      "ApplyOn": "None",
      "OptimizationStatus": "Off"
    }
  },
  {
    "FunctionName": "workflow-task-release-qa",
    "FunctionArn": "arn:aws:lambda:us-east-1:583980982166:function:workflow-task-release-qa:$LATEST",
    "Runtime": "python3.10",
    "Role": "arn:aws:iam::583980982166:role/service-role/workflow-task-release-qa-role-7biwy220",
    "Handler": "lambda_function.lambda_handler",
    "CodeSize": 693,
    "Description": "",
    "Timeout": 3,
    "MemorySize": 128,
    "LastModified": "2023-12-29T01:56:52.704+0000",
    "CodeSha256": "x3mlxPDHP5KksHws8b6zZxm6FKhEkdSkulf26uuxGIU=",
    "Version": "$LATEST",
    "TracingConfig": {
      "Mode": "PassThrough"
    },
    "RevisionId": "51207fe3-f8e5-4fcd-98c4-f9e1eab72f2c",
    "Layers": [
      {
        "Arn": "arn:aws:lambda:us-east-1:583980982166:layer:requests-python39:2",
        "CodeSize": 788128
      }
    ],
    "PackageType": "Zip",
    "Architectures": [
      "x86_64"
    ],
    "EphemeralStorage": {
      "Size": 512
    },
    "SnapStart": {
      "ApplyOn": "None",
      "OptimizationStatus": "Off"
    }
  },
  {
    "FunctionName": "workflow-create-user-qa",
    "FunctionArn": "arn:aws:lambda:us-east-1:583980982166:function:workflow-create-user-QA:$LATEST",
    "Runtime": "python3.10",
    "Role": "arn:aws:iam::583980982166:role/service-role/workflow-create-user-QA-role-d3ytrl83",
    "Handler": "lambda_function.lambda_handler",
    "CodeSize": 634,
    "Description": "",
    "Timeout": 3,
    "MemorySize": 128,
    "LastModified": "2023-12-29T01:42:18.000+0000",
    "CodeSha256": "V8ZMLwlVtkFafAH6I5DeE3KqMQoxUvJp2cDtZhLuGsk=",
    "Version": "$LATEST",
    "TracingConfig": {
      "Mode": "PassThrough"
    },
    "RevisionId": "c43ea6fe-ee95-4dc9-8d56-aff4169aed70",
    "Layers": [
      {
        "Arn": "arn:aws:lambda:us-east-1:583980982166:layer:requests-python39:2",
        "CodeSize": 788128
      }
    ],
    "PackageType": "Zip",
    "Architectures": [
      "x86_64"
    ],
    "EphemeralStorage": {
      "Size": 512
    },
    "SnapStart": {
      "ApplyOn": "None",
      "OptimizationStatus": "Off"
    }
  },
  {
    "FunctionName": "workflow-get-task-by-request-qa",
    "FunctionArn": "arn:aws:lambda:us-east-1:583980982166:function:workflow-get-task-by-request-qa:$LATEST",
    "Runtime": "python3.10",
    "Role": "arn:aws:iam::583980982166:role/service-role/workflow-get-task-by-request-qa-role-sgg7yelu",
    "Handler": "lambda_function.lambda_handler",
    "CodeSize": 856,
    "Description": "",
    "Timeout": 3,
    "MemorySize": 128,
    "LastModified": "2023-12-29T02:11:57.544+0000",
    "CodeSha256": "MxJYGgxDZ/k3BcKbI3cO0tuJiPWekRhxaHiNpJtwN0c=",
    "Version": "$LATEST",
    "TracingConfig": {
      "Mode": "PassThrough"
    },
    "RevisionId": "1db89f0f-655a-4208-b3a7-755ec6c01305",
    "Layers": [
      {
        "Arn": "arn:aws:lambda:us-east-1:583980982166:layer:requests-python39:2",
        "CodeSize": 788128
      }
    ],
    "PackageType": "Zip",
    "Architectures": [
      "x86_64"
    ],
    "EphemeralStorage": {
      "Size": 512
    },
    "SnapStart": {
      "ApplyOn": "None",
      "OptimizationStatus": "Off"
    }
  },
  {
    "FunctionName": "workflow-consult-user-qa",
    "FunctionArn": "arn:aws:lambda:us-east-1:583980982166:function:workflow-consult-user-qa:$LATEST",
    "Runtime": "python3.10",
    "Role": "arn:aws:iam::583980982166:role/service-role/workflow-consult-user-qa-role-01lh2zvx",
    "Handler": "lambda_function.lambda_handler",
    "CodeSize": 544,
    "Description": "",
    "Timeout": 3,
    "MemorySize": 128,
    "LastModified": "2023-12-29T01:45:00.901+0000",
    "CodeSha256": "gf4tb6y4wOs7E4Va9g+Q9HBRemPuybevi7Fl3r4F5Rk=",
    "Version": "$LATEST",
    "TracingConfig": {
      "Mode": "PassThrough"
    },
    "RevisionId": "5115e524-7261-4e79-92d4-ef741c510678",
    "Layers": [
      {
        "Arn": "arn:aws:lambda:us-east-1:583980982166:layer:requests-python39:2",
        "CodeSize": 788128
      }
    ],
    "PackageType": "Zip",
    "Architectures": [
      "x86_64"
    ],
    "EphemeralStorage": {
      "Size": 512
    },
    "SnapStart": {
      "ApplyOn": "None",
      "OptimizationStatus": "Off"
    }
  },
  {
    "FunctionName": "workflow-update-task-info-qa",
    "FunctionArn": "arn:aws:lambda:us-east-1:583980982166:function:workflow-update-task-info-qa:$LATEST",
    "Runtime": "python3.10",
    "Role": "arn:aws:iam::583980982166:role/service-role/workflow-update-task-info-qa-role-psu6dn6j",
    "Handler": "lambda_function.lambda_handler",
    "CodeSize": 995,
    "Description": "",
    "Timeout": 3,
    "MemorySize": 128,
    "LastModified": "2023-12-29T02:27:08.490+0000",
    "CodeSha256": "skkiUh1txBmLMUBBOEoewCjZk0Ba1eWzUskorYyNN6Q=",
    "Version": "$LATEST",
    "TracingConfig": {
      "Mode": "PassThrough"
    },
    "RevisionId": "081a790c-e7be-4528-83b0-1336ab1841ba",
    "Layers": [
      {
        "Arn": "arn:aws:lambda:us-east-1:583980982166:layer:requests-python39:2",
        "CodeSize": 788128
      }
    ],
    "PackageType": "Zip",
    "Architectures": [
      "x86_64"
    ],
    "EphemeralStorage": {
      "Size": 512
    },
    "SnapStart": {
      "ApplyOn": "None",
      "OptimizationStatus": "Off"
    }
  },
  {
    "FunctionName": "workflow-request-status-qa",
    "FunctionArn": "arn:aws:lambda:us-east-1:583980982166:function:workflow-request-status-qa:$LATEST",
    "Runtime": "python3.10",
    "Role": "arn:aws:iam::583980982166:role/service-role/workflow-request-status-qa-role-j1tpmi83",
    "Handler": "lambda_function.lambda_handler",
    "CodeSize": 531,
    "Description": "",
    "Timeout": 3,
    "MemorySize": 128,
    "LastModified": "2023-12-29T02:25:43.521+0000",
    "CodeSha256": "wm+N2254L0Omoa3fQHMoj/CccKMRMQNChbp3i19tLrU=",
    "Version": "$LATEST",
    "TracingConfig": {
      "Mode": "PassThrough"
    },
    "RevisionId": "60b98b67-0733-4d5f-9f32-aa59a40d6025",
    "PackageType": "Zip",
    "Architectures": [
      "x86_64"
    ],
    "EphemeralStorage": {
      "Size": 512
    },
    "SnapStart": {
      "ApplyOn": "None",
      "OptimizationStatus": "Off"
    }
  },
  {
    "FunctionName": "workflow-create-task-instace-qa",
    "FunctionArn": "arn:aws:lambda:us-east-1:583980982166:function:workflow-create-task-instace-qa:$LATEST",
    "Runtime": "python3.10",
    "Role": "arn:aws:iam::583980982166:role/service-role/workflow-create-task-instace-qa-role-uac1j0x3",
    "Handler": "lambda_function.lambda_handler",
    "CodeSize": 608,
    "Description": "",
    "Timeout": 3,
    "MemorySize": 128,
    "LastModified": "2024-01-17T01:24:36.000+0000",
    "CodeSha256": "/NDkx69zE9LKVlyIYNJKTMlY0R7qGVCGo1jhWN1cFmk=",
    "Version": "$LATEST",
    "TracingConfig": {
      "Mode": "PassThrough"
    },
    "RevisionId": "b04e9581-c40b-4b7c-8f9f-74196a5e9eca",
    "Layers": [
      {
        "Arn": "arn:aws:lambda:us-east-1:583980982166:layer:requests-python39:2",
        "CodeSize": 788128
      }
    ],
    "PackageType": "Zip",
    "Architectures": [
      "x86_64"
    ],
    "EphemeralStorage": {
      "Size": 512
    },
    "SnapStart": {
      "ApplyOn": "None",
      "OptimizationStatus": "Off"
    }
  },
  {
    "FunctionName": "workflow-abort-task-qa",
    "FunctionArn": "arn:aws:lambda:us-east-1:583980982166:function:workflow-abort-task-qa:$LATEST",
    "Runtime": "python3.10",
    "Role": "arn:aws:iam::583980982166:role/service-role/workflow-abort-task-qa-role-pfcb3whi",
    "Handler": "lambda_function.lambda_handler",
    "CodeSize": 648,
    "Description": "",
    "Timeout": 3,
    "MemorySize": 128,
    "LastModified": "2024-01-17T17:56:10.000+0000",
    "CodeSha256": "Bvk6WWhLy8p+96Pd65CWKw/mZBp2jwz3d+olRVYULKA=",
    "Version": "$LATEST",
    "TracingConfig": {
      "Mode": "PassThrough"
    },
    "RevisionId": "96a17bff-bcbb-4bb7-81b8-6626de1e0c74",
    "Layers": [
      {
        "Arn": "arn:aws:lambda:us-east-1:583980982166:layer:requests-python39:2",
        "CodeSize": 788128
      }
    ],
    "PackageType": "Zip",
    "Architectures": [
      "x86_64"
    ],
    "EphemeralStorage": {
      "Size": 512
    },
    "SnapStart": {
      "ApplyOn": "None",
      "OptimizationStatus": "Off"
    }
  }
]

for fun in test:
    file_path = fun["FunctionName"]+".zip"
    with open(file_path,'rb') as f:
        zip_file = f.read()
    client = boto3.client('lambda')
    response = client.create_function(
    FunctionName = fun["FunctionName"][:-2]+"test-v2",
    Runtime = fun["Runtime"],
    Role= "arn:aws:iam::583980982166:role/lambda-for-workflow-v2",
    Handler = "lambda_function.lambda_handler",
    Layers = ["arn:aws:lambda:us-east-1:583980982166:layer:requests-python39:2"],
    Code = {
        'ZipFile': zip_file
    }
    )