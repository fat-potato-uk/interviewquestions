import asyncio

import uvicorn
from fastapi import FastAPI

from python_interview_questions.service_client import Client, ComputeResource


def create_app(client: Client, resources: list[ComputeResource]) -> FastAPI:
    """Create a FastAPI application that brokers compute requests to the 3rd
    party and keeps a record of the acquired resources"""
    app = FastAPI()

    @app.post("/api/v1/compute")
    async def acquire_compute(amount: int) -> list[ComputeResource]:
        """Acquire compute resources from the 3rd party"""
        new_resources = await client.request_compute_resource(amount)
        resources.extend(new_resources)
        return new_resources

    @app.get("/api/v1/compute")
    async def list_compute() -> list[ComputeResource]:
        """List the compute resources acquired by this application instance"""
        return resources

    return app


async def log_acquired_resources(new_resources: list[ComputeResource]) -> None:
    """Every 5 seconds, log the resources acquired since the last report"""
    while True:
        await asyncio.sleep(5.0)

        if not new_resources:
            continue

        print("=== Newly Acquired Resources ===")
        for resource in new_resources:
            print(resource.name)

        # Start the next report from empty
        new_resources.clear()


async def run() -> None:
    client = Client()
    acquired_resources: list[ComputeResource] = []
    app = create_app(client, acquired_resources)

    config = uvicorn.Config(app, host="127.0.0.1", port=8000, log_level="warning")
    server = uvicorn.Server(config)

    async with asyncio.TaskGroup() as tg:
        tg.create_task(server.serve())
        tg.create_task(log_acquired_resources(acquired_resources))


def main() -> None:
    try:
        asyncio.run(run())
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
