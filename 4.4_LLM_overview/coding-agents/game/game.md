# Coding Agents using OpenCode + Ollama: Number Guessing Game 

In this exercise you will:
1. Start an Ollama instance   
2. Configure OpenCode to talk to Ollama   
3. Use OpenCode to generate a number guessing game as a single Python script
4. Execute the script to play the game  

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

## 2. Configure OpenCode to talk to Ollama

1. Create an OpenCode config file to connect to the Ollama server.  This file has already been creted for you.  Copy it to ~/.config/opencode:

   ```bash
   cp opencode.json ~/.config/opencode
   ```

3. Test that OpenCode can talk to Ollama:

   ```bash
   opencode run "What LLM am I using?" --model ollama/gemma4:e4b
   ```
---

## 3. Use OpenCode to generate the number guessing game

1. Start OpenCode:

   ```bash
   opencode
   ```

2. In OpenCode, select the correct model:

    ```text
    /models
    Hit <Return>
    Select gemma4:e4b using the up/down arrow key
    ```

3. Copy and paste the following instruction, then hit \<Return\>:

   ```text
   You are writing a single Python script.

   Task:
   Write a complete Python script that implements a number guessing game with these requirements:
   - The computer picks a random number from 1 to 100.
   - The player types a guess into an input box and presses Enter to submit.
   - Show whether the guess is too high, too low, or correct.
   - Count and display guesses made.
   - When correct, ask if the player wants to play again, and reset if yes.
   - All code must be in a single file named game.py.
   - Do not create any other files.

   Now generate game.py in the current directory.
   ```

4. Let OpenCode run and create `game.py`.When prompted, select 'Allow Always', then 'Confirm' to give OpenCode permission to write files.

5. In another terminal window in Jupyter Lab, execute the script:

   ```bash
   python3 game.py
   ```
6. Type 'exit' to exit OpenCode.