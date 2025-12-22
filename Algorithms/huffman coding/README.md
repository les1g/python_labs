# Huffman Coding & Lossless Text Compression

## Purpose of This Module

This module demonstrates how **Huffman coding** compresses text by assigning shorter bit patterns to frequent characters and longer patterns to rare ones. It provides a complete, working implementation of:

- Building a frequency table  
- Constructing a Huffman tree  
- Generating prefix‑free binary codes  
- Compressing text into a bitstring  
- Decompressing the bitstring back to the original text  

The included demonstration shows the full compression cycle using the string `"BANANAS"`.

## What Is Huffman Coding?

Huffman coding is a **lossless compression algorithm** that reduces file size by using variable‑length binary codes:

- Characters that appear often receive **shorter codes**  
- Characters that appear rarely receive **longer codes**  

This ensures the total number of bits used is minimized.

Huffman coding is widely used in:

- ZIP and GZIP compression  
- JPEG image encoding  
- Network protocols  
- Text and data compression systems  

## Why Huffman Coding Works

Compression is effective because real text is not random. Some characters appear far more frequently than others.

Huffman coding takes advantage of this by:

1. Counting character frequencies  
2. Building a binary tree where frequent characters are closer to the root  
3. Assigning shorter codes to those frequent characters  
4. Ensuring all codes are **prefix‑free** (no code is the prefix of another)

Prefix‑free codes guarantee that the compressed bitstream can be decoded unambiguously.

## How the Algorithm Works

### 1. Build a Frequency Table  
Count how many times each character appears in the input string.

### 2. Build the Huffman Tree  
Use a min‑heap to repeatedly combine the two least‑frequent nodes into a binary tree.

### 3. Generate Codes  
Traverse the tree:

- Left branch = 0  
- Right branch = 1  

Leaf nodes receive their final binary codes.

### 4. Compress  
Replace each character in the input with its binary code to form a compressed bitstring.

### 5. Decompress  
Walk the tree bit‑by‑bit to reconstruct the original text.

This process is guaranteed to be lossless.

## Program Structure

### Node Class  
Represents a node in the Huffman tree:

- `freq`: frequency of the character  
- `char`: character stored in leaf nodes  
- `left`, `right`: child nodes  

Implements `__lt__` so nodes can be compared inside a min‑heap.

### Frequency Table  
`build_frequency_table()` returns a dictionary mapping characters to counts.

### Huffman Tree Builder  
`build_huffman_tree()` constructs the binary tree using a priority queue.

### Code Generator  
`get_codes()` recursively assigns binary codes to each character.

### Compressor  
`huffman_compress()` returns:

- The compressed bitstring  
- The Huffman tree root  
- The dictionary of character codes  

### Decompressor  
`huffman_decompress()` walks the tree to rebuild the original string.

## Summary

This module provides a complete, working implementation of Huffman coding and demonstrates:

- How frequency drives compression  
- How the Huffman tree produces optimal prefix‑free codes  
- How text is compressed into a bitstring  
- How decompression restores the exact original text  

Understanding Huffman coding builds a foundation for studying more advanced compression algorithms and data‑encoding techniques.

