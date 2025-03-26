import json

def RawTextHandler(text: str) -> str:
    json_data = {"message": text}
    return json.dumps(json_data, indent=4)

# Example usage
if __name__ == "__main__":
    text = "Hello, this is a sample text!"
    json_output = RawTextHandler(text)
    print(json_output) 