# Demo of AWS IAM usage buliding from Different IaC tools

## Demo situation description

1. build two lambdas each with different IAM roles
   - [AllowedLambdaFunction] with allow to create bucket object role
   - [DeniedLambdaFunction]  with only simple basic aws managed lambda role
2. Attach each lambda with it own log groups
3. create bucket for letting lambda to create object
4. After deployment, first check the bucket is empty
5. Invoked `DeniedLambdaFunction` and check the log group also check the bucket is empty
6. Invoked `AllowedLambdaFunction` and check the log group also check the bucket has been created a new object

## CloudFormation

### Necessary configuration

- In `AllowedLambdaRole` resource it has more policies permissions than `DeniedLambdaRole`
- To allow lambda to create object in bucket will need to permission `s3:PutObject`, `s3:PutObjectAcl`
- To narrow down to the bucket build with CloudFormation, specify the `Resource` to the bucket's arn which is build in this template. To compose this string format, use `!Sub` function in this template: `!Sub "arn:aws:s3:::${BucketBuildByCFN}/*"`