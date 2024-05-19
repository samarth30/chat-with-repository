# chat with github repository

1. Create a virtual environment and activate on your local machine to isolate the project's dependencies.

```bash
 python -m venv
 source env/bin/activate
```

2. Install the required Python packages using `pip`.

   ```bash
   pip install -r requirements.txt
   ```

3. Install the "llama-cpp-python" library.
   ### Installation without Hardware Acceleration
   ```bash
   pip install llama-cpp-python
   ```

## Usage

1. Open your terminal and run the following command to start the application:

   ```bash
   streamlit run app.py
   ```

2. You can now input the GitHub repository link.

3. it will fetch all the files from the repository and store them in a folder named "cloned_repo."

4. The embeddings are stored locally in a vector database called ChromaDB.
