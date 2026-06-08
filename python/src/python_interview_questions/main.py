import asyncio
import logging
from typing import Annotated

import uvicorn
from fastapi import Depends, FastAPI, Request

from python_interview_questions.service_client import Client, ComputeResource


# Create a FastAPI 'dependency' to facilitate dependency injection of
# our service client in to FastAPI endpoints
def get_api_client(request: Request) -> Client:
    return request.app.state.client


def get_current_resource_list(request: Request) -> list[ComputeResource]:
    return request.app.state.acquired_resources


# Type hint for easy of use in method signatures
ApiClient = Annotated[Client, Depends(get_api_client)]
ResourceList = Annotated[list[ComputeResource], Depends(get_current_resource_list)]


def create_app(client: Client, resource_list: list[ComputeResource]) -> FastAPI:
    """Create a FastAPI application instance. Registers the client and resource list
    on the FastAPI context"""
    app = FastAPI()
    app.state.acquired_resources = resource_list
    app.state.client = client

    @app.get("/api/v1/compute")
    async def acquire_compute(
        amount: int, client: ApiClient, resource_list: ResourceList
    ) -> None:
        """Endpoint that calls a 3rd party API to acquire compute resources."""
        try:
            new_resources = await client.request_compute_resource(amount)
            resource_list.extend(new_resources)
        except Exception as exc:
            print(f"Unable to acquire more compute: {exc}")

    return app


async def log_acquired_resources(current_resources: list[ComputeResource]) -> None:
    """Log out the resources that have been acquired by this application instance"""
    while True:
        await asyncio.sleep(5.0)

        if len(current_resources) == 0:
            continue

        # Convert list to just the names
        current_resources = [resource.name for resource in current_resources]
        print("=== Currently Acquired Resources ===")
        for resource in current_resources:
            print(resource)


async def run():

    client = Client()
    acquired_resource_list = []
    app = create_app(client, acquired_resource_list)

    config = uvicorn.Config(app, host="0.0.0.0", port=8000, log_level="warning")
    server = uvicorn.Server(config)

    async with asyncio.TaskGroup() as tg:
        tg.create_task(server.serve())
        tg.create_task(log_acquired_resources(acquired_resource_list))


def main():
    logging.getLogger("httpx").setLevel(logging.WARNING)
    try:
        asyncio.run(run())
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
