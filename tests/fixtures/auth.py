from economic.auth import Authentication
import pytest
from _pytest.fixtures import SubRequest


@pytest.fixture
def auth(request: SubRequest):
    return Authentication(
        request.config.option.app_id,
        request.config.option.bkm_token
    )
