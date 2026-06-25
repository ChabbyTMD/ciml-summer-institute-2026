# Coding Agents Demo: Titanic EDA 

This demo shows how to use OpenCode with an LLM service to generate code to perform exploratory data analysis (EDA) on the Titanic dataset.

---
## 1. Start Ollama - Skip if Ollama is already running

1. In a terminal window in Jupyter Lab, follow the following stepsto start an Ollama instance.

2. Set the path where Ollama models are stored:
   
   ```bash
   export OLLAMA_MODELS=/cm/shared/examples/sdsc/ciml/2026//ollama_models/
   ```
   
3. Configure `OLLAMA_HOST` for the Ollama server with a randomly selected port:
   
   ```bash
   export OLLAMA_PORT="$(shuf -i 3000-65000 -n 1)" && echo "${OLLAMA_PORT}" > ~/.ollama_port
   ```

   ```bash
    export OLLAMA_HOST="127.0.0.1:${OLLAMA_PORT}"
   ```

4. Start the Ollama server:

    ```bash
   ollama serve > ollama.log 2>&1 &
   ```
---

## 3. Configure OpenCode to talk to Ollama

1. Check that the OpenCode configuration file exists ( ~/.config/opencode/opencode.json) and is correct.

2. Test that OpenCode can talk to Ollama:

   ```bash
   opencode run "What LLM am I using?" --model ollama/gemma4:e4b
   ```
---

## 4. Use OpenCode to generate a Python script to perform EDA on the file titanic.csv.

1. Start OpenCode:

   ```bash
   opencode
   ```

2. In OpenCode, select the correct model:
    ```text
    /models
    Hit <Return>
    Select qwen3:14b using the up/down arrow key
    ```

3. Copy and paste the following instruction, then hit <Return>:

   ```text
   Read and follow the instructions in the file 'titanic-py-prompt.txt'.
   ```

4. When prompted by OpenCode, select 'Always Allow', then 'Confirm' to give OpenCode permission to read and write files.

5. In another terminal window in Jupyter Lab, convert the Python script to a Jupyter notebook:

   ```bash
   jupytext --to notebook titanic-eda.py -o titanic-eda.ipynb
   ```
If you don't already have jupytext, install it using this command:

```bash
pip install jupytext --user
```
6. Open titanic-eda.ipynb and run it.