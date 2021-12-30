from requests import Session, Response
import logging

LOGGER = logging.getLogger(__name__)


def test_using_fixture_example(email: str):
    LOGGER.info(msg=f"Email being passed is - {email}")
    assert email == "brandon@techstep.com"


def test_can_login_using_api_requests():
    session = Session()

    # mimic landing to the landing page
    landing_page_response = session.get(url='http://127.0.0.1:5000/')
    LOGGER.info(f"Status Code : {landing_page_response.status_code}")
    LOGGER.info(f"Cookies : {session.cookies}")
    LOGGER.info(f"Headers : {session.headers}")
    
    assert landing_page_response.status_code == 200
    
    # logging in with a post request
    login_info = {
        "email": "brandon@techstep.com",
        "password": "abc123"
    }
    request_url = "http://127.0.0.1:5000/v1/login"
    login_response: Response = session.post(url=request_url, data=login_info)
    LOGGER.info(login_response.status_code)