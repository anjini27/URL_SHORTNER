from flask import Blueprint, request, jsonify

from db import insert_url, update_short_code
from base62 import encode

shorten_bp = Blueprint("shorten", __name__)


@shorten_bp.route("/api/shorten", methods=["POST"])
def shorten_url():

    data = request.get_json()

    if not data:
        return jsonify({"error": "No JSON data provided"}), 400

    if "url" not in data:
        return jsonify({"error": "URL field is missing"}), 400

    original_url = data["url"]

    if original_url.strip() == "":
        return jsonify({"error": "URL cannot be empty"}), 400

    # Step 1: Insert URL
    url_id = insert_url(original_url)

    # Step 2: Generate Base62 code
    short_code = encode(url_id)

    # Step 3: Store short code
    update_short_code(url_id, short_code)

    # Step 4: Return response
    return jsonify({
        "id": url_id,
        "original_url": original_url,
        "short_code": short_code,
        "short_url": f"http://localhost:5000/{short_code}"
    })
