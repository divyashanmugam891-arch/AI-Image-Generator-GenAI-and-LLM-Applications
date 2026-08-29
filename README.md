# AI Image Generator

A simple web-based AI Image Generator built using **Python, Streamlit, Hugging Face Diffusers, and PyTorch**.

This application allows the user to enter a text prompt and generate an AI image based on the given prompt.

##  About the Project

The main purpose of this project is to understand how **Text-to-Image AI generation** works.

The application uses the **Stable Diffusion Turbo (SD-Turbo)** model from Hugging Face. Streamlit is used to create a simple and interactive web interface.

The user can enter any text prompt, and the AI model generates an image based on the prompt.

## Features

-  User can enter a text prompt
-  Generates an AI image from the prompt
-  Uses a pretrained text-to-image model
-  Uses SD-Turbo for faster image generation
-  Simple Streamlit interface
-  Shows a loading message while generating
-  Displays the generated image
-  Supports CPU and CUDA devices
-  Shows a warning when no prompt is entered
-  Model caching for faster interaction

##  Technologies Used

- **Python**
- **Streamlit**
- **Hugging Face Diffusers**
- **PyTorch**
- **SD-Turbo**

##  How It Works

The application works in the following steps:

1. The user enters a text prompt.
2. Streamlit receives the prompt.
3. The application loads the SD-Turbo model.
4. The model processes the prompt.
5. The AI generates an image.
6. The generated image is displayed in the application.

##  Workflow

```text
User Enters Prompt
        ↓
Streamlit Receives Prompt
        ↓
SD-Turbo Model
        ↓
AI Image Generation
        ↓
Generated Image
        ↓
Image Displayed in Streamlit
```

##  Model

This project uses:

**stabilityai/sd-turbo**

The model is loaded using the Hugging Face Diffusers `DiffusionPipeline`:

```python
pipe = DiffusionPipeline.from_pretrained(
    "stabilityai/sd-turbo",
    torch_dtype=torch.float32
)
```

When CUDA is available, the application uses:

```python
torch_dtype=torch.float16
```

This helps the application use the available computing device.

##  Installation

Make sure Python is installed on your computer.

Install the required packages using:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file contains:

```text
streamlit
diffusers
torch
```

##  Running the Application

The Python file is saved as:

```text
imagegen.py
```

Open the terminal in the project folder and run:

```bash
streamlit run imagegen.py
```

The application will normally open at:

```text
http://localhost:8501
```

##  Example

Enter a prompt such as:

```text
A cute cat sitting in a beautiful garden
```

Then click:

** Generate Image**

The AI model will generate an image based on the given prompt.

##  Project Structure

```text
AI-Image-Generator-GenAI-and-LLM-Applications/
│
├── imagegen.py
├── README.md
├── requirements.txt
│
└── image_gen/
    │
    ├── imggen.PNG
    ├── imggen1.PNG
    ├── imggen2.PNG
    ├── imggen3.PNG
    ├── imggen4.PNG
    └── imggen5.PNG
```

##  What I Learned

Through this project, I learned about:

- Text-to-image generation
- Pretrained AI models
- Hugging Face Diffusers
- Streamlit application development
- Using PyTorch with AI models
- Using user input for AI image generation
- CPU and CUDA device handling
- Connecting an AI model to a web interface

##  Note

The generated image may vary depending on the prompt and the model.

The generation speed may also depend on the available hardware, especially whether the application is running on CPU or CUDA.

This project is mainly created for learning and demonstration purposes.

##  Possible Improvements

The application can be extended by adding:

- Image download option
- Image size selection
- Number of inference steps control
- Different AI model selection
- Image generation history
- More advanced prompt controls
- Negative prompt support

##  Conclusion

This project demonstrates how a pretrained text-to-image AI model can be connected to a simple Streamlit web application.

It provides an easy way for users to enter a prompt and generate an AI image.
