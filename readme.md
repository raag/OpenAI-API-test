## OpenAI API Test

This is a test of the openAI's API.

It simulates a virtual assistant over voice.

## Test it.

Clone this project:

```bash
git clone https://github.com/raag/OpenAI-API-test.git
```

Go to project directory.

```bash
cd OpenAI-API-test
```

Install the dependencies:

```bash
pip3 install -r requirements.txt
```

Create a file named `.env` with the next content:

```
OPENAI_API_KEY=XXXXXXXXXXXXXXXXXXXX
LANGUAGE=en
```

You can get your OPEN_API_KEY from https://platform.openai.com/account/api-keys
For now in LANGUAGE you can use `en` and `es`

Run the project:

```bash
python3 main.py
```

Just tell to your mic what do you need and wait for your response.
