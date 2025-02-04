# import streamlit as st
# from llm_chain import ask_ai

# # Set page configuration
# st.set_page_config(
#     page_title="Medical GPT: Medi 🤖|🩺",
#     page_icon="🩺",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # Sidebar with logo and description
# with st.sidebar:
#     st.image("medilogo.webp", width=150)  # Replace with your logo URL
#     st.title("Medical GPT: Medi 🤖|🩺")
#     st.markdown("Your AI-powered assistant for medical queries.")
#     st.markdown("---")
#     st.markdown(
#         "💡 **Tip:** Try asking detailed medical questions for better responses!"
#     )

# # Main title and description
# st.title("Welcome to **Medical GPT: Medi 🤖|🩺**")
# st.markdown(
#     """
#     <style>
#     .big-font {
#         font-size:18px;
#         font-weight: bold;
#         color: #007BFF;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )
# st.markdown('<p class="big-font">Your virtual assistant for medical solutions!</p>', unsafe_allow_html=True)

# # Model selection
# st.subheader("Model Selection")
# col1, col2 = st.columns([1, 3])  # Adjust column widths for balance
# with col1:
#     llm_name = st.radio(
#         "Choose your Model",
#         ["4o", "4o-mini"],
#         help="Select the AI model to generate responses."
#     )

# # User input and response generation
# st.subheader("Interact with Medi 🤖")
# with st.form("my_form"):
#     text = st.text_area(
#         "Enter your query below:",
#         "What are your duties as a doctor?",
#         height=150
#     )
#     submitted = st.form_submit_button("Submit")
#     if submitted:
#         with st.spinner("Generating response..."):
#             response = ask_ai(
#                 query=text,
#                 model_name=llm_name
#             )
#         st.success("Response generated!")
#         st.write(response)

# # Footer
# st.markdown("---")
# st.markdown(
#     "Developed with ❤️ by [Abdul Wassay] | Powered by AI"
# )


# from flask import Flask, render_template, request, jsonify
# from flask import send_file
# from llm_chain import ask_ai
# import os

# app = Flask(__name__)

# # Load the logo image (assuming it is in the static folder)
# @app.route('/logo')
# def logo():
#     return send_file('static/medilogo.webp', mimetype='image/webp')

# # Home page
# @app.route('/')
# def home():
#     return render_template('index.html')

# # API endpoint to handle user queries
# @app.route('/ask_ai', methods=['POST'])
# def ask_ai_endpoint():
#     data = request.json
#     query = data['query']
#     model_name = data['model_name']
#     response = ask_ai(query=query, model_name=model_name)
#     return jsonify({'response': response})

# if __name__ == '__main__':
#     app.run(debug=True)

#----------------------------------------------

from flask import Flask, render_template, request
from llm_chain import ask_ai  # Ensure your 'ask_ai' function is imported here

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    llm_name = request.form.get('llm_name')  # Get selected model
    text = request.form.get('text')  # Get user query
    
    # Check if the form was submitted
    if llm_name and text:
        # Generate response using the ask_ai function
        response = ask_ai(query=text, model_name=llm_name)
        return render_template('index.html', response=response)
    
    # If no input, just render the page without response
    return render_template('index.html', response=None)

if __name__ == '__main__':
    app.run(debug=True)
