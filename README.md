# Content Management API

## Overview

This document outlines the API for managing content within a MongoDB database using asynchronous operations. The API allows for retrieving, adding, updating, and deleting content within specified collections.

## Base URL

The base URL for the API is: `http://<your-api-hostname>:<port>`

Replace `<your-api-hostname>` and `<port>` with your actual API hostname and port number.

## API Endpoints

All API endpoints are prefixed with `/api/content`.

### GET Endpoints

#### Retrieve Content by ID
GET /api/content/id/{collection}/{_id}

Retrieves the content with the specified _id from the collection.

**Parameters:**

- `collection` (string) - The name of the collection.
- `_id` (string) - The ObjectId of the content to retrieve.

**Response:**

A JSON object representing the content.

#### Retrieve Content by Path
GET /api/content/path/{collection}/{path}

Retrieves the content at the specified path within the collection.

**Parameters:**

- `collection` (string) - The name of the collection.
- `path` (string) - The path of the content to retrieve.

**Response:**

A JSON array of objects representing the content.

#### Retrieve All Content from a Collection
GET /api/content/collection/{collection}

Retrieves all content from the specified collection.

**Parameters:**

- `collection` (string) - The name of the collection to retrieve content from.

**Response:**

A JSON array of all objects within the collection.

### POST Endpoint

#### Add Content
POST /api/content/{collection}

Adds new content to the specified collection.

**Parameters:**

- `collection` (string) - The name of the collection to add content to.

**Request Body:**

A JSON object representing the content to add.

**Response:**

A JSON object with the result of the operation.

### PUT Endpoints

#### Update Content Text by ID
PUT /api/content/text/{collection}/{_id}

Updates the text of the content with the specified _id within the collection.

**Parameters:**

- `collection` (string) - The name of the collection.
- `_id` (string) - The ObjectId of the content to update.

**Request Body:**

A JSON object with the new text.

**Response:**

A JSON object with the result of the operation.

#### Update Content Path by ID
PUT /api/content/path/{collection}/{_id}

Updates the path of the content with the specified _id within the collection.

**Parameters:**

- `collection` (string) - The name of the collection.
- `_id` (string) - The ObjectId of the content to update.

**Request Body:**

A JSON object with the new path.

**Response:**

A JSON object with the result of the operation.

### DELETE Endpoints

#### Delete Content by ID
DELETE /api/content/id/{collection}/{_id}

Deletes the content with the specified _id from the collection.

**Parameters:**

- `collection` (string) - The name of the collection.
- `_id` (string) - The ObjectId of the content to delete.

**Response:**

A JSON object with the result of the operation.

#### Delete Content by Path
DELETE /api/content/path/{collection}/{path}

Deletes all content at the specified path within the collection.

**Parameters:**

- `collection` (string) - The name of the collection.
- `path` (string) - The path of the content to delete.

**Response:**

A JSON object with the result of the operation.

#### Delete a Collection
DELETE /api/content/collection/{collection}

Deletes the specified collection and all its contents.

**Parameters:**

- `collection` (string) - The name of the collection to delete.

**Response:**

A JSON object with the result of the operation.

## Usage

To use the API, make HTTP requests to the provided endpoints with the required parameters. Ensure that you have the necessary permissions and that your requests are authenticated, if required.

## Error Handling

The API will return appropriate HTTP status codes along with error messages in the response body, should any request fail due to client-side or server-side issues.

## License

Specify your license here.

## Contact

For any further questions or feedback, please contact [Your Contact Information].
You will need to fill in the placeholders with your actual data, such as <your-api-hostname> and <port>. Additionally, add your contact information and license details where indicated.