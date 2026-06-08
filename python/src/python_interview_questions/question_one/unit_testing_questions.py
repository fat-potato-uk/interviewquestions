from dataclasses import dataclass
from enum import Enum

import httpx

client = httpx.Client()


class HostType(Enum):
    WEB_SERVER = "WEB_SERVER"
    DATABASE = "DATABASE"
    BUILD_AGENT = "BUILD_AGENT"


class HostRiskTooHighException(Exception):
    pass


class RiskConstantGetter:
    def get_cpu_risk_constant(self) -> int:
        # We call an external service to get the constant, so first, build the request
        response = client.get(
            "https://api.fatpotato.made-up-example/risk/cpu-constant",
            headers={"accept": "application/json"},
            timeout=5,
        )

        # Then return the value
        return int(response.text)

    def get_disk_risk_constant(self) -> int:
        # We call an external service to get the constant, so first, build the request
        response = client.get(
            "https://api.fatpotato.made-up-example/risk/disk-constant",
            headers={"accept": "application/json"},
            timeout=5,
        )

        # Then return the value
        return int(response.text)


@dataclass
class UnitTestingInterviewQuestions:
    risk_constant_getter: RiskConstantGetter

    def is_host_too_risky(
        self,
        cpu_usage: int,
        disk_usage: int,
        host_type: HostType,
    ) -> bool:
        risk_score = self.generate_risk_score(cpu_usage, disk_usage)

        if risk_score > 100:
            raise HostRiskTooHighException()

        match host_type:
            case HostType.WEB_SERVER:
                return risk_score > 70
            case HostType.DATABASE:
                return risk_score > 40
            case HostType.BUILD_AGENT:
                return risk_score > 60

    def generate_risk_score(self, cpu_usage: int, disk_usage: int) -> int:
        # TODO: Some additional maths that makes this function very long and complex
        disk_risk_score = self._calculate_disk_risk_score(disk_usage)
        return (
            cpu_usage * disk_risk_score
        ) // self.risk_constant_getter.get_cpu_risk_constant()

    def _calculate_disk_risk_score(self, disk_usage: int) -> int:
        # TODO: More complex maths
        return disk_usage * self.risk_constant_getter.get_disk_risk_constant()
