import heapq
from collections import defaultdict

# Node classes
class Node:
    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right

    # Needed for priority queue (min-heap)
    def __lt__(self, other):
        return self.freq < other.freq


# Step 1: Build character frequency table
def build_frequency_table(input_string):
    table = defaultdict(int)
    for ch in input_string:
        table[ch] += 1
    return dict(table)


# Step 2: Build Huffman Tree
def build_huffman_tree(input_string):
    freq_table = build_frequency_table(input_string)
    heap = []

    # Create leaf nodes
    for char, freq in freq_table.items():
        heapq.heappush(heap, Node(freq, char))

    # Build tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        parent = Node(left.freq + right.freq, None, left, right)
        heapq.heappush(heap, parent)

    return heap[0]  # Root node


# Step 3: Generate Huffman Codes
def get_codes(node, prefix="", code_map=None):
    if code_map is None:
        code_map = {}

    if node.char is not None:  # Leaf node
        code_map[node.char] = prefix
    else:
        get_codes(node.left, prefix + "0", code_map)
        get_codes(node.right, prefix + "1", code_map)

    return code_map


# Step 4: Compress string
def huffman_compress(input_string):
    root = build_huffman_tree(input_string)
    codes = get_codes(root)
    compressed = "".join(codes[ch] for ch in input_string)
    return compressed, root, codes


# Step 5: Decompress string
def huffman_decompress(compressed_string, root):
    result = []
    node = root
    for bit in compressed_string:
        node = node.left if bit == "0" else node.right
        if node.char is not None:  # Leaf
            result.append(node.char)
            node = root
    return "".join(result)

