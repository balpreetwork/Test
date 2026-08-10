from decimal import Decimal, getcontext
import sys

# Set high decimal precision context
getcontext().prec = 10000  

print("Streaming true digits of Pi using Python's decimal module...")
print("Press Ctrl + C at any time to stop.\n")

try:
    # Chudnovsky algorithm components for calculating Pi efficiently
    q, r, t, k, n, l = Decimal(1), Decimal(0), Decimal(1), Decimal(1), Decimal(3), Decimal(3)
    
    print("3", end=".", flush=True)
    
    while True:
        if 4 * q + r - t < n * t:
            print(n, end="", flush=True)
            q, r, t, k, n, l = (
                Decimal(10) * q,
                Decimal(10) * (r - n * t),
                t,
                k,
                (Decimal(10) * (3 * q + r)) // t - Decimal(10) * n,
                l,
            )
        else:
            q, r, t, k, n, l = (
                q * k,
                (2 * q + r) * l,
                t * l,
                k + 1,
                (q * (7 * k + 2) + r * l) // (t * l),
                l + 2,
            )

except KeyboardInterrupt:
    print("\n\n[Kill Switch Activated!] Stopped streaming Pi.")