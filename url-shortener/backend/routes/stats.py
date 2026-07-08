from flask import Blueprint, jsonify

from db import get_statistics

stats_bp = Blueprint("stats", __name__)


@stats_bp.route("/api/stats/<short_code>", methods=["GET"])
def statistics(short_code):

    result = get_statistics(short_code)

    if result is None:
        return jsonify({
            "error": "Short URL not found"
        }), 404

    return jsonify({
        "id": result[0],
        "original_url": result[1],
        "short_code": result[2],
        "click_count": result[3],
        "created_at": result[4]
    })
