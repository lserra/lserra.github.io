"""Legacy shim for old Fabric commands.

This project migrated from Fabric 1.x (`fab`) to Invoke (`inv`) in `tasks.py`.
Any call to legacy tasks intentionally fails with an actionable migration hint.
"""

from __future__ import annotations


_MIGRATION_HINT = {
    "clean": "inv clean",
    "build": "inv build",
    "rebuild": "inv rebuild",
    "regenerate": "inv regenerate",
    "serve": "inv serve",
    "reserve": "inv reserve",
    "preview": "inv preview",
    "publish": "inv publish",
}


def _legacy_task(task_name: str) -> None:
    replacement = _MIGRATION_HINT.get(task_name, "python -m invoke --list")
    raise SystemExit(
        "[legacy] `fab {task}` is no longer supported in this repository. "
        "Use `{replacement}` instead (or `python -m invoke {task}`).".format(
            task=task_name, replacement=replacement
        )
    )


def clean():
    """Legacy alias for `inv clean`."""
    _legacy_task("clean")


def build():
    """Legacy alias for `inv build`."""
    _legacy_task("build")


def rebuild():
    """Legacy alias for `inv rebuild`."""
    _legacy_task("rebuild")


def regenerate():
    """Legacy alias for `inv regenerate`."""
    _legacy_task("regenerate")


def serve():
    """Legacy alias for `inv serve`."""
    _legacy_task("serve")


def reserve():
    """Legacy alias for `inv reserve`."""
    _legacy_task("reserve")


def preview():
    """Legacy alias for `inv preview`."""
    _legacy_task("preview")


def publish():
    """Legacy alias for `inv publish`."""
    _legacy_task("publish")
