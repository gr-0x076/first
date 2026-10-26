# ReLU Activation

Beginner | problemset | dl-core | activation-functions

Apply the ReLU activation element-wise: $\max(0,x)$.

Implement `solve(x)`.

**Returns.** Return a NumPy array of the same shape: negative values become $0$, others are unchanged.

### Examples

**Example 1**

Input:

```python
solve([-2, 0, 3])
```

Output:

```text
[0, 0, 3]
```

**Example 2**

Input:

```python
solve([[-1.5, 2.5], [0.0, -0.1]])
```

Output:

```text
[[0.0, 2.5], [0.0, 0.0]]
```
