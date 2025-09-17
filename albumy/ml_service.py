import requests
import json
from albumy.api_config import VISION_API_KEY, VISION_API_ENDPOINT


def analyze_image(image_path):
    """
    Analyze image using Azure Computer Vision API
    Returns dict with description and tags
    """
    headers = {
        "Ocp-Apim-Subscription-Key": VISION_API_KEY,
        "Content-Type": "application/octet-stream",
    }

    params = {"visualFeatures": "Description,Tags", "details": "", "language": "en"}

    try:
        with open(image_path, "rb") as image_data:
            response = requests.post(
                f"{VISION_API_ENDPOINT}/vision/v3.2/analyze",
                headers=headers,
                params=params,
                data=image_data,
                timeout=30,
            )

        if response.status_code == 200:
            result = response.json()

            # Extract description for alt text
            alt_text = ""
            if "description" in result and result["description"]["captions"]:
                alt_text = result["description"]["captions"][0]["text"]

            # Extract tags for search
            tags = []
            if "tags" in result:
                tags = [
                    tag["name"] for tag in result["tags"] if tag["confidence"] > 0.5
                ]

            return {"success": True, "alt_text": alt_text, "tags": tags}
        else:
            return {"success": False, "error": "API call failed"}

    except Exception as e:
        return {"success": False, "error": str(e)}
