# backend/app/explain.py
import os
OPENAI_KEY = os.environ.get("OPENAI_API_KEY")

if OPENAI_KEY:
    import openai
    openai.api_key = OPENAI_KEY

def explain_with_openai(text: str, max_tokens: int = 200) -> str:
    prompt = (
        "You are an insurance assistant. Read the following claim/settlement text and give a short "
        "plain-language explanation (2-4 sentences). Keep it neutral and highlight key reasons for approval/denial.\n\n"
        f"Text:\n{text}\n\nExplanation:"
    )
    try:
        resp = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=0.2,
            top_p=1,
            n=1,
            stop=None
        )
        return resp.choices[0].text.strip()
    except Exception as e:
        return f"(explain_error) {str(e)}"

def rule_based_explain(doc_type: str, text: str) -> str:
    # useful fallback
    templates = {
        "Claim Document": "This appears to be a claim document — it likely contains policy and loss details. Check the deductible and approved amounts for settlement details.",
        "Invoice": "This appears to be an invoice listing parts or services billed for a repair or job.",
        "Inspection Report": "This is an inspection report containing findings about property or vehicle condition after an event.",
    }
    return templates.get(doc_type, "No detailed explanation available. Please review the document.")

def explain_text(doc_type: str, text: str) -> str:
    if OPENAI_KEY:
        return explain_with_openai(text)
    return rule_based_explain(doc_type, text)
