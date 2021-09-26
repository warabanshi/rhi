import io
import pytest

from unittest.mock import patch

from rhi.commands.add import Add


input1 = """
  1  ls -lh
  2  cat /tmp/testfile
  3  history
""".strip()

input2 = """
 13  ls -lh
 14  cat /etc/SuSE-brand
 15  cd /home/foo
 16  history
""".strip()

input3 = """
 13  ls -lh
 14*
 15  cd /home/foo
 16  history
""".strip()


@patch('rhi.commands.add.Add.__init__')
def test_cleanup_input_no_rownum_1(mock_add_init):
    mock_add_init.return_value = None

    s = io.StringIO(input1)
    expected = "cat /tmp/testfile"

    add = Add()
    result = add.cleanup_input(s)

    assert result == expected

@patch('rhi.commands.add.Add.__init__')
def test_cleanup_input_no_rownum_2(mock_add_init):
    mock_add_init.return_value = None

    s = io.StringIO(input2)
    expected = "cd /home/foo"

    add = Add()
    result = add.cleanup_input(s)

    assert result == expected

@patch('rhi.commands.add.Add.__init__')
def test_cleanup_input_with_rownum_1(mock_add_init):
    mock_add_init.return_value = None

    s = io.StringIO(input1)
    expected = "cat /tmp/testfile"

    add = Add()
    result = add.cleanup_input(s, 2)

    assert result == expected

@patch('rhi.commands.add.Add.__init__')
def test_cleanup_input_with_rownum_2(mock_add_init):
    mock_add_init.return_value = None

    s = io.StringIO(input2)
    expected = "cd /home/foo"

    add = Add()
    result = add.cleanup_input(s, 15)

    assert result == expected

@patch('rhi.commands.add.Add.__init__')
def test_cleanup_input_with_rownum_out_of_range_1(mock_add_init):
    mock_add_init.return_value = None

    s = io.StringIO(input1)

    with pytest.raises(Exception):
        add = Add()
        result = add.cleanup_input(s, 10)

@patch('rhi.commands.add.Add.__init__')
def test_cleanup_input_with_rownum_out_of_range_2(mock_add_init):
    mock_add_init.return_value = None

    s = io.StringIO(input2)

    with pytest.raises(KeyError):
        add = Add()
        result = add.cleanup_input(s, 3)

@patch('rhi.commands.add.Add.__init__')
def test_cleanup_input_empty_row(mock_add_init):
    mock_add_init.return_value = None

    s = io.StringIO(input3)
    expected = "cd /home/foo"

    add = Add()
    result = add.cleanup_input(s)

    assert result == expected

