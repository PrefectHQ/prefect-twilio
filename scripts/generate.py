"""
Used for appending extra routes.
"""
import httpx
from prefect_collection_generator.rest import populate_collection_repo

# UPDATE THIS SECTION
collection_template_url = "https://github.com/PrefectHQ/prefect-collection-template"
service_name = "Twilio"
base_url = "https://raw.githubusercontent.com/twilio/twilio-oai/main/"
tree = httpx.get(
    "https://api.github.com/repos/twilio/twilio-oai/git/trees/main?recursive=1"
).json()["tree"]
urls = [
    base_url + branch["path"]
    for branch in tree
    if branch["path"].startswith("spec/json/")
]
routes = None
overwrite = True

populate_collection_repo(
    service_name,
    urls,
    routes=routes,
    overwrite=overwrite,
    repo_directory="..",
    file_name_as_module=True,
)
