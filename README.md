# SMS Alerting Integration for Monitoring Systems

## Overview

This is a serverless solution designed to seamlessly integrate SMS alerting with various monitoring systems. It's powered by AWS Lambda, API Gateway, and the Clickatell SMS Gateway Platform.

## Features

- Integration with common monitoring systems for SMS alerts.
- Serverless design for cost efficiency and scalability.
- AWS Lambda functions for event-triggered alert processing.
- Works with Clickatell SMS Gateway for reliable SMS delivery.

## Prerequisites

Before deploying, make sure you have:

- An AWS account with permissions for Lambda and API Gateway.
- Clickatell account with API credentials.
- Configuration details for your specific monitoring systems.

## Setup Instructions

1. **AWS Lambda Setup:**
   - Create a new Lambda function in your AWS account.
   - Configure the function with the code in the `lambda` directory.
   - Set environment variables for necessary credentials and configurations.

2. **API Gateway Configuration:**
   - Create a new API Gateway in AWS.
   - Configure the API with endpoints and link it to the Lambda function.

3. **Clickatell SMS Gateway Integration:**
   - Obtain API credentials from Clickatell.
   - Update Lambda function environment variables with Clickatell API details.

4. **Monitoring System Integration:**
   - Follow your monitoring system's documentation to set up custom alert notifications.
   - Configure the notification endpoint to the API Gateway URL.

5. **Deployment:**
   - Deploy the Lambda function and API Gateway configuration.
   - Test by triggering test alerts in your monitoring system.

## Configuration

Modify the `config.js` file for specific configurations, like AWS region, Clickatell API credentials, and logging preferences.

## Usage

After deployment:

1. Alerts triggered in your monitoring system will be sent to the API Gateway endpoint.
2. AWS Lambda processes alerts and sends SMS notifications using Clickatell.

## Contributing

Feel free to contribute—submit bug reports, feature requests, or make a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
