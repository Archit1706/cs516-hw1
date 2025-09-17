# Albumy with ML Features

_Capture and share every wonderful moment with AI-powered accessibility and search._

This enhanced version of Albumy includes:

-   **Auto-generated alt text** for uploaded images using Azure Computer Vision API
-   **AI-powered image search** using automatically detected tags

## Installation

### Prerequisites

-   Python 3.7+ (I used Python 3.9.0)
-   Azure Computer Vision API account

### Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/Archit1706/cs516-hw1.git
cd cs516-hw1
```

2. Create and activate virtual environment:

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set up Azure Computer Vision API:

    - Sign up for [Azure Cognitive Services](https://azure.microsoft.com/services/cognitive-services/)
    - Create a Computer Vision resource
    - Get your API key and endpoint
    - Create `albumy/api_config.py` with:

    ```python
    VISION_API_KEY = "your_api_key_here"
    VISION_API_ENDPOINT = "your_endpoint_here"
    ```

5. Initialize the database:

```bash
flask initdb --drop
flask forge  # Optional: add sample data
```

6. Run the application:

```bash
flask run
```

7. Access the application at http://127.0.0.1:5000

### Test Account

-   Email: admin@helloflask.com
-   Password: helloflask

## New ML Features

### Alternative Text Generation

-   Upload any image and it will automatically generate descriptive alt text
-   View the alt text by inspecting the HTML source of image elements
-   Improves accessibility for screen readers

### AI-Powered Image Search

-   Images are automatically tagged with detected objects
-   Search for images using keywords like "person", "car", "building", etc.
-   Uses the existing search functionality with AI-generated tags

## API Requirements

This application requires an active Azure Computer Vision API subscription. The free tier provides 5,000 API calls per month, which is sufficient for testing and development.

## License

This project is licensed under the MIT License (see the
[LICENSE](LICENSE) file for details).
