import datetime
import unittest.mock

import pytest

import pyramid_json_response


def test_default():
    json_response = pyramid_json_response.JsonResponse()

    date_time = datetime.datetime(2017, 11, 19, 00, 18, 6)

    with pytest.raises(TypeError):
        json_response.dump_json(unittest.mock.MagicMock(), {"date_time": date_time})


def test_adapter():
    json_response = pyramid_json_response.JsonResponse()
    json_response.add_adapter(
        unittest.mock.MagicMock(), datetime.datetime, lambda obj, request: obj.isoformat())

    date_time = datetime.datetime(2017, 11, 19, 00, 18, 6)

    actual = json_response.dump_json(unittest.mock.MagicMock(), {"date_time": date_time})
    assert actual == '{"date_time": "2017-11-19T00:18:06"}'
