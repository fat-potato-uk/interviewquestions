from argparse import Namespace
from unittest.mock import patch

import pytest

from python_interview_questions.user_tools.acquire_compute import (
    Config,
    make_request,
    validate_args,
)


class TestValidateArgs:
    def test_passes_when_no_config_and_amount_supplied(self):
        args = Namespace(config=None, interactive=False, amount=5)

        assert validate_args(args) is None

    def test_passes_in_interactive_mode_without_amount(self):
        args = Namespace(config=None, interactive=True, amount=None)

        assert validate_args(args) is None

    def test_passes_when_config_path_exists(self, tmp_path):
        config_file = tmp_path / "config.ini"
        config_file.write_text("[constraints]\nmax-compute-request = 5\n")
        args = Namespace(config=config_file, interactive=True, amount=None)

        assert validate_args(args) is None


class TestMakeRequest:
    @patch("python_interview_questions.user_tools.acquire_compute.httpx")
    def test_requests_compute_endpoint_with_amount(self, mock_httpx):
        config = Config(max_compute_amount=10, base_url="http://localhost:8000")
        mock_client = mock_httpx.Client.return_value

        assert make_request(7, config) is None

        mock_httpx.Client.assert_called_once_with(
            headers={"Content-Type": "application/json"}
        )
        mock_client.get.assert_called_once_with(
            "http://localhost:8000/api/v1/compute",
            params={"amount": 7},
        )

    @patch("python_interview_questions.user_tools.acquire_compute.httpx")
    def test_raises_for_status_on_the_response(self, mock_httpx):
        config = Config(max_compute_amount=10, base_url="http://localhost:8000")
        mock_client = mock_httpx.Client.return_value
        mock_response = mock_client.get.return_value

        make_request(3, config)

        mock_response.raise_for_status.assert_called_once_with()

    @pytest.mark.parametrize(
        "base_url,expected_endpoint",
        [
            ("http://localhost:8000", "http://localhost:8000/api/v1/compute"),
            ("https://compute.example.com", "https://compute.example.com/api/v1/compute"),
        ],
    )
    @patch("python_interview_questions.user_tools.acquire_compute.httpx")
    def test_builds_endpoint_from_config_base_url(
        self, mock_httpx, base_url, expected_endpoint
    ):
        config = Config(max_compute_amount=10, base_url=base_url)
        mock_client = mock_httpx.Client.return_value

        make_request(1, config)

        mock_client.get.assert_called_once_with(
            expected_endpoint, params={"amount": 1}
        )
