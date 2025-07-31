def build_prompt(position, location, tech_list):
    prompt = f"""
You are an AI Hiring Assistant interviewing a candidate for the position of {position} based in {location}.
Now generate 5 short technical interview questions for each of the following skills: {', '.join(tech_list)}.
Avoid repetition and keep the questions concise.
"""
    return prompt
