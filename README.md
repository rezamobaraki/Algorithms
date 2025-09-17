# Algorithms

A comprehensive collection of algorithm implementations in Python, covering various computer science concepts including data structures, sorting algorithms, ciphers, and computational complexity analysis.

## 📋 Contents

### Core Algorithms
- **Two Sum**: Finding two numbers in an array that add up to a target sum
- **ZigZag Iterator**: Iterating through two arrays in a zigzag pattern
- **Rotate**: String rotation algorithm
- **Move Zeros**: Moving all zeros to the end of an array
- **Search Insert**: Binary search for insertion position
- **Buy Sell Stock**: Maximum profit calculation for stock trading
- **Remove Min**: Finding and removing minimum element from stack

### Sorting Algorithms
- **Bead Sort**: Sorting using the bead sort algorithm
- **Bubble Sort**: Implementation of bubble sort with polynomial time complexity

### Ciphers and Encoding
- **Caesar Cipher**: Classic Caesar cipher implementation with Persian and English documentation
- **One Time Pad Cipher**: Cryptographic one-time pad implementation
- **A1Z26 Cipher**: Alphabet to number encoding/decoding

### Complexity Analysis
- **Constant Time O(1)**: Examples of constant time algorithms
- **Linear Time O(n)**: Linear search and traversal algorithms
- **Logarithmic Time O(log n)**: Binary search implementation
- **Polynomial Time O(n²), O(n³)**: Quadratic and cubic time complexity examples
- **Exponential Time O(2ⁿ), O(3ⁿ)**: Subset generation and exponential algorithms

### Utility Functions
- **Isomorphic**: String isomorphism checking
- **Limit**: Array filtering by min/max values
- **Top 1**: Finding most frequent elements in arrays

## 🚀 Usage

Each algorithm is implemented as a standalone Python file with clear documentation and examples. You can run any algorithm directly:

```python
# Example: Two Sum
from _two_sum import two_sum
result = two_sum([2, 6, 11, 15], 18)
print(result)  # Output: [2, 3]
```

## 📚 Algorithm Complexity

This repository includes practical examples of different time complexities:

- **O(1)** - Constant time operations
- **O(log n)** - Logarithmic time (binary search)
- **O(n)** - Linear time (array traversal)
- **O(n²)** - Quadratic time (bubble sort)
- **O(n³)** - Cubic time (certain matrix operations)
- **O(2ⁿ)** - Exponential time (subset generation)

## 🛠 Installation and Setup

1. Clone the repository:
```bash
git clone https://github.com/rezamobaraki/Algorithms.git
cd Algorithms
```

2. Run any algorithm:
```bash
python _two_sum.py
python complexity-linear.py
```

## 📖 Documentation

Each file contains detailed documentation in both English and Persian (where applicable), explaining:
- Algorithm purpose and use cases
- Input/output examples
- Time and space complexity
- Implementation details

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. When contributing:

1. Follow the existing code style
2. Add clear documentation and examples
3. Include time/space complexity analysis
4. Test your implementation with various inputs

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Reza Mobaraki**
- GitHub: [@rezamobaraki](https://github.com/rezamobaraki)
- LinkedIn: [reza-mobaraki](https://linkedin.com/in/reza-mobaraki)

---

*This repository serves as both a learning resource and a reference implementation for common algorithms and data structures in computer science.*
