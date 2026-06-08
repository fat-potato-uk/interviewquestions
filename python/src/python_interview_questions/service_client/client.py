from dataclasses import dataclass
from uuid import uuid4

import httpx


@dataclass(frozen=True)
class ComputeResource:
    name: str
    size: str


class Client:
    def __init__(self, base_url_override: str | None = None):
        self._base_url = (
            "https://httpbin.org" if not base_url_override else base_url_override
        )
        self._http_client = httpx.AsyncClient(
            headers={"Content-Type": "application/json"},
            timeout=60,
        )

    async def request_compute_resource(self, amount: int) -> list[ComputeResource]:
        response = await self._http_client.post(
            f"{self._base_url}/anything/compute", json={"amount": amount}
        )
        response.raise_for_status()

        # We simulate our return types here for demo purposes
        return [ComputeResource(name=str(uuid4()), size="L") for _ in range(0, amount)]
