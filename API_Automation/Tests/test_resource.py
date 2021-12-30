from pytest import mark
import logging

LOGGER = logging.getLogger(__name__)


@mark.resource
def test_can_add_resource(logged_in_session, app_url):
    resource_url: str = f"{app_url}/v1/resource"
    request_payload: dict = {
        "author": "Brandon Blair",
        "edition": "",
        "id": 1,
        "isbn10": "11119999",
        "isbn13": "",
        "title": "Elegant API Automation: The Sequel"
    }

    add_resource_response = logged_in_session.post(
        url=resource_url,
        json=request_payload)

    response_data = add_resource_response.json()
    LOGGER.info(f"Response data = {response_data}")
    assert response_data.get("error") == "add-resource-error"