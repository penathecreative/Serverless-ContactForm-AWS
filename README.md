# 📬 Serverless Contact Form Using AWS DynamoDB, Lambda, and API Gateway

![Demo of the contact form](assets/demo.gif)

This project creates a fully functional contact form using a **React frontend** and **serverless backend** with **AWS Lambda**, **DynamoDB**, and **API Gateway**.

---

## 📌 Features

### ✅ Frontend (React)

- User-friendly form for name, email, and message.
- Submits data securely via API Gateway.

### ✅ Backend (AWS)

- **Lambda (Python)**: Processes and stores data.
- **DynamoDB**: Stores submissions.
- **API Gateway**: Publicly accessible endpoint with CORS enabled.

---

## 🛠️ AWS Setup

### 1️⃣ Create DynamoDB Table

| Field         | Value         |
| ------------- | ------------- |
| Table Name    | `ContactForm` |
| Partition Key | `form_id`     |
| Type          | `String`      |

> Go to **DynamoDB → Create Table**  
> Add `form_id` as the **Partition Key**

---

### 2️⃣ Create Lambda Function

1. Go to **AWS Lambda → Create function** → “Author from scratch”
2. Runtime: `Python 3.8+`
3. IAM Role: Choose or create a role with **AmazonDynamoDBFullAccess**
4. Paste this code:

```python
import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ContactForm')

def lambda_handler(event, context):
    try:
        body = json.loads(event["body"]) if isinstance(event["body"], str) else event["body"]
        body["form_id"] = str(uuid.uuid4())
        table.put_item(Item=body)

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Data stored successfully!",
                "form_id": body["form_id"]
            }),
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            }
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)}),
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            }
        }
```

### 3️⃣ API Gateway

- Create REST API.

- Add POST /submit endpoint linked to Lambda.

- Enable CORS.

- Deploy and copy the API URL.

### 🎨 React Frontend Setup

1. Create Project

```js
const response = await fetch(
  "https://your-api-id.execute-api.region.amazonaws.com/submit",
  {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(formData),
  }
);
```

2. Install dependencies and run the app

```bash
npm install
npm start
```

### 🚀 Deployment

- Frontend: Deploy with Vercel, Netlify, or AWS S3.

- Backend: Confirm Lambda, API Gateway, and DynamoDB are live.

- Test end-to-end: submit form → check DynamoDB.

### ✅ Real-World Use Case

- Use this for:

- Client portfolios

- SaaS app contact support

- Feedback systems

- Job applications

### 📚 Resources

- AWS Lambda Docs

- API Gateway Docs

- DynamoDB Docs

- React Docs
