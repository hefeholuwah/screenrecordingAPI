# Python on Replit

This is a template to get you started with Python on Replit. It's ready to go so you can just hit run and start coding!

## Running the repl

1. Setup a new secret environment variable (the lock icon) where the key is `SECRET_KEY` and the value is
   a randomly generated token of 32 bits of randomnese. To generate such a token type this into the shell and hit Enter:
```
python
import secrets
secrets.token_urlsafe(32)
```
2. Hit run!

See this 1 minute video for a walkthrough: [https://www.loom.com/share/ecc4e738149f4d1db3bcff01758b3e71](https://www.loom.com/share/341b5574d12040fb9fcbbff150777f1c)

## Installing packages

To add packages to your repl, you can just import directly in the file you want to use the package in, and it will automatically be installed when you press the run button. Like below:
```python
import math
import pandas as pd
```

You could also install packages by using the Replit packager interface in the left sidebar.

## Help

If you need help you might be able to find an answer on our [docs](https://docs.replit.com) page. Feel free to report bugs and give us feedback [here](https://replit.com/support).




# Screen Recordings App Documentation

## Overview

Welcome to the Screen Recordings app documentation. This documentation provides information on how to interact with the Screen Recordings API and how the frontend and backend components work together.

### Backend Overview

The backend of the Screen Recordings app is built using Django, a powerful Python web framework. It provides RESTful API endpoints for uploading and retrieving screen recordings.

Key components of the backend:
- Django Framework: Powers the API and handles database operations.
- Django Rest Framework (DRF): Extends Django to simplify API development.

### Frontend Overview

The frontend is responsible for interacting with users, including uploading and displaying screen recordings.

Key components of the frontend:
- HTML, CSS, and JavaScript: The core web technologies for building user interfaces.
- Fetch API: Used for making asynchronous requests to the backend.
- Form elements: Used for uploading screen recordings.

## API Endpoints

### Base URL

The base URL for the API is: `(https://screenrecording.ifeoluwaadefioy.repl.co/app/api/screen-recordings/)`

### Authentication

This API requires authentication. Please obtain an API token by contacting our support team.

#### Authentication Header Example:

```
Authorization: Token your-api-token-here
```

### Create a Screen Recording

To create a new screen recording, make a POST request to the following endpoint:

```
POST /screen-recordings/
```

**Request:**

- Method: POST
- URL: `(https://screenrecording.ifeoluwaadefioy.repl.co/app/api/screen-recordings/)`
- Headers: `Authorization: Token your-api-token-here`
- Body: JSON data containing title and the audio blob.

**Response:**

- Status Code: 201 (Created) if successful.
- Status Code: 400 (Bad Request) if there are validation errors.
- Status Code: 500 (Internal Server Error) if there is a server-side error.

### Get Screen Recordings

To retrieve a list of all screen recordings, make a GET request to the following endpoint:

```
GET /screen-recordings/
```

**Request:**

- Method: GET
- URL:(https://screenrecording.ifeoluwaadefioy.repl.co/app/api/screenrecordings/)
- Headers: `Authorization: Token your-api-token-here`

**Response:**

- Status Code: 200 (OK)
- Content Type: application/json
- Response Body: JSON array containing a list of screen recordings.

### Additional Features

## Frontend Integration

**Upload**

The Backend also supports integration with S3 buckets , you can upload your video file to s3 bucket using the form url 

URL: https://screenrecording.ifeoluwaadefioy.repl.co/app/upload/

