# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law of agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from typing import List
from src.shared.logger import setup_logger

logger = setup_logger(__name__)

def chunk_text(text: str, chunk_size: int = 1000, overlap: int = 100) -> List[str]:
    """
    Splits text into chunks.

    NOTE: This is a naive, fixed-size implementation that serves as a placeholder.
    For the hackathon, this should be replaced with a context-aware chunking strategy
    like Recursive or Semantic chunking.

    Args:
        text (str): The input text to chunk.
        chunk_size (int): The desired size of each chunk.
        overlap (int): The number of characters to overlap between chunks.

    Returns:
        List[str]: A list of text chunks.
    """
    
    # Naive, fixed-size chunking (TO BE REPLACED)
    if overlap >= chunk_size:
        logger.warning("Overlap is greater than or equal to chunk_size. Adjusting overlap to be chunk_size - 1.")
        overlap = chunk_size - 1

    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += (chunk_size - overlap)

    logger.info(f"Chunked text into {len(chunks)} segments with chunk_size={chunk_size} and overlap={overlap}.")
    return chunks
