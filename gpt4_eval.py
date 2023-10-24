import openai

# Initialize the OpenAI API
openai.api_key = 'api-key'

def evaluate_answer_with_gpt4(question, answer):
    # Define the prompt for suitability for the age group
    suitability_prompt = f"Given the answer '{answer}' to the question '{question}', rate its suitability for the target age group on a scale of 1 to 10."
    suitability_response = openai.ChatCompletion.create(
      model="gpt-4-0613",  # Use the appropriate engine or model name for GPT-4
      messages=[{"role": "system", "content": suitability_prompt}],
      max_tokens=50
    )
    suitability_score = int(suitability_response['choices'][0]['message']['content'].strip())

    # Define the prompt for information content usefulness
    usefulness_prompt = f"Given the answer '{answer}' to the question '{question}', rate its information content usefulness on a scale of 1 to 10."
    usefulness_response = openai.ChatCompletion.create(
      model="gpt-4-0613",  # Use the appropriate engine or model name for GPT-4
      messages=[{"role": "system", "content": usefulness_prompt}],
      max_tokens=50
    )
    usefulness_score = int(usefulness_response['choices'][0]['message']['content'].strip())

    return suitability_score, usefulness_score

def evaluate_question_answer_pairs(pairs):
    evaluations = []
    for pair in pairs:
        question, answer = pair
        suitability_score, usefulness_score = evaluate_answer_with_gpt4(question, answer)
        evaluations.append((question, answer, suitability_score, usefulness_score))
    return evaluations

if __name__ == "__main__":

    pairs = [
        ("What's the capital of France?", "Paris"),
        ("Who wrote 'Romeo and Juliet'?", "William Shakespeare")
        # ... add more pairs
    ]

    evaluations = evaluate_question_answer_pairs(pairs)
    for eval in evaluations:
        question, answer, suitability_score, usefulness_score = eval
        print(f"Question: {question}")
        print(f"Answer: {answer}")
        print(f"Suitability for Age Group: {suitability_score}/10")
        print(f"Information Content Usefulness: {usefulness_score}/10")
        print('-'*50)
