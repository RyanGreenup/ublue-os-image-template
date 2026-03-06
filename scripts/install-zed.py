#!/usr/bin/env python3
"""Install Zed Editor via Flatpak, ensuring Flathub is configured."""

import subprocess
import sys


def run(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result


def main():
    # Check flatpak is available
    if subprocess.run(["which", "flatpak"], capture_output=True).returncode != 0:
        print("Error: flatpak is not installed.", file=sys.stderr)
        sys.exit(1)

    # Check if Flathub remote is configured
    result = run(["flatpak", "remotes", "--columns=name"])
    remotes = result.stdout.strip().splitlines()
    if "flathub" not in remotes:
        print("Adding Flathub remote...")
        r = run([
            "flatpak", "remote-add", "--if-not-exists", "--user",
            "flathub", "https://flathub.org/repo/flathub.flatpakrepo",
        ])
        if r.returncode != 0:
            print(f"Error adding Flathub: {r.stderr}", file=sys.stderr)
            sys.exit(1)
    else:
        print("Flathub remote already configured.")

    # Check if Zed is already installed
    result = run(["flatpak", "list", "--app", "--columns=application"])
    if "dev.zed.Zed" in result.stdout:
        print("Zed Editor is already installed.")
        return

    # Install Zed
    print("Installing Zed Editor...")
    r = run(["flatpak", "install", "--user", "-y", "flathub", "dev.zed.Zed"])
    if r.returncode != 0:
        print(f"Error installing Zed: {r.stderr}", file=sys.stderr)
        sys.exit(1)

    print("Zed Editor installed successfully.")


if __name__ == "__main__":
    main()
