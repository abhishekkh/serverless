## Todo service
Simple todo service to create/update/list todos using the AWS lambda architecture of API Gateway, http events and dynamodb storage.

### Create service using template
```
serverless create --template aws-python

```

### Deploy service
```
cd hello-service
serverless deploy

Serverless: Packaging service...
Serverless: Excluding development dependencies...
Serverless: Uploading CloudFormation file to S3...
Serverless: Uploading artifacts...
Serverless: Uploading service hello-service.zip file to S3 (2.19 KB)...
Serverless: Validating template...
Serverless: Updating Stack...
Serverless: Checking Stack update progress...
..........................
Serverless: Stack update finished...
Service Information
service: hello-service
stage: dev
region: us-east-1
stack: hello-service-dev
resources: 24
api keys:
  None
endpoints:
  GET - https://qglab4k6pd.execute-api.us-east-1.amazonaws.com/dev/hello
  POST - https://qglab4k6pd.execute-api.us-east-1.amazonaws.com/dev/todos
  GET - https://qglab4k6pd.execute-api.us-east-1.amazonaws.com/dev/todos
functions:
  hello: hello-service-dev-hello
  create: hello-service-dev-create
  list: hello-service-dev-list
layers:
  None
Serverless: Removing old service artifacts from S3...

```

### Invoke function
```
serverless invoke -f hello -l
serverless invoke -f list -l | jq "."
```

### Using REST endpoint
```
GET: 
curl https://qglab4k6pd.execute-api.us-east-1.amazonaws.com/dev/todos | jq '.'

POST:
curl -X POST https://qglab4k6pd.execute-api.us-east-1.amazonaws.com/dev/todos --data '{ "text": "Learn Serverless" }'

```


