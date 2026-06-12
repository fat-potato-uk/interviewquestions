import argparse
import configparser
from dataclasses import dataclass
from pathlib import Path

import httpx


@dataclass(frozen=True)
class Config:
    max_compute_amount: int
    base_url: str


def make_request(compute_amount: int, config: Config) -> None:
    client = httpx.Client(headers={"Content-Type": "application/json"})
    endpoint = f"{config.base_url}/api/v1/compute"
    response = client.get(endpoint, params={"amount": compute_amount})
    response.raise_for_status()


def validate_args(args):
    """Further validates the arguments past the context for which `argparse` can be responsible"""
    if args.config:
        assert isinstance(args.config, Path)  # Assert the type for valid type-hinting
        if not args.config.exists():
            raise RuntimeError("Config path does not exist")

    if args.interactive == False and args.amount is None:
        raise RuntimeError(
            "If the script is not in interactive mode, --amount must be supplied on the command line"
        )


def parse_config(config_file: Path | None):
    """Parse the configuration file if one is provided, else return defaults"""
    if config_file is None:
        return Config(max_compute_amount=10, base_url="")

    parser = configparser.ConfigParser()
    parser.read(config_file)

    # Parse the constraints in the config file
    constraints = parser["constraints"]
    max_compute_amount: int = int(constraints.get("max-compute-request", 10))

    # Parse the service options in the config file
    service = parser["service"]
    base_url = service.get("base_url", "")
    return Config(max_compute_amount=max_compute_amount, base_url=base_url)


def interactive() -> int:
    """Interactively ask the user for the number of compute resources they require"""
    user_input = input("Compute amount required: ")
    try:
        return int(user_input)
    except ValueError:
        raise RuntimeError(f"[{user_input}] is not a valid integer")


def main():
    parser = argparse.ArgumentParser(
        description="CLI for interacting with the compute management service",
        color=True,
    )
    parser.add_argument(
        "-c",
        "--config",
        type=Path,
        default="./example-config.ini",
        nargs="?",
        help="An optional path to the config file to use",
    )
    parser.add_argument(
        "-i",
        "--interactive",
        default=False,
        action="store_true",
        help="Use interactive mode when the script is run",
    )
    parser.add_argument(
        "-a", "--amount", type=int, nargs="?", help="The amount of compute to request"
    )

    args = parser.parse_args()

    try:
        validate_args(args)
        config = parse_config(args.config)
        compute_amount = interactive() if args.interactive else args.amount
        if compute_amount > config.max_compute_amount:
            raise RuntimeError(
                f"Cannot request [{compute_amount}] resource, amount too high!"
            )
        make_request(compute_amount, config)
        print(f"Successfully requested [{compute_amount}] resources!")

    except Exception as exc:
        print(f"Script exiting: {exc}")


if __name__ == "__main__":
    main()
