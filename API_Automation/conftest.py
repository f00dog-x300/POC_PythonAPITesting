from pytest import fixture
from requests import Session, Response


@fixture
def email() -> str:
    """Example email fixture"""
    return "brandon@techstep.com"

@fixture
def app_url() -> str:
    """Base Url to be used across tests"""
    return "http://127.0.0.1:5000"

@fixture
def logged_in_session(app_url):
    session: Session = Session()
    # mimicking landing in the login page
    landing_page_response = session.get(url=app_url)
    
    # Logging in with a POST request
    login_request_url: str = f"{app_url}/v1/login"
    login_info: dict = {
        "email": "brandon@techstep.com",
        "password": "abc123"
    }
    login_resp: Response = session.post(url=login_request_url, data=login_info)
    
    if login_resp.status_code != 200:
        raise ValueError(f"Expected 200, but received {login_resp.status_code}")
    
    return session
