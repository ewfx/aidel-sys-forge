# Load model directly
from huggingface_hub import hf_hub_download
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from constants import hugg_sk

tokenizer = AutoTokenizer.from_pretrained("/home/oracle/repos/aidel-sys-forge/code/src/backend/apiHandler/lib/model/LLM/Llama-3.2-1B-Instruct/")
model = AutoModelForCausalLM.from_pretrained("/home/oracle/repos/aidel-sys-forge/code/src/backend/apiHandler/lib/model/LLM/Llama-3.2-1B-Instruct/")

messages = [
    {"role": "user", "content": "Given the below text regarding a financial transaction, extract the following parameters and return them to me as a JSON object. The parameters necessary are: Transaction ID, Date, Amount, Transaction Type, Sender Name, Sender Account, Sender Address, Sender Notes, Receiver Name, Receiver Account, Receiver Address, Receiver Notes, Additional Notes. The parameters can also be empty. But all parameters should be present in the output JSON"},
    {"role": "user", "content": """
Transaction ID: TXN-2023-5A9B
Date: 2023-08-15 14:22:00
Sender: {
Name: "Global Horizons Consulting LLC"
Account: IBAN CH56 0483 5012 3456 7800 9 (Swiss bank)
Address: Rue du Marché 17, Geneva, Switzerland
Notes: "Consulting fees for project Aurora"
}

Receiver:{
Name: "Bright Future Nonprofit Inc" Account: 987654321 (Cayman National Bank, KY)
Address: P.O. Box 1234, George Town, Cayman Islands
}

Tax ID: KY-45678
Amount: $49,850.00 (USD)
Currency Exchange: N/A
Transaction Type: Wire Transfer
Reference: "Charitable Donation Ref #DR-2023-0815"
Additional Notes:{
"Urgent transfer approved by Mr. Ali Al-Mansoori (Director)."
"Linked invoice missing. Processed via intermediary Quantum Holdings Ltd (BVI)."
Bender IP: 192.168.89.123 (VPN detected: NordVPN, exit node in Panama)
}

"""},
]

pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)
output = pipe(messages1)
print(output)
output = pipe(messages2)
print(output)