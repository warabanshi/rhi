import io
import pytest

from unittest.mock import patch

from rhi.commands.add import Add


input1 = """
  1  ls -lh
  2  cat /tmp/testfile
  3  history
""".strip("\n")

input2 = """
 13  ls -lh
 14  cat /etc/SuSE-brand
 15  cd /home/foo
 16  history
""".strip("\n")

input3 = """
 13  ls -lh
 14*
 15  cd /home/foo
 16  history
""".strip("\n")

line1 = "  10 ls -lh"
line2 = "This is just a single line input"


@patch('rhi.commands.add.Add.__init__')
def test_cleanup_commands_no_rownum_1(mock_add_init):
    mock_add_init.return_value = None

    s = io.StringIO(input1)
    expected = "cat /tmp/testfile"

    add = Add()
    result = add.cleanup_commands(s)

    assert result == expected

@patch('rhi.commands.add.Add.__init__')
def test_cleanup_commands_no_rownum_2(mock_add_init):
    mock_add_init.return_value = None

    s = io.StringIO(input2)
    expected = "cd /home/foo"

    add = Add()
    result = add.cleanup_commands(s)

    assert result == expected

@patch('rhi.commands.add.Add.__init__')
def test_cleanup_commands_with_rownum_1(mock_add_init):
    mock_add_init.return_value = None

    s = io.StringIO(input1)
    expected = "cat /tmp/testfile"

    add = Add()
    result = add.cleanup_commands(s, 2)

    assert result == expected

@patch('rhi.commands.add.Add.__init__')
def test_cleanup_commands_with_rownum_2(mock_add_init):
    mock_add_init.return_value = None

    s = io.StringIO(input2)
    expected = "cd /home/foo"

    add = Add()
    result = add.cleanup_commands(s, 15)

    assert result == expected

@patch('rhi.commands.add.Add.__init__')
def test_cleanup_commands_with_rownum_out_of_range_1(mock_add_init):
    mock_add_init.return_value = None

    s = io.StringIO(input1)

    with pytest.raises(Exception):
        add = Add()
        result = add.cleanup_commands(s, 10)

@patch('rhi.commands.add.Add.__init__')
def test_cleanup_commands_with_rownum_out_of_range_2(mock_add_init):
    mock_add_init.return_value = None

    s = io.StringIO(input2)

    with pytest.raises(KeyError):
        add = Add()
        result = add.cleanup_commands(s, 3)

@patch('rhi.commands.add.Add.__init__')
def test_cleanup_commands_empty_row(mock_add_init):
    mock_add_init.return_value = None

    s = io.StringIO(input3)
    expected = "cd /home/foo"

    add = Add()
    result = add.cleanup_commands(s)

    assert result == expected

@patch('rhi.commands.add.Add.__init__')
def test_is_history_true(mock_add_init):
    mock_add_init.return_value = None
    expected = False

    add = Add()
    result = add.is_history(line1)

    assert result == expected

@patch('rhi.commands.add.Add.__init__')
def test_is_history_false(mock_add_init):
    mock_add_init.return_value = None
    expected = False

    add = Add()
    result = add.is_history(line2)

    assert result == expected

@patch('rhi.commands.add.Add.__init__')
def test_cleanup_tags_normal(mock_add_init):
    mock_add_init.return_value = None

    add = Add()
    result = add.cleanup_tags('bash,docker,local')
    expected = ['bash', 'docker', 'local']

    assert result == expected

@patch('rhi.commands.add.Add.__init__')
def test_cleanup_tags_strip(mock_add_init):
    mock_add_init.return_value = None

    add = Add()
    result = add.cleanup_tags(' bash,docker,local, ')
    expected = ['bash', 'docker', 'local']

    assert result == expected

@patch('rhi.commands.add.Add.__init__')
def test_cleanup_no_tags(mock_add_init):
    mock_add_init.return_value = None

    add = Add()
    result = add.cleanup_tags(None)
    expected = []

    assert result == expected
