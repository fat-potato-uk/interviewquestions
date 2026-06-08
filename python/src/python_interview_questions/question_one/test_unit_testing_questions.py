from unittest.mock import Mock, patch

import pytest

from python_interview_questions.question_one.unit_testing_questions import (
    HostRiskTooHighException,
    HostType,
    RiskConstantGetter,
    UnitTestingInterviewQuestions,
)


@pytest.fixture
def risk_constant_getter():
    getter = Mock(spec=RiskConstantGetter)
    getter.get_cpu_risk_constant.return_value = 10
    getter.get_disk_risk_constant.return_value = 1
    return getter


@pytest.fixture
def unit_testing_interview_questions(risk_constant_getter):
    return UnitTestingInterviewQuestions(risk_constant_getter)


def test_is_host_too_risky_for_web_server(unit_testing_interview_questions):
    with patch.object(
        unit_testing_interview_questions,
        "generate_risk_score",
        return_value=80,
    ):
        assert (
            unit_testing_interview_questions.is_host_too_risky(
                10,
                10,
                HostType.WEB_SERVER,
            )
            is True
        )

    with patch.object(
        unit_testing_interview_questions,
        "generate_risk_score",
        return_value=50,
    ):
        assert (
            unit_testing_interview_questions.is_host_too_risky(
                10,
                10,
                HostType.WEB_SERVER,
            )
            is False
        )


def test_is_host_too_risky_raises_exception_when_risk_score_is_too_high(
    unit_testing_interview_questions,
):
    with patch.object(
        unit_testing_interview_questions,
        "generate_risk_score",
        return_value=101,
    ):
        with pytest.raises(HostRiskTooHighException):
            unit_testing_interview_questions.is_host_too_risky(
                10,
                10,
                HostType.WEB_SERVER,
            )


@pytest.mark.parametrize(
    "cpu_usage,disk_usage,result",
    [
        # Test our happy case
        (100, 20, 200),
        # Test a negative CPU usage
        (-15, 20, -30),
        # Test a 0 value case
        (20, 0, 0),
    ],
)
def test_generate_risk_score(
    unit_testing_interview_questions,
    cpu_usage,
    disk_usage,
    result,
):
    assert (
        unit_testing_interview_questions.generate_risk_score(cpu_usage, disk_usage)
        == result
    )


def test_generate_risk_score_uses_risk_constants(risk_constant_getter):
    risk_constant_getter.get_cpu_risk_constant.return_value = 5
    risk_constant_getter.get_disk_risk_constant.return_value = 2

    unit_testing_interview_questions = UnitTestingInterviewQuestions(
        risk_constant_getter
    )

    assert unit_testing_interview_questions.generate_risk_score(10, 10) == 40

    risk_constant_getter.get_cpu_risk_constant.assert_called_once()
    risk_constant_getter.get_disk_risk_constant.assert_called_once()


def test_risk_constant_getter_calls_external_service():
    mock_response = Mock()
    mock_response.text = "10"

    with patch(
        "python_interview_questions.question_one.unit_testing_questions.client"
    ) as mock_client:
        mock_client.get.return_value = mock_response
        result = RiskConstantGetter().get_cpu_risk_constant()

    assert result == 10
    mock_client.get.assert_called_once_with(
        "https://api.fatpotato.made-up-example/risk/cpu-constant",
        headers={"accept": "application/json"},
        timeout=5,
    )
