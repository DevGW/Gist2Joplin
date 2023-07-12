import pytest
import re
from gist2joplin import Gist2Joplin
from unittest import mock
from unittest.mock import patch

@pytest.fixture
def initial_gists():
    return [
        {
            'id': 'gist1',
            'description': 'Gist 1',
            'files': {
                'file1.txt': {
                    'raw_url': 'https://example.com/raw/file1.txt',
                    'language': 'txt',
                    'content': 'This is the content of file1.txt'
                },
                'file2.py': {
                    'raw_url': 'https://example.com/raw/file2.py',
                    'language': 'python',
                    'content': 'print("Hello, World!")'
                }
            }
        },
        {
            'id': 'gist2',
            'description': 'Gist  2',
            'files': {
                'file3.md': {
                    'raw_url': 'https://example.com/raw/file3.md',
                    'language': 'markdown',
                    'content': '# Example Markdown File\n\nThis is some **bold** text.'
                }
            }
        },
        {
            'id': 'gist3',
            'description': 'Gist 3',
            'files': {
                'file4.md': {
                    'raw_url': 'https://example.com/raw/file4.md',
                    'language': 'markdown',
                    'content': '# Another Markdown File\n\nThis is another Markdown file.'
                }
            }
        }
    ]


def test_get_gists(initial_gists):
    config = {'api_token': 'dummy_token'}
    gt = Gist2Joplin(config)
    gt.gists = initial_gists

    gists = gt.get_gists()

    assert len(gists) == len(initial_gists)


def test_buildTagListDirectories(tmpdir, initial_gists):
    config = {'api_token': 'dummy_token'}
    gt = Gist2Joplin(config)
    gt.gists = initial_gists

    # Set the current working directory to the tmpdir
    with tmpdir.as_cwd():
        gt.buildTagListDirectories(tmpdir)

    output_dir = tmpdir / "output"
    gists_dir = output_dir / "gists"
    assert gists_dir.check(dir=True)
    assert gists_dir.join("Gist 1.md").check(file=True)
    assert gists_dir.join("Gist 2.md").check(file=True)
    assert gists_dir.join("Gist 3.md").check(file=True)


def test_filename_correct(tmpdir, initial_gists):
    config = {'api_token': 'dummy_token'}
    gt = Gist2Joplin(config)
    gt.gists = initial_gists

    # Set the current working directory to the tmpdir
    with tmpdir.as_cwd():
        gt.buildTagListDirectories(tmpdir)

    output_dir = tmpdir / "output"
    gists_dir = output_dir / "gists"
    assert gists_dir.check(dir=True)
    assert gists_dir.join("Gist 1.md").check(file=True)
    assert gists_dir.join("Gist 2.md").check(file=True)
    assert gists_dir.join("Gist 3.md").check(file=True)


@pytest.mark.parametrize("filename, content", [
    ("file1.txt", "This is the content of file1.txt"),
    ("file2.py", "print(\"Hello, World!\")"),
    ("file3.md", "# Example Markdown File\n\nThis is some **bold** text."),
])
@patch("gist2joplin.requests.get")
def test_file_written_correct(mock_get, tmpdir, initial_gists, filename, content):
    config = {'api_token': 'dummy_token'}
    gt = Gist2Joplin(config)
    gt.gists = initial_gists

    # Set up the mock response
    mock_response = mock.Mock()
    mock_response.text = content
    mock_get.return_value = mock_response

    # Set the current working directory to the tmpdir
    with tmpdir.as_cwd():
        gt.buildTagListDirectories(tmpdir)

    output_dir = tmpdir / "output"
    gists_dir = output_dir / "gists"
    assert gists_dir.check(dir=True)

    gist_description = [gist["description"] for gist in initial_gists if filename in gist["files"]][0]
    tags_with_prefix = re.findall(r'\#\w+', gist_description)
    expected_tags = [tag[1:] for tag in tags_with_prefix]
    expected_tags_str = " ".join(expected_tags)

    actual_content = gists_dir.join("Gist 2.md").read()
    expected_content = f"{content}\n\nTags: {expected_tags_str}"
    assert actual_content.strip() == expected_content.strip()
