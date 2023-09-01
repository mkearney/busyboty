#!/bin/bash
/Users/mwk/projects/busyboty/.venv/bin/python Users/mwk/projects/busyboty/run.py
cd /Users/mwk/projects/busyboty && \
    git add count.txt && \
    git commit -m "update" && \
    git push origin master