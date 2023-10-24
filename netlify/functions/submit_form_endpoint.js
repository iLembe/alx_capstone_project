// netlify/functions/submit_form_endpoint.js

exports.handler = async (event, context) => {
    // Your code to handle form submissions goes here
    return {
      statusCode: 200,
      body: JSON.stringify({ message: 'Form submitted successfully' }),
    };
  };
  