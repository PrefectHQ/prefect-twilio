from prefect_collection_generator.rest import RESTGenerator

# UPDATE THIS SECTION
service_name = "Twilio"
base_directory = "../prefect-twilio"
overwrite = True
url = ""
routes = []

rest_generator = RESTGenerator(
    service_name,
    base_directory=base_directory,
    overwrite=overwrite
)
rest_generator.generate_endpoint_files(url, routes=routes)
rest_generator.generate_docs_files()
