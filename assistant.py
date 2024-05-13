import json
from pathlib import Path
from typing import Optional
from textwrap import dedent
from typing import List

from phi.assistant import Assistant
from phi.tools import Toolkit
from phi.tools.exa import ExaTools
from phi.tools.shell import ShellTools
from phi.tools.calculator import Calculator
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from phi.tools.file import FileTools
from phi.llm.openai import OpenAIChat 
from phi.knowledge import AssistantKnowledge
from phi.embedder.openai import OpenAIEmbedder
from phi.assistant.duckdb import DuckDbAssistant
from phi.assistant.python import PythonAssistant
from phi.storage.assistant.postgres import PgAssistantStorage
from phi.utils.log import logger
from phi.vectordb.pgvector import PgVector2