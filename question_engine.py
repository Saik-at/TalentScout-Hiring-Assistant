def generate_response(prompt):
    prompt_lower = prompt.lower()

    if "python" in prompt_lower:
        return """1. What are Python's key data types?
2. Explain the difference between a list and a tuple.
3. How does Python manage memory and garbage collection?
4. What are decorators and how are they used?
5. Explain Python’s lambda functions with an example."""

    elif "sql" in prompt_lower:
        return """1. What is the difference between WHERE and HAVING clause?
2. Explain different types of JOINs in SQL.
3. How do you retrieve the second highest salary in a table?
4. What is a subquery and how is it used?
5. What is the difference between DELETE and TRUNCATE?"""

    elif "power bi" in prompt_lower:
        return """1. What are the key components of Power BI?
2. What is DAX and how is it used in Power BI?
3. Explain the difference between a calculated column and a measure.
4. How do relationships work in Power BI data models?
5. What are slicers and filters in Power BI dashboards?"""

    else:
        return """1. Describe the core concepts of this technology.
2. What is one real-world application of it?
3. What are its advantages and limitations?
4. How does it integrate with other tools?
5. How would you troubleshoot common issues?"""
