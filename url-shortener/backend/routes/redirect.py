from cache import LRUCache

cache = LRUCache(capacity=100)

from flask import Blueprint, redirect, jsonify

from db import (
    get_url_by_short_code,
    increment_click_count
)
cache = LRUCache(capacity=100)

redirect_bp = Blueprint("redirect", __name__)

@redirect_bp.route("/<short_code>", methods=["GET"])
def redirect_url(short_code):

    # Check cache first
    cached_url = cache.get(short_code)

    if cached_url:
        increment_click_count(short_code)
        return redirect(cached_url)

    # Cache miss → check database
    original_url = get_url_by_short_code(short_code)

    if original_url is None:
        return jsonify({"error": "Short URL not found"}), 404

    # Store in cache
    cache.put(short_code, original_url)

    increment_click_count(short_code)

    return redirect(original_url)
