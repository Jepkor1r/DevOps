from flask import Flask, jsonify
from flask_cors import CORS
import requests  # Import requests to fetch external data (numbersapi.com)

app = Flask(__name__)
CORS(app)

@app.route('/')
@app.route('/api/classify-number/<int:num>', methods=['GET'])
def number(num):
    try:
        # Fetch a fun fact about the number from numbersapi.com
        fun_fact_response = requests.get(f"http://numbersapi.com/{num}?json")

        # If the request to numbersapi fails, return an error
        if fun_fact_response.status_code != 200:
            return jsonify({"error": "Unable to fetch fun fact for the number."}), 400 

        fun_fact = fun_fact_response.json().get("text", "No fun fact available.")

        # Check if the number is an Armstrong number and get properties
        properties = classify_number(num)

        # Prepare the final output
        return jsonify({
            "number": num,
            "is_prime": is_prime(num),
            "is_perfect": is_perfect_square(num),
            "properties": properties,
            "digit_sum": digit_sum(num), 
            "fun_fact": fun_fact
        })

    except Exception as e:
        return jsonify({"error": "Internal server error", "message": str(e)}), 500

# Helper function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Helper function to check if a number is a perfect square
def is_perfect_square(n):
    return (n ** 0.5).is_integer()

# Helper function to determine number properties (Armstrong + Odd/Even)
def classify_number(n):
    digits = [int(digit) for digit in str(n)]
    num_digits = len(digits)
    armstrong_value = sum(d ** num_digits for d in digits)

    properties = []
    if armstrong_value == n:
        properties.append("armstrong")

    if n % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")

    return properties  # Always returns at least ["even"] or ["odd"]

# Helper function to compute the digital sum of a number
def digit_sum(n):
    return sum(int(digit) for digit in str(n))

if __name__ == '__main__':
    app.run(debug=True)