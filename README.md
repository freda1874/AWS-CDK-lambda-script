<h1 align="center"> AWS CI/CD Pipeline with GitHub Actions practice </h1>

<p>
  This project demonstrates how to build an <b>AWS CI/CD pipeline</b> using <b>GitHub Actions</b>, <b> AWS CDK (TypeScript)</b>, <b>AWS Lambda (Python)</b>, and DynamoDB </b>.
  It automates infrastructure deployment while incorporating <b>AWS Lambda</b> and <b>DynamoDB</b> to track and store website visits.
</p>
 
<h2>📚 Key Concepts Practiced</h2>
<ul>
  <li>✅ <b>AWS CDK</b>: Defines infrastructure as code using TypeScript.</li>
  <li>✅ <b>GitHub Actions</b>: Automates deployments and version updates.</li>
  <li>✅ <b>AWS Lambda</b>: Runs a Python function for visit tracking.</li>
  <li>✅ <b>DynamoDB</b>: Stores visit counts as a NoSQL database.</li>
  <li>✅ <b>Git Hooks</b>: Automatically increments version numbers.</li>
</ul>
 
<p align="center">
  <img src="https://github.com/user-attachments/assets/c55670cc-fb8b-4e01-a9ec-429cc8d9b875" alt="Project Image" width="600">
</p>


<h2>⚙️ Setting Up the Project</h2>

<ul>
  <li>Install <b>AWS CLI</b> and configure your AWS credentials: <code>aws configure</code></li>
  <li>Install <b>Node.js</b> and AWS CDK globally: <code>npm install -g aws-cdk</code></li>
  <li>Ensure <b>Python 3.9+</b> is installed for the Lambda function.</li>
  <li>Enable GitHub Actions by adding AWS credentials as secrets in GitHub.</li>
</ul>

<h2> Building and Deploying the Project</h2>

<h3>1️⃣ Initialize a New AWS CDK Project</h3>
using typescript for example
<pre>
cdk init app --language typescript
</pre>

<h3>2️⃣ Define AWS Resources in CDK</h3>
<p>In <b>cicd-aws-stack.ts</b>, define a Lambda function with DynamoDB access:</p>

<pre>
const lambdaFunction = new lambda.Function(this, "LambdaFunction", {
    runtime: lambda.Runtime.PYTHON_3_9,
    code: lambda.Code.fromAsset("lambda"), 
    handler: "main.handler",
    environment: {
        VERSION: process.env.VERSION || "0.0",
        TABLE_NAME: table.tableName,
    }
});
</pre>

<p>Define a <b>DynamoDB table</b> for visit tracking:</p>
<pre>
const table = new dynamodb.Table(this, "VisitorTimeTable", {
    partitionKey: { name: "key", type: dynamodb.AttributeType.STRING },
    billingMode: dynamodb.BillingMode.PAY_PER_REQUEST,
});
</pre>

<h3>3️⃣ Enable Function URL for Direct HTTP Requests</h3>
<pre>
lambdaFunction.addFunctionUrl({
    authType: lambda.FunctionUrlAuthType.NONE,
});
</pre>

<h3>4️⃣ Deploy the CDK Stack</h3>
<pre>
cdk bootstrap --region us-west-2
cdk synth
cdk deploy
</pre>

---

<h2> Configuring GitHub Actions for CI/CD</h2>

![image](https://github.com/user-attachments/assets/2d90d0d9-369d-4d48-a686-463821a79209)

 
<h3> Create the GitHub Actions Workflow</h3>
<p>Workflows must be inside <code>.github/workflows/</code>. This setup:</p>
<ul>
  <li> Caches dependencies for faster builds.</li>
  <li> Deploys the CDK stack using AWS credentials.</li>
  <li> Automatically updates the version.</li>
</ul>

<p>To enable GitHub Actions deployment, add AWS credentials in GitHub:</p>
<pre>
GitHub Repo -> Settings -> Secrets and variables -> Actions -> New Repository Secret
</pre>

<h2> Automating Versioning with a Git Hook</h2>

<h3>1️⃣ Enable Git Hooks</h3>
<p>Since <code>.git</code> is hidden, enable it and navigate to the hooks directory.</p>

<h3>2️⃣ Create a Pre-Commit Hook</h3>
<p>Copy and rename <code>pre-commit.sample</code> to <code>pre-commit</code>, then add this script:</p>

<pre>
#!/bin/sh 

VERSION=$(sed -n 's/VERSION="\([^"]*\)"/\1/p' .env)

if [[ -n $VERSION ]]; then
    IFS='.' read -ra ADDR <<< $VERSION 
    last_index=$((${#ADDR[@]} - 1))
    ADDR[$last_index]=$((${ADDR[$last_index]} + 1))
    NEW_VERSION=$(IFS=.; echo "${ADDR[*]}")

    perl -pi -e "s/$VERSION/$NEW_VERSION/g" .env
    echo "NEW version: $NEW_VERSION"
    git add .env
fi 
</pre>

<h3>3️⃣ Make the Script Executable</h3>
<pre>
chmod +x .git/hooks/pre-commit
</pre>

---

<h2> Connecting Lambda to DynamoDB</h2>

<p>In the Lambda function, use <b>Boto3</b> to interact with DynamoDB:</p>

<pre>
import boto3
import os

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["TABLE_NAME"])

def handler(event, context):
    table.update_item(
        Key={"key": "visitor_count"},
        UpdateExpression="ADD visit_count :inc",
        ExpressionAttributeValues={":inc": 1}
    )
    return {"statusCode": 200, "body": "Visit count updated!"}
</pre>

![image](https://github.com/user-attachments/assets/2a7c8781-0874-4d7f-a0c7-30259237a674)

<h3>Filtering Out Unwanted Paths</h3>
<p>Ensure only root paths increase the visit count:</p>

<pre>
if event["rawPath"] != "/":
    return {"statusCode": 404, "body": "Not Found"}
</pre>
 

---

<h2>📜 Credit</h2>

<p>Inspired by <a href="https://www.youtube.com/watch?v=9uMcN66mfwE">this tutorial</a>.</p>
