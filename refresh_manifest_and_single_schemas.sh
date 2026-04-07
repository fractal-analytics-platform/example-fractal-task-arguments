#!/bin/bash

uv run fractal-manifest create
uv run ./single_json_schemas/extract.py
