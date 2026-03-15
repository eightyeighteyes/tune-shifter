"""Tests for tune_shifter.config."""

from pathlib import Path

import pytest

from tune_shifter.config import Config


class TestFirstRunSetup:
    def test_creates_config_file(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """first_run_setup writes a TOML file at the given path."""
        inputs = iter(["~/staging", "~/music", "me@example.com"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        path = tmp_path / "config.toml"
        Config.first_run_setup(path)
        assert path.exists()
        assert "me@example.com" in path.read_text()

    def test_returns_config_with_user_values(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """Returned Config reflects the prompted values."""
        inputs = iter(["~/staging", "~/lib", "test@test.com"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        config = Config.first_run_setup(tmp_path / "config.toml")
        assert config.musicbrainz.contact == "test@test.com"
        assert "staging" in str(config.paths.staging)

    def test_blank_input_uses_default(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """Pressing Enter at a prompt accepts the shown default."""
        monkeypatch.setattr("builtins.input", lambda _: "")
        config = Config.first_run_setup(tmp_path / "config.toml")
        assert config.musicbrainz.contact == "user@example.com"
        assert config.paths.staging == Path("~/Music/staging").expanduser()
        assert config.paths.library == Path("~/Music").expanduser()

    def test_written_toml_is_valid(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """The written TOML file can be loaded back by Config.load()."""
        inputs = iter(["~/staging", "~/music", "me@example.com"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        path = tmp_path / "config.toml"
        Config.first_run_setup(path)
        # Round-trip: load should succeed without error
        loaded = Config.load(path)
        assert loaded.musicbrainz.contact == "me@example.com"

    def test_creates_parent_directories(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """first_run_setup creates intermediate directories if needed."""
        monkeypatch.setattr("builtins.input", lambda _: "")
        path = tmp_path / "nested" / "dir" / "config.toml"
        Config.first_run_setup(path)
        assert path.exists()
