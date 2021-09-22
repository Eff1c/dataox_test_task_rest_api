import requests
from decouple import config

failed_output = {
        "Arguments": "company_name, orient (optional)",
        "Output": "Please input company_name argument!",
        "Options orient": "'columns','records','index','split','table'"
    }

test_company_name = config("TEST_COMPANY_NAME")
api_url = "http://127.0.0.1:80/"

def test_none_args():
    assert requests.get(api_url).json() == failed_output

def test_only_orient_arg():
    assert requests.get(api_url, data={"orient": "columns"}).json() == failed_output

def test_only_company_name_arg():
    assert requests.get(api_url, data={"company_name": test_company_name}).json() != failed_output

def test_all_args():
    assert requests.get(
        api_url,
        data={
            "company_name": test_company_name,
            "orient": "columns"
        }
    ).json() != failed_output
