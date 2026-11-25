# QA test plan

| Case | Expected behavior |
|---|---|
| CART-01 | Add/remove updates quantity and total |
| CART-02 | Empty cart rejected |
| CHECK-01 | Invalid email blocks submission |
| CHECK-02 | Terms required |
| CHECK-03 | Valid order clears cart |
| A11Y-01 | Keyboard activation and nonnegative quantity |

Illustrative hypothetical defect CART-002: removing from an empty cart could produce a negative total. Expected: zero units and $0.00. The regression test covers this risk; the fixture guards against it. Not an observed defect.

Out of scope: actual payments, external integrations, load testing and cross-browser coverage.
