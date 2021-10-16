import json
import pytest

import requests.models

from unittest.mock import patch

from rhi.commands.get import Get


@patch('rhi.commands.get.Get.__init__')
@patch('rhi.commands.get.Get.call_get')
def test_get_all_output(mock_call_get, mock_get_init):
    res = requests.models.Response()
    res.status_code = 200
    res.encoding = 'utf-8'
    res._content = bytes(json.dumps({
        'result': [
            {'command': 'ls -alh', 'message': '', 'tags': ['python', 'bash']},
            {'command': 'cat /etc/SUSE-brand', 'message': 'opensuse version file', 'tags': []},
        ]}), 'utf-8')

    mock_get_init.return_value = None
    mock_call_get.return_value = res

    expected = [
        " 1: ls -alh  tags=['python', 'bash']", 
        ' 2: cat /etc/SUSE-brand   # opensuse version file',
    ]

    get = Get()
    result = get.get_all()

    assert result == expected

@patch('rhi.commands.get.Get.__init__')
@patch('rhi.commands.get.Get.call_get')
def test_get_single_output(mock_call_get, mock_get_init):
    res = requests.models.Response()
    res.status_code = 200
    res.encoding = 'utf-8'
    res._content = bytes(json.dumps({
        'result': {'command': 'cat /etc/SUSE-brand', 'message': 'opensuse version file', 'tags': []}
    }), 'utf-8')

    mock_get_init.return_value = None
    mock_call_get.return_value = res

    expected = ['cat /etc/SUSE-brand   # opensuse version file']

    get = Get()
    get.num = 2
    result = get.get_single()

    assert result == expected

