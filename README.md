# Devrev-CodeHermit
# Image Denoising Website

This is a Django-based web application for image denoising. It provides a user interface for uploading images and applying denoising algorithms to remove noise and enhance the image quality.

## Prerequisites

- Python 3.x
- Django
- Virtual Environment (recommended)

## Setup

1. Clone the repository:

```bash
git clone https://github.com/rameshgitter/Devrev-CodeHermit/tree/main/image_denoising_website
```
2. Navigate to the project directory:
``` bash
cd image-denoising-website
```
3. Create a virtual environment (optional but recommended):
``` bash
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
```
4. Install the required dependencies:
``` bash
pip install -r requirements.txt
```
But how would you know what are requirements.txt?
``` bash
pip install pipreqs
pipreqs
```
5. Apply database migrations:
``` bash
python manage.py migrate
```
6. Start the development server:
``` bash
python manage.py runserver
```
The application should now be running at http://localhost:8000/.

## Usage
1. Visit http://localhost:8000/ in your web browser.
2. Upload an image file for denoising.
3. Select the desired denoising algorithm and options.
4. Click the "Denoise" button to process the image.
5. View the denoised image and download it if needed.
## Contributing
Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch: git checkout -b my-new-feature
3. Make your changes and commit them: git commit -am 'Add some feature'
4. Push to the branch: git push origin my-new-feature
5. Submit a pull request

## License
This project is licensed under the MIT License.

##  Acknowledgments
1. Django - The web framework used
2. example-denoising-library - Denoising algorithms used in this project

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
This repo was originally developed to make a product regarding the following but it halted.
Crack the Multi-Channel Voice of Customer (VoC) data conundrum using LLMs.
In today's digital landscape, customer feedback and sentiments are dispersed across various channels such as LinkedIn, WhatsApp, Twitter, Email, App Reviews, Instagram, Facebook, and more. Collating this Voice of Customer (VoC) data is pivotal for organizations to understand customer needs, pain points, and preferences.

However, the diverse sources and unstructured nature of this data pose challenges in processing, denoising, and extracting actionable insights effectively.

The challenge is to develop an AI-powered solution that uses snap-ins to seamlessly aggregate VoC data from multiple channels. This solution should leverage the capabilities of the DevRev platform, utilizing its APIs for data ingestion and an omnichannel inbox for displaying actionable items to internal teams.
