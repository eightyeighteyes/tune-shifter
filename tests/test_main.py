"""Tests for tune_shifter.__main__ helpers."""

import pytest

from tune_shifter.__main__ import _yn_prompt


class TestYnPrompt:
    def test_empty_input_returns_default_true(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setattr("builtins.input", lambda _: "")
        assert _yn_prompt("Question?", default=True) is True

    def test_empty_input_returns_default_false(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setattr("builtins.input", lambda _: "")
        assert _yn_prompt("Question?", default=False) is False

    def test_y_returns_true(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr("builtins.input", lambda _: "y")
        assert _yn_prompt("Question?") is True

    def test_yes_returns_true(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr("builtins.input", lambda _: "yes")
        assert _yn_prompt("Question?") is True

    def test_n_returns_false(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr("builtins.input", lambda _: "n")
        assert _yn_prompt("Question?") is False

    def test_eof_returns_default(self, monkeypatch: pytest.MonkeyPatch) -> None:
        def raise_eof(_: str) -> str:
            raise EOFError

        monkeypatch.setattr("builtins.input", raise_eof)
        assert _yn_prompt("Question?", default=True) is True
