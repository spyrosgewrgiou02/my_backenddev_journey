# 🐍 Python Backend Engineering Lab

This repository serves as my structured learning hub and portfolio as I transition from a security analysis (SOC L1) background into **Backend Software Engineering**. 

Instead of building simple scripts, every lab here is approached with a **production-ready and security-first mindset**, focusing on data integrity, secure inputs, and clean system logic.

---

## Repository Roadmap & Projects:


### 📁 Folder: `01_fundamentals/`
*Core focus: Python syntax engines, control flow integrity, and processing standard user streams.*

#### 🔹 Project Name: `cost_estimator.py`
* **What it does:** Calculates and standardizes daily operational costs for running specific cloud assets (like databases or background worker servers).
* **Why it works:** It handles dynamic console input validation, casts strings into appropriate mathematical data types (`float`, `int`), and formats values safely into user-facing output templates using modern python `f-strings`.

#### 🔹 Project Name: `security_gateway.py`
* **What it does:** Evaluates and processes inbound API authentication strings against preset authorization parameters.
* **Why it works:** It uses proactive string sanitization via `.strip()` to eliminate unintended whitespaces before processing, then utilizes python truthiness evaluations (`if not token`) to intercept empty payloads before downstream systems are hit.

#### 🔹 Project Name: `log_scanner.py`
* **What it does:** Simulates a firewall network traffic scanner parsing a list of target IP addresses.
* **Why it works:** It leverages a `for` loop to automate repetitive scanning tasks, executing control flow manipulations via `continue` to seamlessly pass trusted internal traffic and `break` to execute emergency loops stops when specific markers are triggered.

---

### 📁 Folder: `02_core_data_structures/`
*Core focus: Advanced data primitives, object mutability vs immutability, and indexing structures.*

#### 🔹 Project Name: `payload_extractor.py`
* **What it does:** Breaks down raw, unformatted server error logs into structured, isolated components.
* **Why it works:** It leverages python string manipulation methods to slice and separate text streams into high-performance lists, allowing precise data recovery via list indexing.

#### 🔹 Project Name: `traffic_analyzer.py`
* **What it does:** Filters noisy network traffic log inputs to identify distinct unique visitors.
* **Why it works:** It uses Python `set` conversions to instantly drop duplicate string metrics from a data pool and relies on immutable `tuples` to securely store hardcoded configuration points that must remain unmodified during execution.

#### 🔹 Project Name: `user_permissions.py`
* **What it does:** Maps and models a mock user's profile metadata and permissions attributes.
* **Why it works:** It implements structured key-value maps via Python `dictionaries` to mirror JSON payloads, executing multi-conditional boolean evaluations (`and`) to dynamically approve or deny administrative system access.

---

### 📁 Folder: `03_functions/`
*Core focus: Modular code design, input/output structures, parameters, and logical returns.*

#### 🔹 Project Name: `clamp_number.py`
* **What it does:** Ensures a given number stays strictly within a set minimum and maximum boundary.
* **Why it works:** It uses multi-conditional branching (`if`/`elif`) to evaluate numerical ranges and returns clamped boundary values when limits are exceeded.

#### 🔹 Project Name: `domain_extractor.py`
* **What it does:** Safely parses an email address string to extract the host domain name.
* **Why it works:** It utilizes Python's `.split()` method to break the string at the `@` symbol, directly returning the second element of the resulting list.

#### 🔹 Project Name: `list_averager.py`
* **What it does:** Calculates the mathematical average of any list of numbers.
* **Why it works:** It combines Python's built-in `sum()` and `len()` functions to perform division, including a defensive check to prevent division-by-zero errors on empty lists. 

#### 🔹 Project Name: `log_formatter.py`
* **What it does:** Formats system log entries with an optional custom severity level.
* **Why it works:** It implements a default parameter value (`level = "INFO"`) and processes string case normalization (`.upper()`) dynamically to standardize log formats.

#### 🔹 Project Name: `power_calculator.py`
* **What it does:** Calculates the power of a base number raised to an exponent.
* **Why it works:** It uses a default parameter to square the number by default (`exponent = 2`), returning a raw, mathematical `int` or `float` for flexible downstream calculations.

#### 🔹 Project Name: `task_scheduler.py`
* **What it does:** Appends task descriptions to a scheduler list safely.
* **Why it works:** It avoids Python's classic mutable default argument trap by initializing the parameter default to `None` and instantiating a clean local list using identity validation (`is None`).

#### 🔹 Project Name: `dynamic_concatenator.py`
* **What it does:** Concatenates an arbitrary number of string inputs using hyphens.
* **Why it works:** Uses `*args` to collect variable positional arguments into a tuple and joins them efficiently using `"-".join()`.

#### 🔹 Project Name: `profile_card_generator.py`
* **What it does:** Generates a structured multi-line profile card from keyword arguments.
* **Why it works:** Uses `**kwargs` to process key-value metadata, capitalizing labels and joining lines with newline (`\n`) characters.

#### 🔹 Project Name: `order_total_calculator.py`
* **What it does:** Calculates total customer expenditure based on dynamic item-price pairings.
* **Why it works:** Combines a required positional parameter (`customer_name`) with `**kwargs` to accumulate item costs from a dictionary's values.