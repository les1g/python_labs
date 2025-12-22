from huffman_functions import huffman_compress, huffman_decompress

# Example usage
if __name__ == "__main__":
    print("\n=== HUFFMAN COMPRESSION DEMONSTRATION ===")
    print("This module demonstrates how Huffman coding compresses text by assigning")
    print("shorter bit patterns to frequent characters and longer patterns to rare ones.\n")

    print("How Huffman Compression Works:")
    print("- Count how often each character appears.")
    print("- Build a binary tree where frequent characters are closer to the root.")
    print("- Assign shorter binary codes to frequent characters.")
    print("- Assign longer binary codes to rare characters.")
    print("Why this is important:")
    print("- Produces optimal prefix-free codes.")
    print("- Reduces file size without losing information.")
    print("- Forms the basis of many real-world compression algorithms.\n")

    # ---------------------------------------------------------
    # Demonstration
    # ---------------------------------------------------------
    text = "BANANAS"

    print("===============================================")
    print("Original text:", text)
    print("Compressing using Huffman coding...\n")

    compressed, root, codes = huffman_compress(text)

    print("Character Codes (Huffman Tree Output):")
    for char, code in codes.items():
        print(f"  '{char}': {code}")

    print("\nCompressed bitstring:")
    print(compressed)

    print("\nDecompressing...")
    decompressed = huffman_decompress(compressed, root)

    print("Decompressed text:", decompressed)

    # ---------------------------------------------------------
    # Summary
    # ---------------------------------------------------------
    print("\n===============================================")
    print("SUMMARY: WHY HUFFMAN CODING MATTERS")
    print("-----------------------------------------------")
    print("Huffman coding is useful when:")
    print("- You want lossless compression.")
    print("- Some characters appear more frequently than others.")
    print("- You need efficient encoding for text or data streams.")

    print("\nHuffman coding is NOT ideal when:")
    print("- All characters appear with equal frequency.")
    print("- You need random access to encoded data.")
    print("- You require extremely fast encoding/decoding.")

    print("\nThis example shows how Huffman coding:")
    print("- Compresses data by using variable-length codes.")
    print("- Guarantees no code is a prefix of another (prefix-free).")
    print("- Always decompresses back to the exact original text.")