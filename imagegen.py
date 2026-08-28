import streamlit as st
from diffusers import DiffusionPipeline
import torch

st.set_page_config(
    page_title="AI Image Generator",
    page_icon="🎨"
)

st.title("🎨 AI Image Generator")
st.write("✨ Enter a prompt and generate an AI image!")

prompt = st.text_input(
    "Enter your prompt:",
)

@st.cache_resource
def load_model():

    device = "cuda" if torch.cuda.is_available() else "cpu"

    if device == "cuda":
        pipe = DiffusionPipeline.from_pretrained(
            "stabilityai/sd-turbo",
            torch_dtype=torch.float16
        )
    else:
        pipe = DiffusionPipeline.from_pretrained(
            "stabilityai/sd-turbo",
            torch_dtype=torch.float32
        )

    pipe = pipe.to(device)

    return pipe, device


if st.button("🎨 Generate Image"):

    if prompt:

        with st.spinner("🤖 Generating image..."):

            pipe, device = load_model()

            image = pipe(
                prompt,
                num_inference_steps=1,
                guidance_scale=0.0
            ).images[0]

        st.subheader("🖼️ Generated Image")
        st.image(image, caption="Generated Image")

    else:
        st.warning("⚠️ Please enter a prompt.")