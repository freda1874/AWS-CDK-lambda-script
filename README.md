<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AWS CI/CD Pipeline with GitHub Actions & CDK</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            max-width: 900px;
            margin: auto;
            padding: 20px;
            background: #f4f4f4;
            color: #333;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        code {
            background: #ddd;
            padding: 3px 6px;
            border-radius: 5px;
            font-family: Consolas, monospace;
        }
        pre {
            background: #2c3e50;
            color: white;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        .highlight {
            background: #3498db;
            color: white;
            padding: 5px 10px;
            border-radius: 5px;
        }
        ul {
            padding-left: 20px;
        }
        .footer {
            margin-top: 20px;
            font-size: 0.9em;
            color: #555;
        }
    </style>
</head>
<body>

    <h1 align="center">🚀 AWS CI/CD Pipeline with GitHub Actions & CDK</h1>
    
    <p align="center">
        A hands-on project to automate deployments using AWS CDK (TypeScript), AWS Lambda (Python), and DynamoDB, with GitHub Actions handling CI/CD.  
        This project builds a versioned pipeline, counts page visits, and stores them in DynamoDB.  
    </p>

    <h2>📌 Key Concepts Practiced</h2>
    <ul>
        <li>✅ Building an <b>AWS CI/CD pipeline</b> with GitHub Actions</li>
        <li>✅ Using <b>AWS CDK</b> to define cloud infrastructure</li>
        <li>✅ Deploying and updating an <b>AWS Lambda function (Python)</b></li>
        <li>✅ Storing and managing data in <b>DynamoDB</b></li>
        <li>✅ Automating versioning using <b>Git Hooks</b></li>
        <li>✅ Handling <b>HTTP requests with Lambda function URLs</b></li>
    </ul>

    <h2>⚙️ How to Build & Deploy</h2>

    <h3>1️⃣ Install AWS CDK</h3>
    <pre>npm install -g aws-cdk</pre>

    <h3>2️⃣ Create a New CDK App</h3>
    <pre>cdk init app --language typescript</pre>

    <h3>3️⃣ Define AWS Resources (CDK Stack)</h3>
    <p>Inside <code>cicd-aws-stack.ts</code>, define the Lambda function and DynamoDB table:</p>

    <h4>📌 Lambda Function (Python 3.9)</h4>
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

    <h4>📌 DynamoDB Table</h4>
    <pre>
const table = new dynamodb.Table(this, "VisitorTimeTable", {
    partitionKey: { name: "key", type: dynamodb.AttributeType.STRING },
    billingMode: dynamodb.BillingMode.PAY_PER_REQUEST,
});
    </pre>

    <h3>4️⃣ Add Function URL for Lambda</h3>
    <p>Without <code>addFunctionUrl()</code>, Lambda is not directly accessible via HTTP requests.</p>
    <pre>cdk bootstrap --region us-west-2</pre>

    <h3>5️⃣ Set Up GitHub Actions CI/CD Pipeline</h3>
    <p>Workflows must be inside the <code>.github/workflows/</code> directory.</p>
    <p>To use dependency caching for <code>package.json</code>, set up a cache step in GitHub Actions.</p>

    <h3>6️⃣ Deploy CDK Stack with AWS Access Credentials</h3>
    <p>Go to <b>GitHub → Repo Settings → Secrets & Variables → Actions</b> and add your AWS access key & secret.</p>

    <h3>7️⃣ Push Code to Main Branch & Trigger Deployment</h3>
    <p>After pushing code to the <code>main</code> branch, go to the <b>Actions</b> tab in GitHub.</p>

    <h3>8️⃣ Verify Deployment in AWS</h3>
    <p>Once the deployment succeeds, check AWS Lambda and DynamoDB for expected behavior.</p>

    <h2>🔄 Automating Versioning with Git Hooks</h2>

    <h3>1️⃣ Enable Git Hooks</h3>
    <p>The <code>.git</code> directory is hidden, so enable hooks and create a <b>pre-commit</b> script.</p>

    <h3>2️⃣ Add Versioning Script (pre-commit hook)</h3>
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

    <h2>🔗 Connecting Lambda with DynamoDB</h2>

    <h3>1️⃣ Install AWS SDK for Python</h3>
    <pre>pip install boto3</pre>

    <h3>2️⃣ Modify Lambda to Connect to DynamoDB</h3>
    <p>The function reads/writes visit count data.</p>

    <h3>3️⃣ Filter Unwanted Paths in Lambda</h3>
    <p>Ignore non-root paths before processing requests.</p>

    <h2>🎥 Credit</h2>
    <p>Tutorial inspiration: <a href="https://www.youtube.com/watch?v=9uMcN66mfwE">AWS CI/CD YouTube Tutorial</a></p>

    <div class="footer">
        <p>📧 Contact: your.email@example.com | 🌍 GitHub: <a href="https://github.com/yourusername">yourusername</a></p>
    </div>

</body>
</html>
