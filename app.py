from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])

def index():
    '''Function to handle string manipulation requests'''
    result = None
    original_text = ""
    operation = "uppercase"

    if request.method == "POST":
        original_text = request.form.get("text", "")
        operation = request.form.get("operation", "uppercase")

    if operation == "uppercase":
        result = original_text.upper()
    elif operation == "lowercase":
        result = original_text.lower()
    elif operation == "reverse":
        result = original_text[::-1]
    elif operation == "count":
        chars = len(original_text)
        words = len(original_text.split())
        result = (
          f"Character count: {chars} | Word count: {words}"
          if original_text.strip()
          else "Character count: 0 | Word count: 0"
      )
    elif operation == "palindrome":
        cleaned = "".join(ch.lower() for ch in original_text if ch.isalnum())
        is_pal = cleaned == cleaned[::-1] and len(cleaned) > 0
        result = (
          "Yes, it's a palindrome!" if is_pal else "No, it's not a palindrome."
      )

    return render_template(
      "index.html",
      result=result,
      original_text=original_text,
      operation=operation,
  )


if __name__ == "__main__":
    app.run(debug=True)