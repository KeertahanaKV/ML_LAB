sns.boxplot(data=np.random.randn(100))
plt.show()

# Alpha-Beta Pruning
def ab(depth, idx, maxP, vals, a, b):
    if depth == 2: return vals[idx]
    if maxP:
        val = -999
        for i in range(2):
            val = max(val, ab(depth+1, idx*2+i, False, vals, a, b))
            a = max(a, val)
            if b <= a: break
        return val
    else:
        val = 999
        for i in range(2):
            val = min(val, ab(depth+1, idx*2+i, True, vals, a, b))
            b = min(b, val)
            if b <= a: break
        return val
print("Result:", ab(0, 0, True, [3, 5, 6, 9], -999, 999))