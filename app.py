from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = "OPENAI_API_KEY"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    job_role = request.form.get('job_role')
    
    # Prompt to generate questions and answers
    prompt = f"""
    Generate 5 common interview questions for a {job_role}. Provide ideal sample answers for each question.
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that generates interview questions and answers."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500
        )

        # Parse the response
        content = response['choices'][0]['message']['content']
        return render_template('results.html', job_role=job_role, content=content)
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True)
