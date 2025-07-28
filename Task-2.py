def load_llm_output(file_path="output.txt"):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        print("output.txt not found.")
        return ""

def save_combined_prompt(text, file_path="output.txt"):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)

def main():
    combined_prompt = load_llm_output()
    if not combined_prompt:
        combined_prompt = input("Enter your initial prompt: ")
        save_combined_prompt(combined_prompt)

    while True:
        new_prompt = input("\nEnter a new prompt (or type 'exit' to quit): ")
        if new_prompt.lower() == "exit":
            break
        combined_prompt = new_prompt + combined_prompt
        save_combined_prompt(combined_prompt)
        print("\nUpdated combined prompt:")
        print(combined_prompt)

if __name__ == "__main__":
    main()

