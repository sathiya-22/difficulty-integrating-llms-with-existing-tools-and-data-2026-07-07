import google.generativeai as genai
from config import settings
from pydantic import ValidationError

# Configure the generative AI model
try:
    genai.configure(api_key=settings.api_key.get_secret_value())
except ValidationError as e:
    print(f"Configuration Error: {e}")
    print("Please ensure GEMINI_API_KEY environment variable is set.")
    exit(1)
except Exception as e:
    print(f"An unexpected error occurred during configuration: {e}")
    exit(1)


def simulate_read_document(file_path: str) -> str:
    """
    Simulates reading content from a document.
    In a real application, this would use libraries like python-docx, openpyxl, etc.
    For this prototype, it returns a hardcoded string.
    """
    print(f"Simulating reading document from: {file_path}")
    # Hardcoded content for demonstration
    return """
    The quarterly financial report for Q1 2024 shows a 15% increase in revenue compared to the previous quarter, reaching $1.2 million.
    Net profit also saw a significant boost, up by 20% to $350,000, primarily driven by successful product launches and
    optimized operational costs. Employee satisfaction surveys indicate a positive trend, with 85% of staff reporting high
    job satisfaction. The company plans to expand into new markets in Q3, focusing on Southeast Asia.
    """

def summarize_document_with_llm(document_content: str) -> str:
    """
    Uses the Gemini LLM to summarize the provided document content.
    """
    model = genai.GenerativeModel('gemini-pro')
    prompt = f"""
    Please summarize the following document content concisely, highlighting key financial figures,
    operational achievements, and future plans.

    Document Content:
    ---
    {document_content}
    ---

    Summary:
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating summary: {e}"

if __name__ == "__main__":
    document_path = "reports/Q1_2024_Financial_Report.docx"
    content = simulate_read_document(document_path)

    print("\n--- Document Content ---")
    print(content)

    print("\n--- Generating Summary with LLM ---")
    summary = summarize_document_with_llm(content)

    print("\n--- LLM Generated Summary ---")
    print(summary)
