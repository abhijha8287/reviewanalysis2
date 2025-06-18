# 🧠 Enhanced Review Analysis Bot

This Streamlit app uses **OpenAI GPT-4 + LangChain** with **Pydantic schema validation** to analyze user reviews in a **structured, accurate, and clean format**. It extracts detailed insights like sentiment, pros/cons, key themes, a summary, and even the **reviewer’s name** if present.

🔗 **Live Demo**: [https://reviewanalysis2byabhishek.streamlit.app/](https://reviewanalysisbyabhishek.streamlit.app/)

> ⚠️ If the app is inactive or "asleep", Streamlit may take a few seconds to wake it up. Just click or refresh once to activate.

---

## 🚀 What's New Compared to the Previous Version?

✅ **Pydantic Model for Schema**  
- Uses `pydantic.BaseModel`  to define strict, validated structured output.
- Adds descriptions for each field (better prompt clarity).
  
✅ **Reviewer Name Extraction**  
- Detects and extracts reviewer’s name (if mentioned in the text).

✅ **Better Prompt Reliability**  
- The `Field()` annotations help GPT-4 generate **cleaner**, more **reliable**, and **typed outputs**.
- Supports optional fields (`Pros`, `Cons`, and `Name`) gracefully.

✅ **Code Fixes**  
- Changed the incorrect class name reference from `Review` to `Student` in `model.with_structured_output(...)`.

✅ **Cleaner Output Display**  
- Designed to be more user-friendly with explicit structure using Streamlit's output area.

---

## 💬 What This App Does

Just enter a review and the app intelligently returns:

- 🎯 **Sentiment**: `Positive`, `Negative`, or `Neutral`
- 🔍 **Key Themes**: List of major points discussed
- ✅ **Pros**: What was liked
- ❌ **Cons**: What was disliked
- 🧾 **Summary**: A short, natural language explanation
- 🧑 **Name** *(New)*: Extracts reviewer’s name if found

---

