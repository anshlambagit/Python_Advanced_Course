# Python for Data Domain - Advanced Tutorial

A comprehensive tutorial covering advanced Python concepts and techniques essential for data professionals. This course goes beyond the fundamentals to equip you with industry-standard practices in object-oriented programming, asynchronous operations, testing, and data handling.

## Full YouTube Tutorial: 
- https://youtu.be/M-UtKxgtKag?si=JKqncawI92fa18aL

## 📚 Course Overview

This tutorial is structured into 9 chapters, each focusing on critical Python concepts that are crucial for data engineers, data scientists, and backend developers working with data-heavy applications.

**Target Audience:** Intermediate Python developers with foundational knowledge who want to level up their skills for data-centric projects.

**Prerequisites:** Basic understanding of Python syntax, data types, and control flow.

## 📋 Table of Contents

### [Chapter 1: Object-Oriented Programming (OOP)](#chapter-1-object-oriented-programming)
### [Chapter 2: Inheritance](#chapter-2-inheritance)
### [Chapter 3: Polymorphism & Decorators](#chapter-3-polymorphism--decorators)
### [Chapter 4: Multi-Threading](#chapter-4-multi-threading)
### [Chapter 5: Pydantic](#chapter-5-pydantic)
### [Chapter 6: Asynchronous Programming](#chapter-6-asynchronous-programming)
### [Chapter 7: APIs](#chapter-7-apis)
### [Chapter 8: PyTest](#chapter-8-pytest)
### [Chapter 9: OS Operations](#chapter-9-os-operations)

---

## Chapter 1: Object-Oriented Programming

**Location:** `Ch-1_OOP/`

Master the fundamentals of OOP in Python, the backbone of scalable data applications.

### Topics Covered:
- **1_basics.py** - Core OOP concepts: classes, objects, attributes, and methods
- **2_constructors.py** - Understanding `__init__` and object initialization
- **3_encapsulation.py** - Data hiding, private/protected attributes, and properties
- **4_DataExt_Class.py** - Working with dataclass decorator for simplified class creation
- **5_methods.py** - Instance methods, class methods, and static methods

### Key Learnings:
- How to design and structure classes effectively
- Encapsulation principles for robust code
- Using dataclasses for concise, maintainable code
- Method types and their use cases

### Example Files:
- Sample data files in `Files/`: `orders.csv`, `orders.json`, `orders.tsv`

---

## Chapter 2: Inheritance

**Location:** `Ch-2_Inheritance/`

Learn how to create hierarchical class structures and reuse code through inheritance.

### Topics Covered:
- **1_single_level.py** - Single inheritance: parent-child class relationships
- **2.1_multiple.py** - Multiple inheritance: inheriting from multiple classes (Part 1)
- **2.2_multiple.py** - Multiple inheritance: Method Resolution Order (MRO) and diamond problem (Part 2)
- **3_multi_level.py** - Multi-level inheritance: grandparent → parent → child chains

### Key Learnings:
- Advantages and pitfalls of inheritance patterns
- Method Resolution Order (MRO) and how Python resolves method calls
- Handling the diamond problem in multiple inheritance
- When to use inheritance vs. composition

---

## Chapter 3: Polymorphism & Decorators

**Location:** `Ch-3_Polymorphism&Decorators/`

Leverage polymorphism and decorators to write flexible, DRY Python code.

### Topics Covered:
- **1_polymorphism.py** - Method overriding, duck typing, and interface design
- **2_decorators.py** - Function decorators: enhancing functions without modifying them
- **3_decorator_pandas.py** - Practical decorators for data manipulation with pandas

### Key Learnings:
- Writing polymorphic code that works with multiple types
- Creating custom decorators for logging, validation, and performance monitoring
- Decorator patterns in data processing workflows
- Higher-order functions and function wrappers

### Additional Files:
- `orders.csv` - Sample data for decorator examples

---

## Chapter 4: Multi-Threading

**Location:** `Ch-4_Multi-Threading/`

Master concurrent programming with threads for I/O-bound operations.

### Topics Covered:
- **1_multi-threading.py** - Thread basics, creating and managing threads, the GIL, and thread synchronization
  - Thread creation and lifecycle
  - Thread safety and locks
  - Race conditions and deadlocks
  - Practical examples for I/O-bound tasks

### Key Learnings:
- When to use multi-threading vs. multiprocessing
- Thread synchronization mechanisms (locks, events, conditions)
- Avoiding common threading pitfalls
- Performance benefits for I/O-bound operations

---

## Chapter 5: Pydantic

**Location:** `Ch-5_Pydantic/`

Learn data validation and serialization using Pydantic, essential for data pipelines.

### Topics Covered (Jupyter Notebooks):
- **1_basics.ipynb** - Core concepts: models, validation, type hints
  - Creating Pydantic models
  - Automatic type validation
  - Configuration options
  
- **2_Fields.ipynb** - Advanced field configurations
  - Field constraints and validators
  - Custom validation logic
  - Nested models and complex types
  
- **3_Serialization.ipynb** - Serialization and deserialization
  - Converting models to dictionaries and JSON
  - Handling complex data types
  - Schema generation

### Key Learnings:
- Building robust data validation pipelines
- Ensuring data quality at ingestion points
- Serialization for APIs and storage
- Integration with FastAPI and other frameworks

---

## Chapter 6: Asynchronous Programming

**Location:** `Ch-6_Async/`

Harness async/await for highly concurrent, non-blocking operations.

### Topics Covered:
- **1_basics.py** - Async fundamentals: coroutines, event loops, and async/await syntax
- **2_await_api.py** - Calling async functions and handling single API requests
- **3_multiple_apis.py** - Managing concurrent API calls with `asyncio.gather()`
- **4_multiple_tasks.py** - Coordinating multiple async tasks with different timing patterns

### Key Learnings:
- Event loop mechanics and the async runtime
- Writing async functions and coroutines
- Efficient concurrent I/O with minimal overhead
- Task scheduling and coordination
- Far superior performance compared to threading for I/O operations

---

## Chapter 7: APIs

**Location:** `Ch-7_APIs/`

Master HTTP APIs and integration patterns for data retrieval.

### Topics Covered (Jupyter Notebook):
- **1_apis.ipynb** - Working with REST APIs
  - Making HTTP requests (GET, POST, PUT, DELETE)
  - Handling authentication and headers
  - Parsing and processing JSON responses
  - Error handling and retries
  - Real-world API integration examples

### Key Learnings:
- HTTP fundamentals for data engineers
- API authentication and security
- Data parsing and transformation
- Building robust API clients
- Integration with data pipelines

---

## Chapter 8: PyTest

**Location:** `Ch-8_PyTest/`

Write comprehensive tests to ensure code quality and reliability.

### Topics Covered:
- **1_Basics/**
  - `main.py` - Simple functions to test
  - `test_main.py` - Basic pytest assertions and test structure
  
- **2_Classes/**
  - `main.py` - Class implementations for testing
  - `test_main.py` - Testing class methods and properties
  
- **3_CheckErrors/**
  - `main.py` - Functions that raise exceptions
  - `test_main.py` - Testing exception handling with `pytest.raises()`
  
- **4_Parametrized_Testing/**
  - `main.py` - Functions requiring multiple test inputs
  - `test_main.py` - Using `@pytest.mark.parametrize` for data-driven tests
  
- **Mocks/**
  - `main.py` - Code with external dependencies
  - `test_main.py` - Mocking external dependencies and side effects

### Key Learnings:
- Writing clear, maintainable test cases
- Testing class-based code
- Exception testing strategies
- Parametrized tests for comprehensive coverage
- Mocking and dependency injection for isolated tests
- Creating reproducible test environments

---

## Chapter 9: OS Operations

**Location:** `Ch-9_OS/`

Work with the operating system for file handling and system tasks.

### Topics Covered:
- **1_basics.py** - File and directory operations
  - Reading and writing files
  - Directory traversal and manipulation
  - Path handling and normalization
  - File metadata and permissions
  - Working with CSV, JSON, and other formats

### Sample Data:
- `Data/` directory contains time-series CSV files:
  - `2026-01-01.csv`
  - `2026-01-14.csv`
  - `2026-01-15.csv`

### Key Learnings:
- Cross-platform file handling with `pathlib`
- Efficient data file operations
- Directory organization and automation
- File I/O best practices
- Working with various data formats

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip or conda for package management

### Installation

1. **Clone or download the repository:**
   ```bash
   git clone <repository-url>
   cd PythonAdvanced
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   source .venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Recommended Setup
This course recommends using Jupyter notebooks for interactive learning, especially for chapters 5 and 7.

---

## 📂 Project Structure

```
PythonAdvanced/
├── Ch-1_OOP/              # Object-Oriented Programming
│   ├── 1_basics.py
│   ├── 2_constructors.py
│   ├── 3_encapsulation.py
│   ├── 4_DataExt_Class.py
│   ├── 5_methods.py
│   └── Files/             # Sample data files
├── Ch-2_Inheritance/      # Inheritance patterns
├── Ch-3_Polymorphism&Decorators/  # Polymorphism & Decorators
├── Ch-4_Multi-Threading/  # Concurrent programming
├── Ch-5_Pydantic/         # Data validation with Pydantic
├── Ch-6_Async/            # Asynchronous programming
├── Ch-7_APIs/             # Working with APIs
├── Ch-8_PyTest/           # Testing with pytest
│   ├── 1_Basics/
│   ├── 2_Classes/
│   ├── 3_CheckErrors/
│   ├── 4_Parametrized_Testing/
│   └── Mocks/
├── Ch-9_OS/               # OS and file operations
│   └── Data/              # Sample data files
└── README.md              # This file
```

---

## 💡 Learning Tips

1. **Follow the Progressive Difficulty:** Start with Chapter 1 and progress sequentially. Each chapter builds on previous concepts.

2. **Code Along:** Don't just read the code—execute it, modify it, and experiment.

3. **Run Tests:** Chapter 8 provides excellent examples of how code should be tested. Study the test patterns.

4. **Interactive Learning:** Use Jupyter notebooks (Chapters 5 & 7) for interactive exploration.

5. **Real-World Context:** Each chapter is designed with data domain applications in mind. Consider how concepts apply to your specific use case.

---

## 🔧 Common Commands

### Running Python Files
```bash
python Ch-1_OOP/1_basics.py
```

### Running Jupyter Notebooks
```bash
jupyter notebook Ch-5_Pydantic/1_basics.ipynb
```

### Running Tests
```bash
# Run all tests in Ch-8_PyTest
pytest Ch-8_PyTest/

# Run specific test file
pytest Ch-8_PyTest/1_Basics/test_main.py -v

# Run with coverage
pytest Ch-8_PyTest/ --cov
```

---

## 🎯 Learning Outcomes

By completing this tutorial, you will be able to:

✅ Design and implement robust object-oriented Python applications  
✅ Create complex class hierarchies using inheritance  
✅ Write flexible, maintainable code with polymorphism and decorators  
✅ Leverage multi-threading and async programming for concurrent operations  
✅ Validate and serialize data with Pydantic  
✅ Integrate with external APIs efficiently  
✅ Write comprehensive test suites with pytest  
✅ Perform file and OS operations across platforms  

---



## 📌 Key Concepts Summary

| Concept | Chapter | Why Important |
|---------|---------|---------------|
| OOP Design | 1 | Foundation for scalable code |
| Inheritance | 2 | Code reuse and structure |
| Polymorphism | 3 | Flexible, extensible systems |
| Multi-Threading | 4 | Concurrent I/O operations |
| Data Validation | 5 | Data quality and integrity |
| Async/Await | 6 | High-performance I/O |
| API Integration | 7 | Data ingestion and services |
| Testing | 8 | Code reliability and maintenance |
| File Operations | 9 | Data handling and persistence |

---

## 🔗 Resources

- [Official Python Documentation](https://docs.python.org/3/)
- [Pydantic Documentation](https://pydantic-settings.readthedocs.io/)
- [AsyncIO Documentation](https://docs.python.org/3/library/asyncio.html)
- [Pytest Documentation](https://docs.pytest.org/)
- [Real Python Articles](https://realpython.com/)

---

## 📝 Notes

- Each chapter is self-contained but builds on foundational OOP concepts from Chapter 1
- Sample data files are provided for practical exercises
- All code examples are tested and production-ready patterns
- The tutorial emphasizes practical application over pure theory

---

## ❓ Troubleshooting

### Import Errors
Ensure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### Jupyter Not Found
Install Jupyter:
```bash
pip install jupyter notebook
```

### Test Failures
Make sure you're in the correct directory and all files are in place.

---

## 📧 Feedback

This is a comprehensive tutorial designed for professional development. If you find any issues or have suggestions for improvements, please review the code examples and refer to the official documentation of each library.

---

**Last Updated:** April 2026  
**Python Version:** 3.8+  
**License:** Educational Use
