# SIMPLE JOKE POC ALEXA 

### 0) create dir
- mkdir lambda/py/lambda_upload
- cp lambda/py/requirements.txt  lambda/py/lambda_upload/

### 1) virtual env
- cd up_dir/
- cp create_env.sh ../../
- ./create_env.sh alexa_joke_poc true

### 2) lambda files
- cd alexa_joke_poc
- ./create_libs.sh alexa_joke_poc true all

### 3) zip
- ZIP folder: lambda/py/lambda_upload
- Upload to Amazon Lambda

