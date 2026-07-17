from huggingface_hub import HfApi
import os

# Retrieve token
hf_token = os.getenv("HF_TOKEN")
if not hf_token:
    raise ValueError("❌ 'HF_TOKEN' environment variable is missing!")

api = HfApi(token=hf_token)

repo_id = "tharung492/Tourism-Purchase-Prediction"
repo_type = "space"

# Ensure the Space exists before uploading
try:
    api.repo_info(repo_id=repo_id, repo_type=repo_type)
    print(f"✅ Space '{repo_id}' already exists.")
except RepositoryNotFoundError:
    print(f"🚀 Space '{repo_id}' not found. Creating a new Streamlit Space...")
    create_repo(
        repo_id=repo_id,
        repo_type=repo_type,
        space_sdk="streamlit",  # Tells HF to configure it for Streamlit
        private=False
    )
    print("✅ Space successfully created!")

api = HfApi(token=os.getenv("HF_TOKEN"))
api.upload_folder(
    folder_path="tourism_project/deployment",  # the local folder containing your files
    repo_id="tharung492/Tourism-Purchase-Prediction",  # the target repo
    repo_type="space",  # dataset, model, or space
    path_in_repo="",  # optional: subfolder path inside the repo
)
