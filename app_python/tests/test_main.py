from datetime import datetime, timedelta, timezone

import pytest


@pytest.fixture()
def test_format():
    format = "%H:%M:%S"
    timezone_offset = 3.0  # Moscow Standard Time (UTC+03:00)
    tzinfo = timezone(timedelta(hours=timezone_offset))
    time = datetime.now(tzinfo)
    return datetime.datetime.strftime(time, format)
