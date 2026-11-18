---
name: swift-notes
description: Python vs Swift differences for an iOS developer practicing DSA in Python. Use whenever a problem touches something that works differently in Swift (strings, heaps, deques, dictionaries, integer math, recursion, mutation), so a short "In Swift..." hint can be added. Also use when the user asks how to write a solution in Swift.
---

# Swift Notes (for a Python-first learner who interviews for iOS roles)

The learner solves problems in **Python**. They are an iOS developer, and some interviews may ask for Swift. When the current problem uses something on this list, add **one short line** at the end of your reply:

> 🍎 **Swift note:** <the difference, in one or two sentences>

Rules:
- Only when relevant to the code in front of you. Never more than one or two notes per reply.
- Do not convert their solution to Swift unless they ask.
- Do not put Swift notes inside a mock interview (Interview mode) until the feedback report.
- If they ask "how would this look in Swift?", give the Swift version and point out the differences below.

## The differences that matter in DSA problems

### Strings
- **Indexing is not O(1).** `s[i]` is not allowed; Swift uses `String.Index`, and moving an index is O(n) because characters vary in byte length. Convert once: `let chars = Array(s)`, then `chars[i]` is O(1).
- Slicing `s[a..<b]` needs indices and returns a `Substring`; wrap it in `String(...)` to store it.
- No `s.isdigit()` style helpers on String; use `Character` properties: `c.isNumber`, `c.isLetter`, `c.isUppercase`, `c.lowercased()`.
- `"".join(list)` becomes `list.joined()` or `list.joined(separator: " ")`.
- `s.split()` returns `[Substring]`; map with `.map(String.init)` if you need `[String]`.
- `ord(c)` becomes `c.asciiValue!` (a `UInt8`, so convert to `Int`).

### Collections
- **No built-in heap / priority queue.** Python has `heapq`; in Swift you write a small heap or use swift-collections `Heap` if allowed. In a live interview, expect to write it.
- **No built-in deque.** `collections.deque` has O(1) `popleft()`. In Swift, `array.removeFirst()` is O(n). Use an index pointer (`var head = 0`) or swift-collections `Deque`.
- `Counter(x)` becomes `Dictionary(x.map { ($0, 1) }, uniquingKeysWith: +)` or a loop with `dict[key, default: 0] += 1`.
- `defaultdict(list)` becomes `dict[key, default: []].append(x)`.
- Dictionary lookup returns an Optional: `dict[key]` is `Int?`, so unwrap it.
- `set` is `Set<T>`; elements must be `Hashable`. Tuples are not Hashable, so for "visited (r, c)" use a struct or encode as `r * cols + c`.
- `sorted(x, key=...)` becomes `x.sorted { a, b in ... }` (a comparator, not a key function).
- Python negative indexing (`a[-1]`) does not exist; use `a.last!` or `a[a.count - 1]`.

### Numbers
- `Int` overflows and crashes on overflow, unlike Python's unlimited ints. Watch sums and products in big inputs.
- `//` floor division: Swift `/` on Ints truncates toward zero, so negative numbers differ from Python. `-7 / 2` is `-3` in Swift and `-4` in Python.
- `%` with negatives also differs: `-7 % 3` is `-1` in Swift and `2` in Python.
- `float('inf')` becomes `Int.max` or `Double.infinity`.

### Values, references, and mutation
- Arrays, Strings, and Dictionaries are **value types** (copied on assignment). Passing an array to a function and mutating it needs `inout` and `&arr`.
- Linked list and tree nodes should be `class` (reference type), not `struct`. Use `weak var` for `prev`/parent pointers to avoid retain cycles in real code.
- Optional chaining replaces `None` checks: `node?.next?.val`.
- Classes need an explicit `init`; there is no `__init__` with default `self`.

### Recursion and functions
- No default recursion limit like Python's ~1000, but deep recursion can still overflow the stack.
- `@lru_cache` has no Swift equivalent; use a `[Key: Value]` memo dictionary.
- Nested functions work, and they capture outer variables, which is handy for DFS helpers.

### Two-pointer and loop syntax
- `for i in range(n)` becomes `for i in 0..<n`; reverse: `for i in stride(from: n - 1, through: 0, by: -1)`.
- `enumerate(a)` becomes `a.enumerated()` (returns `offset, element`).
- `zip(a, b)` works the same: `zip(a, b)`.
- Swapping: `a.swapAt(i, j)` or `(a[i], a[j]) = (a[j], a[i])`.

If something comes up that is not on this list, add it here so the next session has it.
