<h1 align="center">🚀 AWS CI/CD Pipeline with CDK & Lambda</h1>

<p align="center">
  <b>Automated CI/CD pipeline for deploying AWS resources using AWS CDK (TypeScript) and Python Lambda</b> <br>
  <i>Deployed using GitHub Actions (deploy_beta.yml)</i> ✅
</p>

---

<h2>📌 Project Overview</h2>

<ul>
  <li>🔹 Uses <b>AWS CDK</b> with <b>TypeScript</b> for infrastructure as code.</li>
  <li>🐍 Implements <b>AWS Lambda</b> in <b>Python</b> (main.py).</li>
  <li>⚡ Automates deployment with <b>GitHub Actions</b> (<code>deploy_beta.yml</code>).</li>
  <li>🎯 Deploys resources to AWS in a seamless, scalable manner.</li>
</ul>

---

<h2>📂 Project Structure</h2>

```sh
📦 aws-cicd-project
├── 📂 cdk-app/            # AWS CDK TypeScript project
│   ├── bin/              # CDK entry point
│   ├── lib/              # CDK stack definition
│   ├── cdk.json          # CDK configuration
│   ├── package.json      # Dependencies
│   └── tsconfig.json     # TypeScript config
│
├── 📂 lambda/             # AWS Lambda functions
│   ├── main.py           # Python Lambda function
│   ├── requirements.txt  # Lambda dependencies
│
├── 📂 .github/workflows/  # CI/CD workflows
│   ├── deploy_beta.yml   # GitHub Actions workflow for deployment
│
└── README.md             # This file 📜

<h2>⚙️ Installation & Setup</h2> <h3>🔧 Prerequisites</h3> <ul> <li>Install <b>Node.js</b> and <b>TypeScript</b> (for CDK): <code>npm install -g typescript aws-cdk</code></li> <li>Install <b>Python</b> and dependencies: <code>pip install -r lambda/requirements.txt</code></li> <li>Ensure <b>AWS CLI</b> is configured: <code>aws configure</code></li> <li>Authenticate AWS CDK: <code>cdk bootstrap</code></li> </ul> <h3>🚀 Deploying the App</h3>
# Install dependencies
npm install

# Deploy with AWS CDK
cdk synth
cdk deploy

<h2>🚀 GitHub Actions CI/CD Workflow</h2> <p> This project includes an automated deployment workflow: <code>.github/workflows/deploy_beta.yml</code>. </p> <ul> <li>🔄 Triggers on every <b>push</b> to the <code>main</code> branch.</li> <li>🔧 Runs tests and builds the CDK app.</li> <li>🚀 Deploys to AWS automatically.</li> </ul> <p><b>To trigger a manual deployment:</b></p>
git push origin main

<h2>🎯 AWS Services Used</h2> <ul> <li>✅ <b>AWS CDK</b> - Infrastructure as Code</li> <li>✅ <b>AWS Lambda</b> - Serverless Function</li> <li>✅ <b>AWS CloudFormation</b> - Stack Management</li> <li>✅ <b>Amazon S3</b> - Storage (if applicable)</li> <li>✅ <b>Amazon API Gateway</b> - API Deployment (if applicable)</li> </ul>
<h2>📜 Contributing</h2> <p> Contributions are welcome! To contribute: </p>

<h2>📄 License</h2> <p>This project is licensed under the <b>MIT License</b>. Feel free to use and modify!</p>
<h2>💬 Contact</h2> <p> If you have any questions or suggestions, feel free to reach out! 😊<br> 📧 Email: your.email@example.com <br> 🌍 GitHub: <a href="https://github.com/yourusername">yourusername</a> </p>
