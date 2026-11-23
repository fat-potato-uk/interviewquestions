import argparse
import configparser
from dataclasses import dataclass
from pathlib import Path

import httpx

DEFAULT_BASE_URL = "https://compute.prod.example.com"
DEFAULT_MAX_COMPUTE_AMOUNT = 10


@dataclass(frozen=True)
class Config:
    max_compute_amount: int
    base_url: str


def make_request(compute_amount: int, config: Config) -> None:
    endpoint = f"{config.base_url}/api/v1/compute"
    response = httpx.post(endpoint, params={"amount": compute_amount})
    response.raise_for_status()


def validate_args(args: argparse.Namespace) -> None:
    """Further validates the arguments past the context for which `argparse` can be responsible"""
    if args.config is not None and not args.config.exists():
        raise RuntimeError("Config path does not exist")


def parse_config(config_file: Path | None) -> Config:
    """Parse the configuration file if one is provided, else return defaults"""
    parser = configparser.ConfigParser()
    if config_file is not None:
        parser.read(config_file)

    max_compute_amount = parser.getint(
        "constraints", "max-compute-request", fallback=DEFAULT_MAX_COMPUTE_AMOUNT
    )
    base_url = parser.get("service", "base_url", fallback=DEFAULT_BASE_URL)
    return Config(max_compute_amount=max_compute_amount, base_url=base_url)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="CLI for interacting with the compute management service"
    )
    parser.add_argument(
        "-c", "--config", type=Path, help="An optional path to the config file to use"
    )
    parser.add_argument(
        "-a",
        "--amount",
        type=int,
        required=True,
        help="The amount of compute to request",
    )

    args = parser.parse_args()

    try:
        validate_args(args)
        config = parse_config(args.config)
        if args.amount > config.max_compute_amount:
            raise RuntimeError(
                f"Cannot request [{args.amount}] resource, amount too high!"
            )
        make_request(args.amount, config)
        print(f"Successfully requested [{args.amount}] resources!")

    except Exception as exc:
        print(f"Script exiting: {exc}")


if __name__ == "__main__":
    main()
