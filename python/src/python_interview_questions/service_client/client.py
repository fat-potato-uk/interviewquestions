import asyncio
from dataclasses import dataclass
from uuid import uuid4


@dataclass(frozen=True)
class ComputeResource:
    name: str
    size: str


class Client:
    """Client for the 3rd party compute provider."""

    async def request_compute_resource(self, amount: int) -> list[ComputeResource]:
        # Simulate the 3rd party's response time for demo purposes
        await asyncio.sleep(0.5)
        return [ComputeResource(name=str(uuid4()), size="L") for _ in range(amount)]
