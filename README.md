
# ChatbotAI with Perplexity

A simple Python-based chatbot application using the Perplexity API. This chatbot engages in conversations and provides responses based on the prompt given by the user.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [Configuration](#configuration)
- [Example](#example)
- [License](#license)

## Overview
ChatbotAI with Perplexity is a lightweight chatbot built in Python that leverages the Perplexity API to generate conversational responses. It listens to user inputs and responds until the user decides to exit. This project serves as a great starting point for building more advanced chat applications with Perplexity's AI capabilities.

## Features
- Real-time conversation with the Perplexity API.
- Simple command-line interface.
- Easy to extend and customize.

## Setup
Follow these steps to set up and run the chatbot locally:

### Prerequisites
- Python 3.7 or higher
- A Perplexity API key (available with a Pro version account)

### Installation
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/ChatbotAI-Perplexity.git
   cd ChatbotAI-Perplexity
   ```

2. **Create a Virtual Environment (optional but recommended):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use .venv\Scripts\activate
   ```

3. **Install Required Packages:**
   ```bash
   pip install requests
   ```

4. **Set Your API Key:**
   Open `main.py` and replace `"YOUR_API_KEY"` with your actual Perplexity API key:
   ```python
   perplexity_api_key = "YOUR_API_KEY"
   ```

   Alternatively, you can set the API key as an environment variable:
   ```bash
   export PERPLEXITY_API_KEY="YOUR_API_KEY"  # On Windows use 'set' instead of 'export'
   ```

## Usage
To start the chatbot, run the following command in the terminal:

```bash
python main.py
```

### Stopping the Chatbot
To end the conversation, type any of the following: `quit`, `exit`, or `bye`.

## Configuration
In `main.py`, you can adjust parameters like model and prompt type to customize the chatbot's behavior as supported by the Perplexity API.

## Example
Here's an example interaction with ChatbotAI:
```plaintext
You: Hello
Chatbot: Hello! How can I assist you today?

You: Tell me a joke.
Chatbot: Why did the computer go to the doctor? Because it had a virus!

You: bye
Chatbot: Goodbye! Have a great day!
```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
