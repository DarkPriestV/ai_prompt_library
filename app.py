import streamlit as st
from utils.llm import generate_response
from utils.storage import load_prompts, save_prompt

st.set_page_config(page_title="AI Prompt Library", layout="wide")

st.title("Dark Priest AI Model")

# --- Input Section ---
prompt = st.text_area("Enter your prompt", height=150)

col1, col2 = st.columns(2)

with col1:
    generate_btn = st.button("🚀 Generate")

with col2:
    save_btn = st.button("💾 Save Prompt")

# --- Generate Response ---
if generate_btn and prompt:
    output = generate_response(prompt)

    st.subheader("🤖 Response")
    st.write(output)

    st.session_state["last_prompt"] = prompt
    st.session_state["last_output"] = output

# --- Save Prompt ---
if save_btn:
    if "last_prompt" in st.session_state:
        save_prompt({
            "prompt": st.session_state["last_prompt"],
            "response": st.session_state["last_output"]
        })
        st.success("✅ Prompt saved!")
    else:
        st.warning("Generate something first!")

# --- Display Saved Prompts ---
st.divider()
st.subheader("📚 Saved Prompts")

prompts = load_prompts()

for i, p in enumerate(prompts[::-1]):
    with st.expander(f"Prompt {len(prompts)-i}"):
        st.write("**Prompt:**", p["prompt"])
        st.write("**Response:**", p["response"])