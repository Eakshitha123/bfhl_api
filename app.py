from flask import Flask, request, jsonify

app = Flask(__name__)

# YOUR DETAILS
FULL_NAME = "eakshitha"          # lowercase full name
DOB = "16062005"                 # ddmmyyyy
EMAIL = "eakshitha2005@gmail.com"
ROLL_NUMBER = "22bps1184"

@app.route('/bfhl', methods=['POST'])
def bfhl():
    try:
        data = request.json.get("data", [])

        even_numbers, odd_numbers, alphabets, special_chars = [], [], [], []
        total_sum = 0

        for item in data:
            if item.isdigit():
                num = int(item)
                total_sum += num
                if num % 2 == 0:
                    even_numbers.append(item)
                else:
                    odd_numbers.append(item)
            elif item.isalpha():
                alphabets.append(item.upper())
            else:
                special_chars.append(item)

        # Reverse all letters and alternate caps
        combined_letters = "".join(alphabets)
        rev = combined_letters[::-1]
        concat_str = "".join(ch.upper() if i%2==0 else ch.lower() for i,ch in enumerate(rev))

        response = {
            "is_success": True,
            "user_id": f"{FULL_NAME}_{DOB}",
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_chars,
            "sum": str(total_sum),
            "concat_string": concat_str
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
